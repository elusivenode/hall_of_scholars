#!/usr/bin/env python3
"""Validate the curriculum and progress registers.

Standard library only. Run from anywhere:

    python3 scripts/validate.py
    python3 scripts/validate.py --schedules-text path/to/schedules.txt     # adds the local source audit

WHAT THIS DOES AND DOES NOT ESTABLISH
  It checks structure: unique and well-formed ids, required fields, valid references between registers, typed
  relationships without ordering cycles, lecture counts, mastery-record rules (evidence, authorisation, hint level,
  history and the 28-day interval), bibliography status fields, session-record structure, and internal links.
  It does NOT establish mathematical correctness, it cannot authenticate that an assessment decision really came from the
  assessor, and it cannot tell whether a summary is a faithful rendering of the Cambridge source.
  The optional source audit uses a local copy of the Cambridge Schedules (which is NOT stored in this repository). Each
  register item carries the length and SHA-256 of its normalised source passage; the audit checks that those passages tile
  the Schedules text in order with no unmapped syllabus text. A pass means the register was built from that edition of the
  document. It is NOT proof of semantic equivalence between a summary and its source: that is an academic judgement.

The Schedules text comes from scripts/extract_pdf_text.py (needs the third-party package pypdf). The fingerprints were
calibrated on pypdf 6.21.2 output; another extractor may differ in spacing, ligatures or accents (use --show-mismatch).

Exit status is 0 when every check passes and 1 otherwise.
"""
import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ERRORS = []
WARNINGS = []

STATUSES = {"examinable", "starred-not-examinable", "course-note", "ancillary-non-examinable"}
MASTERY = ["unassessed", "familiarity", "understanding", "independent-competence", "durable-mastery"]
COVERAGE = {"not-started", "in-progress", "covered"}
REL_TYPES = {"required", "recommended", "connection"}
PROVENANCE = {"cambridge-stated", "inferred-from-cambridge", "librarian-judgement", "director-approved"}
QUALIFIERS = {"statement-only", "informal-treatment", "informal-proof", "proof-sketch", "proof-given", "brief", "revision"}
SUMMARY_STATUS = {"librarian-draft", "reviewed"}
HINTS = {"none", "minor", "substantial", "unknown"}
BIB_STATUS = {"verified", "partial", "unverified"}
ALIGN_STATUS = {"checked", "partial", "not-checked"}
LECTURES = {"GP": 24, "VM": 24, "NS": 24, "DE": 24, "AN": 24, "PR": 24, "VC": 24, "DR": 24, "MC": 10, "CP": 8}
ASSESSOR = "ChatGPT-assessor"
DURABLE_INTERVAL_DAYS = 28
COPY_RUN = 56          # letters (about 9 words) of shared text that trigger the possible-copying warning
REQUIRED_COV = ("id", "course", "heading", "summary", "summary_status", "qualifiers", "source_doc", "printed_page", "pdf_page",
                "block", "block_item", "lectures_in_block", "status", "builds_on", "readings", "fingerprint")
SESSION_NAME = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{2}-[a-z0-9-]+\.md$")
SESSION_HEADINGS = ("## Exchanges", "## Unresolved misconceptions", "## Assessment decisions", "## Coverage updates",
                    "## Next question or exercise", "## Addenda")
EXCHANGE_FIELDS = ("Question (exact)", "Student response (verbatim)", "Hints given", "Tutor evaluation", "Item ids",
                   "Source references")


def err(msg):
    ERRORS.append(msg)


def warn(msg):
    WARNINGS.append(msg)


# ------------------------------------------------------------------ the restricted YAML subset
def load_register(path):
    """Parse '- key: value' records whose values are JSON (see the header of coverage.yaml)."""
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


# ------------------------------------------------------------------ syllabus register
def check_ids(cov):
    seen = set()
    for r in cov:
        i = r.get("id", "")
        if not re.fullmatch(r"IA-[A-Z]{2}-(N\d{2}|\d{3})", i):
            err(f"coverage: malformed id {i!r}")
        if i in seen:
            err(f"coverage: duplicate id {i}")
        seen.add(i)
        for k in REQUIRED_COV:
            if k not in r:
                err(f"coverage: {i} missing field {k}")
        if r.get("status") not in STATUSES:
            err(f"coverage: {i} has invalid status {r.get('status')!r}")
        if not str(r.get("summary", "")).strip():
            err(f"coverage: {i} has an empty summary")
        if r.get("summary_status") not in SUMMARY_STATUS:
            err(f"coverage: {i} has invalid summary_status {r.get('summary_status')!r}")
        for t in r.get("qualifiers", []):
            if t not in QUALIFIERS:
                err(f"coverage: {i} has unknown qualifier {t!r}")
        fp = r.get("fingerprint")
        if not (isinstance(fp, dict) and isinstance(fp.get("chars"), int) and re.fullmatch(r"[0-9a-f]{64}", str(fp.get("sha256", "")))):
            err(f"coverage: {i} has a malformed fingerprint")
        if "source" in r:
            err(f"coverage: {i} carries a verbatim 'source' field; the public register must not reproduce Cambridge text")
        if not isinstance(r.get("printed_page"), int) or not isinstance(r.get("pdf_page"), int):
            err(f"coverage: {i} needs integer printed_page and pdf_page")
    return seen


def check_relations(cov, ids):
    graph = {}
    counts = {"type": {}, "prov": {}}
    for r in cov:
        i = r["id"]
        edges = r.get("builds_on", [])
        if not isinstance(edges, list):
            err(f"coverage: {i} builds_on must be a list")
            continue
        seen = set()
        for e in edges:
            if not (isinstance(e, list) and len(e) == 3):
                err(f"coverage: {i} has a malformed relation {e!r} (want [id, type, provenance])")
                continue
            tgt, typ, prov = e
            if tgt not in ids:
                err(f"coverage: {i} relation to {tgt} - that id does not exist")
            if tgt == i:
                err(f"coverage: {i} relates to itself")
            if tgt in seen:
                err(f"coverage: {i} lists {tgt} more than once")
            seen.add(tgt)
            if typ not in REL_TYPES:
                err(f"coverage: {i} -> {tgt} has invalid type {typ!r}")
            if prov not in PROVENANCE:
                err(f"coverage: {i} -> {tgt} has invalid provenance {prov!r}")
            counts["type"][typ] = counts["type"].get(typ, 0) + 1
            counts["prov"][prov] = counts["prov"].get(prov, 0) + 1
            if typ in ("required", "recommended"):
                graph.setdefault(i, []).append(tgt)
    state = {}

    def visit(n, path):
        if state.get(n) == 2:
            return
        if state.get(n) == 1:
            err("coverage: ordering cycle among required/recommended relations: " + " -> ".join(path + [n]))
            return
        state[n] = 1
        for p in graph.get(n, []):
            visit(p, path + [n])
        state[n] = 2

    for n in list(graph):
        visit(n, [])
    return counts


def check_lectures(cov):
    per_block, members = {}, {}
    for r in cov:
        code = r["id"].split("-")[1]
        b = r.get("block")
        if b:
            members.setdefault(b, []).append(r)
        if b and r.get("lectures_in_block") is not None:
            seen = per_block.setdefault(code, {})
            if seen.setdefault(b, r["lectures_in_block"]) != r["lectures_in_block"]:
                err(f"lectures: {r['id']} disagrees with other items in block {b} on lectures_in_block")
    for code, want in LECTURES.items():
        got = sum(per_block.get(code, {}).values())
        if got != want:
            err(f"lectures: {code} blocks sum to {got}, expected {want}")
    for b, rs in members.items():
        for k, r in enumerate(rs, 1):
            if r.get("block_item") != f"{k} of {len(rs)}":
                err(f"coverage: {r['id']} block_item {r.get('block_item')!r} should be '{k} of {len(rs)}'")


# ------------------------------------------------------------------ mastery register
def parse_date(s):
    m = re.fullmatch(r"(\d{2})/(\d{2})/(\d{4})", str(s or ""))
    if not m:
        return None
    import datetime
    try:
        return datetime.date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
    except ValueError:
        return None


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
        for k in ("coverage", "mastery", "hints", "evidence", "authorised_by", "authorised_date", "history"):
            if k not in m:
                err(f"mastery: {i} missing field {k}")
        if m.get("mastery") not in MASTERY:
            err(f"mastery: {i} invalid mastery {m.get('mastery')!r}")
        if m.get("coverage") not in COVERAGE:
            err(f"mastery: {i} invalid coverage {m.get('coverage')!r}")
        hist = m.get("history", [])
        if not isinstance(hist, list):
            err(f"mastery: {i} history must be a list")
            continue
        if m.get("mastery") == "unassessed":
            if hist or m.get("evidence") or m.get("authorised_by") or m.get("authorised_date") or m.get("hints") is not None:
                err(f"mastery: {i} is unassessed but carries history, evidence, hints or authorisation")
            continue
        if not hist:
            err(f"mastery: {i} is {m.get('mastery')} but has no history of authorised decisions")
            continue
        prev_date, ic_entries = None, []
        for n, h in enumerate(hist, 1):
            where = f"mastery: {i} history[{n}]"
            if not isinstance(h, dict):
                err(f"{where} is not an object")
                continue
            lvl, hints, ev, by = h.get("level"), h.get("hints"), h.get("evidence", []), h.get("authorised_by")
            d = parse_date(h.get("date"))
            if lvl not in MASTERY or lvl == "unassessed":
                err(f"{where} has invalid level {lvl!r}")
            if hints not in HINTS:
                err(f"{where} has invalid hints {hints!r} (none, minor, substantial or unknown)")
            if d is None:
                err(f"{where} date must be DD/MM/YYYY")
            elif prev_date and d < prev_date:
                err(f"{where} is dated before the previous decision")
            if d:
                prev_date = d
            if by != ASSESSOR:
                err(f"{where} is not authorised by {ASSESSOR}")
            if not ev:
                err(f"{where} has no evidence")
            for e in ev:
                if not (ROOT / e).exists():
                    err(f"{where} evidence path {e} does not exist")
            if lvl in ("independent-competence", "durable-mastery") and hints != "none":
                err(f"{where} is {lvl} but hints are {hints!r}; {lvl} requires hints 'none'")
            if lvl == "independent-competence" and d:
                ic_entries.append((d, set(ev)))
            if lvl == "durable-mastery" and d:
                ok = any((d - d0).days >= DURABLE_INTERVAL_DAYS and set(ev) != ev0 for d0, ev0 in ic_entries)
                if not ok:
                    err(f"{where} is durable-mastery without an earlier independent-competence decision at least "
                        f"{DURABLE_INTERVAL_DAYS} days before it resting on different evidence")
        last = hist[-1] if isinstance(hist[-1], dict) else {}
        for top, key in (("mastery", "level"), ("hints", "hints"), ("evidence", "evidence"),
                         ("authorised_by", "authorised_by"), ("authorised_date", "date")):
            if m.get(top) != last.get(key):
                err(f"mastery: {i} top-level {top} does not mirror the last history entry")


# ------------------------------------------------------------------ bibliography and reading map
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
        b, c, a = e.get("bibliographic", ""), e.get("contents", ""), e.get("alignment", "")
        if b not in BIB_STATUS:
            err(f"bibliography: {i} bibliographic status {b!r} must be one of {sorted(BIB_STATUS)}")
        if c not in BIB_STATUS:
            err(f"bibliography: {i} contents status {c!r} must be one of {sorted(BIB_STATUS)}")
        if a not in ALIGN_STATUS:
            err(f"bibliography: {i} alignment status {a!r} must be one of {sorted(ALIGN_STATUS)}")
        if not e.get("availability"):
            err(f"bibliography: {i} has no availability statement")
        if "verified via" not in e:
            err(f"bibliography: {i} has no 'Verified via' line (leave it empty only when nothing was verified)")
        has_url = bool(re.search(r"https?://", e.get("verified via", "")))
        if (b != "unverified" or c != "unverified") and not has_url:
            err(f"bibliography: {i} claims some verification but has no 'Verified via' URL")
        if a in ("checked", "partial") and c == "unverified":
            err(f"bibliography: {i} claims syllabus alignment but its contents are unverified")
        if a == "checked" and c != "verified":
            err(f"bibliography: {i} alignment is 'checked' but contents are only {c!r}")


def check_readings(cov, rm, bib):
    for r in cov:
        for x in r.get("readings", []):
            if x not in rm:
                err(f"reading-map: {r['id']} cites {x}, which is not defined in curriculum/reading-map.md")
    p = ROOT / "curriculum" / "reading-map.md"
    text = p.read_text(encoding="utf-8") if p.exists() else ""
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


# ------------------------------------------------------------------ session records
def check_sessions(ids):
    d = ROOT / "progress" / "sessions"
    files = sorted(p for p in d.glob("*.md") if p.name not in ("TEMPLATE.md", "README.md")) if d.exists() else []
    for p in files:
        rel = p.relative_to(ROOT)
        if not SESSION_NAME.match(p.name):
            err(f"{rel}: session record names must look like YYYY-MM-DD-NN-slug.md")
        text = p.read_text(encoding="utf-8")
        for h in SESSION_HEADINGS:
            if h not in text:
                err(f"{rel}: missing section '{h}'")
        if "**Session:**" not in text:
            err(f"{rel}: missing the '**Session:**' header line")
        n_ex = len(re.findall(r"^### Exchange \d+", text, flags=re.M))
        if "## Exchanges" in text and n_ex == 0:
            err(f"{rel}: the Exchanges section has no '### Exchange N' entries")
        for blk in re.split(r"^### Exchange \d+", text, flags=re.M)[1:]:
            for f in EXCHANGE_FIELDS:
                if f"- {f}:" not in blk:
                    err(f"{rel}: an exchange is missing the field '{f}'")
        for i in set(re.findall(r"IA-[A-Z]{2}-(?:N\d{2}|\d{3})", text)):
            if i not in ids:
                err(f"{rel}: cites {i}, which is not a register id")
    check_session_immutability(files)
    return len(files)


def check_session_immutability(files):
    """Saved session records are append-only: the text first committed must still be the start of the file."""
    if not files or not (ROOT / ".git").exists():
        return
    for p in files:
        rel = str(p.relative_to(ROOT))
        try:
            first = subprocess.run(["git", "log", "--diff-filter=A", "--format=%H", "--", rel], cwd=ROOT,
                                   capture_output=True, text=True, check=True).stdout.split()
            if not first:
                continue            # not yet committed: nothing to compare against
            orig = subprocess.run(["git", "show", f"{first[-1]}:{rel}"], cwd=ROOT, capture_output=True,
                                  text=True, check=True).stdout
        except (OSError, subprocess.CalledProcessError):
            warn(f"{rel}: could not read git history to check immutability")
            continue
        if not p.read_text(encoding="utf-8").startswith(orig.rstrip()):
            err(f"{rel}: the committed text was altered; saved session records may only be appended to (Addenda)")


# ------------------------------------------------------------------ optional local source audit
def norm(s):
    """Normalisation shared with the generator: straight apostrophes, repaired extraction artefacts, no spaces or hyphens."""
    s = s.replace("’", "'").replace("M¨ obius", "Möbius").replace("Hˆ opital", "Hôpital")
    s = s.replace("V ector", "Vector")
    return re.sub(r"[\s\-]+", "", s)


TITLE_RE = {
    "GP": r"^GROUPS 24 lectures", "VM": r"^VECTORS AND MA TRICES 24", "NS": r"^NUMBERS AND SETS 24",
    "DE": r"^DIFFERENTIAL EQUA TIONS 24", "AN": r"^ANAL YSIS I 24", "PR": r"^PROBABILITY 24 lectures, Lent",
    "VC": r"^VECTOR CALCULUS 24", "DR": r"^DYNAMICS AND RELA TIVITY 24",
}


def alnum(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def audit_source(cov, schedules_text, show_mismatch=False):
    """Fingerprint audit: the items of each course must tile that course's Schedules text, in order."""
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
            err(f"audit: could not locate the {code} title line in the Schedules text (wrong edition or extractor?)")
            return
        starts[code] = idx[0]
    order = sorted(starts, key=starts.get)
    ends = {}
    for k, code in enumerate(order):
        lim = starts[order[k + 1]] if k + 1 < len(order) else len(stream)
        ends[code] = next(i for i in range(starts[code], lim) if stream[i].strip() == "Appropriate books")
    before = len(ERRORS)
    checked, copy_hits = 0, 0
    for code in order:
        seg = norm("\n".join(stream[starts[code] + 1:ends[code]]))
        items = [r for r in cov if r["id"].split("-")[1] == code]
        pos, prev_head = 0, None
        broke = False
        for r in items:
            guard = 0
            while guard < 8:
                guard += 1
                m = re.match(r"\[\d+\]\.?", seg[pos:])
                if m:
                    pos += m.end()
                    continue
                h = norm(r["heading"])
                if (r.get("block_item") or "").startswith("1 of ") and r["heading"] != prev_head and seg.startswith(h, pos):
                    pos += len(h)
                    prev_head = r["heading"]
                    continue
                break
            n = r["fingerprint"]["chars"]
            piece = seg[pos:pos + n]
            if hashlib.sha256(piece.encode("utf-8")).hexdigest() != r["fingerprint"]["sha256"]:
                err(f"audit: {r['id']} does not match the Schedules text at its expected position "
                    "(different edition or extractor, or the register was edited)")
                if show_mismatch:
                    print(f"  local passage for {r['id']} ({n} chars expected): {piece!r}")
                broke = True
                break
            if not r["heading"].startswith("("):
                prev_head = r["heading"]
            a_s, a_p = alnum(r["summary"]), alnum(piece)
            if len(a_s) >= COPY_RUN and any(a_s[i:i + COPY_RUN] in a_p for i in range(len(a_s) - COPY_RUN + 1)):
                copy_hits += 1
                warn(f"audit: {r['id']} summary shares a run of {COPY_RUN}+ letters (about 9 words) with its source passage")
            pos += n
            checked += 1
        if not broke:
            tail = re.sub(r"\[\d+\]\.?", "", seg[pos:])
            if tail.strip(" .,;:*∗"):
                err(f"audit: unmapped Schedules text at the end of {code}: {len(tail)} characters")
    if len(ERRORS) == before:
        print(f"audit: {checked} items matched their source passages in order with no unmapped gaps "
              f"({copy_hits} possible-copy warnings)")
    else:
        print(f"audit: {len(ERRORS) - before} problem(s) found (see below)")
    print("audit: NOTE - this is a fingerprint match, not proof that any summary is a faithful rendering of its source.")


# ------------------------------------------------------------------ optional leak scan
LEAK_RUN = 70           # consecutive letters/digits shared with a Cambridge text that are reported for review


def _alnum_with_index(s):
    out, idx = [], []
    for i, ch in enumerate(s):
        c = ch.lower()
        if c.isascii() and c.isalnum():
            out.append(c)
            idx.append(i)
    return "".join(out), idx


def leak_scan(source_texts):
    """List passages in the repository's own files that repeat 70+ letters of a local Cambridge text. For human review:
    book titles and the document title legitimately appear; syllabus sentences should not."""
    src = ""
    for t in source_texts:
        t = t.replace("\u2019", "'").replace("M\u00a8 obius", "Mobius")
        src += _alnum_with_index(t)[0]
    grams = {src[i:i + LEAK_RUN] for i in range(len(src) - LEAK_RUN + 1)}
    found = 0
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or ".git" in p.parts or p.suffix not in (".md", ".yaml", ".py"):
            continue
        text = p.read_text(encoding="utf-8")
        a, idx = _alnum_with_index(text)
        i = 0
        while i <= len(a) - LEAK_RUN:
            if a[i:i + LEAK_RUN] in grams:
                j = i + LEAK_RUN
                while j < len(a) and a[j - LEAK_RUN + 1:j + 1] in grams:
                    j += 1
                snippet = text[idx[i]:idx[min(j - 1, len(idx) - 1)] + 1].replace("\n", " ")
                warn(f"leak-scan: {p.relative_to(ROOT)} repeats {j - i} letters of Cambridge text: {snippet[:90]!r}")
                found += 1
                i = j
            else:
                i += 1
    print(f"leak-scan: {found} shared passage(s) of {LEAK_RUN}+ letters reported as warnings for review "
          "(document and book titles are expected; syllabus sentences are not)")


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--schedules-text", help="plain text of schedules.pdf (scripts/extract_pdf_text.py), for the local audit")
    ap.add_argument("--show-mismatch", action="store_true", help="with the audit: print the local passage at a mismatch")
    ap.add_argument("--guide-text", help="plain text of coursesIA.pdf; with --schedules-text, adds a copyright leak scan of the repository")
    args = ap.parse_args()

    cov = load_register(ROOT / "curriculum" / "coverage.yaml")
    mas = load_register(ROOT / "progress" / "mastery.yaml")
    ids = check_ids(cov)
    counts = check_relations(cov, ids)
    check_lectures(cov)
    check_mastery(cov, mas)
    bib = parse_entries(ROOT / "references" / "bibliography.md", "BIB-")
    rm = parse_entries(ROOT / "curriculum" / "reading-map.md", "RM-")
    check_bibliography(bib)
    check_readings(cov, rm, bib)
    check_syllabus_md({r["id"] for r in cov})
    check_links()
    n_sessions = check_sessions(ids)
    if args.schedules_text:
        audit_source(cov, pathlib.Path(args.schedules_text).read_text(encoding="utf-8"), args.show_mismatch)
        texts = [pathlib.Path(args.schedules_text).read_text(encoding="utf-8")]
        if args.guide_text:
            texts.append(pathlib.Path(args.guide_text).read_text(encoding="utf-8"))
        leak_scan(texts)
    else:
        warn("local source audit and leak scan skipped (no --schedules-text given)")

    by = {}
    for r in cov:
        c = r["id"].split("-")[1]
        by[c] = by.get(c, 0) + 1
    print("register records by course code:", ", ".join(f"{k}={v}" for k, v in sorted(by.items())))
    print("relations by type:", counts["type"], "| by provenance:", counts["prov"])
    print(f"bibliography entries: {len(bib)}; reading-map entries: {len(rm)}; mastery records: {len(mas)}; "
          f"session records: {n_sessions}")
    for w in WARNINGS:
        print("WARNING:", w)
    for e in ERRORS:
        print("ERROR:", e)
    print("LIMITS: structural validation only - not mathematical correctness, not authentication of assessment "
          "decisions, not proof that summaries are faithful to Cambridge.")
    print("RESULT:", "FAIL" if ERRORS else "PASS", f"({len(ERRORS)} errors, {len(WARNINGS)} warnings)")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
