#!/usr/bin/env python3
"""Validate the curriculum and progress registers.

Standard library only. Run from anywhere:

    python3 scripts/validate.py
    python3 scripts/validate.py --schedules-text path/to/schedules.txt     # adds the source-fidelity audit

The optional audit needs the plain text of the Cambridge Schedules PDF, which is not stored in this
repository (copyright). scripts/extract_pdf_text.py produces it (needs the third-party package pypdf).

Exit status is 0 when every check passes and 1 otherwise.
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ERRORS = []
WARNINGS = []

STATUSES = {"examinable", "starred-not-examinable", "course-note", "ancillary-non-examinable"}
MASTERY = ["unassessed", "familiarity", "understanding", "independent-competence", "durable-mastery"]
COVERAGE = {"not-started", "in-progress", "covered"}
BASES = {"cambridge-stated", "librarian-judgement"}
VERIFICATION = {"verified", "partially verified", "unverified"}
LECTURES = {"GP": 24, "VM": 24, "NS": 24, "DE": 24, "AN": 24, "PR": 24, "VC": 24, "DR": 24, "MC": 10, "CP": 8}
ASSESSOR = "ChatGPT-assessor"


def err(msg):
    ERRORS.append(msg)


def warn(msg):
    WARNINGS.append(msg)


# ------------------------------------------------------------------ the restricted YAML subset
def load_register(path):
    """Parse '- key: value' records whose values are JSON scalars/arrays (see coverage.yaml header)."""
    records, cur = [], None
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^(- |  )([A-Za-z_]+): (.*)$", line)
        if not m:
            err(f"{path.name}:{n}: line is not in the register subset: {line[:60]!r}")
            continue
        if m.group(1) == "- ":
            cur = {}
            records.append(cur)
        if cur is None:
            err(f"{path.name}:{n}: field before first record")
            continue
        try:
            cur[m.group(2)] = json.loads(m.group(3))
        except json.JSONDecodeError as e:
            err(f"{path.name}:{n}: value is not valid JSON ({e.msg})")
    return records


# ------------------------------------------------------------------ checks
def check_ids(cov):
    seen = set()
    for r in cov:
        i = r.get("id", "")
        if not re.fullmatch(r"IA-[A-Z]{2}-(N\d{2}|\d{3})", i):
            err(f"coverage: malformed id {i!r}")
        if i in seen:
            err(f"coverage: duplicate id {i}")
        seen.add(i)
        for k in ("course", "heading", "source", "location", "status", "prerequisites", "readings"):
            if k not in r:
                err(f"coverage: {i} missing field {k}")
        if r.get("status") not in STATUSES:
            err(f"coverage: {i} has invalid status {r.get('status')!r}")
        if not str(r.get("source", "")).strip():
            err(f"coverage: {i} has an empty source statement")
    return seen


def check_prerequisites(cov, ids):
    graph = {}
    for r in cov:
        i, pre = r["id"], r.get("prerequisites", [])
        graph[i] = pre
        for p in pre:
            if p not in ids:
                err(f"coverage: {i} prerequisite {p} does not exist")
            if p == i:
                err(f"coverage: {i} lists itself as a prerequisite")
        if pre and r.get("prereq_basis") not in BASES:
            err(f"coverage: {i} has prerequisites but prereq_basis {r.get('prereq_basis')!r} is invalid")
        if not pre and r.get("prereq_basis") is not None:
            err(f"coverage: {i} has prereq_basis but no prerequisites")
    state = {}

    def visit(n, path):
        if state.get(n) == 2:
            return
        if state.get(n) == 1:
            err("coverage: prerequisite cycle: " + " -> ".join(path + [n]))
            return
        state[n] = 1
        for p in graph.get(n, []):
            if p in graph:
                visit(p, path + [n])
        state[n] = 2

    for n in graph:
        visit(n, [])


def check_lectures(cov):
    per_block = {}
    for r in cov:
        code = r["id"].split("-")[1]
        if r.get("block") and r.get("lectures_in_block") is not None:
            seen = per_block.setdefault(code, {})
            if seen.setdefault(r["block"], r["lectures_in_block"]) != r["lectures_in_block"]:
                err(f"lectures: {r['id']} disagrees with other items in block {r['block']} on lectures_in_block")
    for code, want in LECTURES.items():
        got = sum(per_block.get(code, {}).values())
        if got != want:
            err(f"lectures: {code} blocks sum to {got}, expected {want}")


def check_mastery(cov, mas):
    topic_ids = {r["id"] for r in cov if r["status"] != "course-note"}
    mids = [m.get("id") for m in mas]
    if len(mids) != len(set(mids)):
        err("mastery: duplicate ids")
    for i in topic_ids - set(mids):
        err(f"mastery: {i} has no state record")
    for i in set(mids) - topic_ids:
        err(f"mastery: {i} is not a syllabus item (or is a course note)")
    for m in mas:
        i = m.get("id")
        if m.get("mastery") not in MASTERY:
            err(f"mastery: {i} invalid mastery {m.get('mastery')!r}")
        if m.get("coverage") not in COVERAGE:
            err(f"mastery: {i} invalid coverage {m.get('coverage')!r}")
        ev = m.get("evidence", [])
        if m.get("mastery") == "unassessed":
            if ev or m.get("authorised_by") or m.get("authorised_date"):
                err(f"mastery: {i} is unassessed but carries evidence or authorisation")
        else:
            if not ev:
                err(f"mastery: {i} is {m.get('mastery')} with no evidence")
            if m.get("authorised_by") != ASSESSOR:
                err(f"mastery: {i} is {m.get('mastery')} without authorisation by {ASSESSOR}")
            if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", str(m.get("authorised_date") or "")):
                err(f"mastery: {i} authorised_date must be DD/MM/YYYY")
            for e in ev:
                if not (ROOT / e).exists():
                    err(f"mastery: {i} evidence path {e} does not exist")


def parse_entries(path, prefix):
    """Entries are '### PREFIX-... title' headings followed by '- Field: value' bullets."""
    entries, cur = {}, None
    if not path.exists():
        err(f"missing file {path.relative_to(ROOT)}")
        return entries
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(rf"^### ({prefix}[A-Z0-9-]*)\b", line)
        if m:
            cur = entries.setdefault(m.group(1), {})
            continue
        if line.startswith("#"):
            cur = None
        m = re.match(r"^- ([A-Za-z ]+): (.*)$", line)
        if cur is not None and m:
            cur[m.group(1).strip().lower()] = m.group(2).strip()
    return entries


def check_bibliography(bib):
    for i, e in bib.items():
        v = e.get("verification", "")
        if v not in VERIFICATION:
            err(f"bibliography: {i} verification {v!r} must be one of {sorted(VERIFICATION)}")
        if v in ("verified", "partially verified") and not re.search(r"https?://", e.get("verified via", "")):
            err(f"bibliography: {i} is {v} but has no 'Verified via' URL")
        if v == "unverified" and e.get("verified via", "").startswith("http"):
            warn(f"bibliography: {i} is unverified yet cites a source - upgrade or explain")


def check_readings(cov, rm, bib):
    for r in cov:
        for x in r.get("readings", []):
            if x not in rm:
                err(f"reading-map: {r['id']} cites {x}, which is not defined in curriculum/reading-map.md")
    text = (ROOT / "curriculum" / "reading-map.md").read_text(encoding="utf-8")
    for b in set(re.findall(r"\bBIB-\d{3}\b", text)):
        if b not in bib:
            err(f"reading-map: cites {b}, which is not defined in references/bibliography.md")


def check_syllabus_md(ids):
    p = ROOT / "curriculum" / "syllabus.md"
    text = p.read_text(encoding="utf-8") if p.exists() else ""
    for i in sorted(ids):
        if i not in text:
            err(f"syllabus.md does not list {i}")


def check_links():
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)\)", text):
            target = m.group(1)
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            t = target.split("#")[0]
            if t and not (md.parent / t).resolve().exists():
                err(f"{md.relative_to(ROOT)}: broken link to {target}")


# ------------------------------------------------------------------ optional source-fidelity audit
def norm(s):
    s = s.replace("’", "'").replace("M¨ obius", "Möbius").replace("Hˆ opital", "Hôpital")
    s = s.replace("V ector", "Vector")
    return re.sub(r"[\s\-]+", "", s)


TITLE_RE = {
    "GP": r"^GROUPS 24 lectures", "VM": r"^VECTORS AND MA TRICES 24", "NS": r"^NUMBERS AND SETS 24",
    "DE": r"^DIFFERENTIAL EQUA TIONS 24", "AN": r"^ANAL YSIS I 24", "PR": r"^PROBABILITY 24 lectures, Lent",
    "VC": r"^VECTOR CALCULUS 24", "DR": r"^DYNAMICS AND RELA TIVITY 24",
}


def audit_source(cov, schedules_text):
    """(1) every source statement occurs verbatim in the Schedules; (2) nothing is left unmapped."""
    pages, cur = {}, 0
    for ln in schedules_text.splitlines():
        m = re.match(r"=====PAGE (\d+)=====", ln)
        if m:
            cur = int(m.group(1))
            continue
        if 10 <= cur <= 14 and not re.match(r"^P AR T IA \d+$", ln.strip()):
            pages.setdefault(cur, []).append(ln)
    stream = [ln for p in sorted(pages) for ln in pages[p]]
    starts = {}
    for code, rx in TITLE_RE.items():
        idx = [i for i, ln in enumerate(stream) if re.match(rx, ln.strip())]
        if len(idx) != 1:
            err(f"audit: could not locate the {code} title line in the Schedules text")
            return
        starts[code] = idx[0]
    order = sorted(starts, key=starts.get)
    ends = {}
    for k, code in enumerate(order):
        lim = starts[order[k + 1]] if k + 1 < len(order) else len(stream)
        ends[code] = next(i for i in range(starts[code], lim) if stream[i].strip() == "Appropriate books")
    checked = 0
    errors_before = len(ERRORS)
    for code in order:
        seg = norm("\n".join(stream[starts[code] + 1:ends[code]]))
        items = [r for r in cov if r["id"].split("-")[1] == code and r["status"] != "ancillary-non-examinable"]
        heads = {norm(r["heading"]) for r in items if not r["heading"].startswith("(")}
        pos = 0
        for r in items:
            s = norm(r["source"])
            j = seg.find(s, pos)
            if j < 0:
                err(f"audit: {r['id']} source statement not found in order in the Schedules text")
                continue
            gap = seg[pos:j]
            for h in sorted(heads, key=len, reverse=True):
                gap = gap.replace(h, "")
            gap = re.sub(r"\[\d+\]\.?", "", gap)
            gap = re.sub(r"\d+lectures,(Michaelmas|Lent|Easter)Term(ofPartIA)?", "", gap).replace("∗", "").replace("*", "")
            if gap.strip(" .,;:"):
                err(f"audit: unmapped Schedules text before {r['id']}: {gap[:80]!r}")
            pos = j + len(s)
            checked += 1
        tail = re.sub(r"\[\d+\]\.?", "", seg[pos:])
        if tail.strip(" .,;:*∗"):
            err(f"audit: unmapped Schedules text at end of {code}: {tail[:80]!r}")
    if len(ERRORS) == errors_before:
        print(f"audit: {checked} items matched in order against the Schedules text with no unmapped gaps")
    else:
        print(f"audit: {len(ERRORS) - errors_before} problem(s) found (see below)")


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--schedules-text", help="plain text of schedules.pdf, for the source-fidelity audit")
    args = ap.parse_args()

    cov = load_register(ROOT / "curriculum" / "coverage.yaml")
    mas = load_register(ROOT / "progress" / "mastery.yaml")
    ids = check_ids(cov)
    check_prerequisites(cov, ids)
    check_lectures(cov)
    check_mastery(cov, mas)
    bib = parse_entries(ROOT / "references" / "bibliography.md", "BIB-")
    rm = parse_entries(ROOT / "curriculum" / "reading-map.md", "RM-")
    check_bibliography(bib)
    check_readings(cov, rm, bib)
    check_syllabus_md({r["id"] for r in cov})
    check_links()
    if args.schedules_text:
        audit_source(cov, pathlib.Path(args.schedules_text).read_text(encoding="utf-8"))
    else:
        warn("source-fidelity audit skipped (no --schedules-text given)")

    by = {}
    for r in cov:
        by.setdefault(r["id"].split("-")[1], 0)
        by[r["id"].split("-")[1]] += 1
    print("register records by course code:", ", ".join(f"{k}={v}" for k, v in sorted(by.items())))
    print(f"bibliography entries: {len(bib)}; reading-map entries: {len(rm)}; mastery records: {len(mas)}")
    for w in WARNINGS:
        print("WARNING:", w)
    for e in ERRORS:
        print("ERROR:", e)
    print("RESULT:", "FAIL" if ERRORS else "PASS", f"({len(ERRORS)} errors, {len(WARNINGS)} warnings)")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
