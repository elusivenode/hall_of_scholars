#!/usr/bin/env python3
"""Validate the curriculum and progress registers.

Standard library only. Run from anywhere:

    python3 scripts/validate.py
    python3 scripts/validate.py --schedules-text path/to/schedules.txt [--guide-text path/to/guide.txt]

WHAT THIS DOES AND DOES NOT ESTABLISH
  It checks structure: unique and well-formed ids, required fields, no duplicate keys, locators consistent with each id,
  valid references between registers, typed relationships without ordering cycles, lecture counts, mastery-record rules
  (evidence files, authorisation, hint level, history, withdrawal and the 28-day interval), bibliography status fields,
  session-record structure, the readable syllabus against the register, and internal links.
  It does NOT establish mathematical correctness, it cannot authenticate that an assessment decision really came from the
  assessor, and it cannot tell whether a summary is a faithful rendering of the Cambridge source.
  The optional source audit uses a local copy of the Cambridge Schedules (NOT stored in this repository). Each register item
  carries the length and SHA-256 of its normalised source passage; the audit checks that those passages tile the Schedules text
  in order with no unmapped syllabus text, and that no summary is identical to its source passage. A pass means the register
  was built from that edition of the document. It is NOT proof of semantic equivalence between a summary and its source: that
  is an academic judgement. It cannot see summaries that were swapped between items or replaced by unrelated text.

The Schedules text comes from scripts/extract_pdf_text.py (needs the third-party package pypdf). The fingerprints were
calibrated on pypdf 6.21.2 output; another extractor may differ in spacing, ligatures or accents (use --show-mismatch).

Exit status is 0 when every check passes and 1 otherwise.
"""
import argparse
import datetime
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
REL_TYPES = {"required", "assumed", "recommended", "connection"}
PROVENANCE = {"cambridge-stated", "cambridge-course-level", "inferred-from-cambridge", "librarian-judgement"}
APPROVAL = {"provisional", "director-approved"}
QUALIFIERS = {"statement-only", "informal-treatment", "informal-proof", "proof-sketch", "proof-given", "brief", "revision"}
SUMMARY_STATUS = {"librarian-draft", "reviewed"}
HINTS = {"none", "minor", "substantial", "unknown"}
BIB_STATUS = {"verified", "partial", "unverified"}
ALIGN_STATUS = {"checked", "partial", "not-checked"}
# code -> (course name in the register, Schedules PDF page, studies folder for evidence)
CODES = {
    "NS": ("Numbers and Sets", 11, "numbers-and-sets"), "GP": ("Groups", 10, "groups"),
    "VM": ("Vectors and Matrices", 10, "vectors-and-matrices"), "DE": ("Differential Equations", 11, "differential-equations"),
    "AN": ("Analysis I", 12, "analysis-i"), "PR": ("Probability", 12, "probability"),
    "VC": ("Vector Calculus", 13, "vector-calculus"), "DR": ("Dynamics and Relativity", 13, "dynamics-and-relativity"),
    "MC": ("Mechanics (non-examinable)", 14, "dynamics-and-relativity"),
    "CP": ("Computational Projects (non-examinable in Part IA)", 14, None),
}
LECTURES = {"GP": 24, "VM": 24, "NS": 24, "DE": 24, "AN": 24, "PR": 24, "VC": 24, "DR": 24, "MC": 10, "CP": 8}
# Items whose source is a bare topic name, so an identical summary is unavoidable (director: keep necessary short terminology).
ALLOW_IDENTICAL = {"IA-NS-003", "IA-AN-005", "IA-AN-020", "IA-PR-013", "IA-DR-003", "IA-DR-018", "IA-VC-002"}
EMPTY_SHA = hashlib.sha256(b"").hexdigest()
ASSESSOR = "ChatGPT-assessor"
DURABLE_INTERVAL_DAYS = 28
COPY_RUN = 56          # letters (about 9 words) of shared text that trigger the possible-copying warning
LEAK_RUN = 70
REQUIRED_COV = ("id", "course", "heading", "summary", "summary_status", "qualifiers", "source_doc", "printed_page", "pdf_page",
                "block", "block_item", "lectures_in_block", "status", "builds_on", "readings", "fingerprint")
EVIDENCE_PARTS = ("## Problem", "## Student work", "## Hints given", "## Assessor evaluation")
STUDY_EVIDENCE = re.compile(r"^studies/([a-z-]+)/work/\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.md$")
DIAG_EVIDENCE = re.compile(r"^assessments/diagnostic/[A-Za-z0-9._-]+\.md$")
SESSION_NAME = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{2}-[a-z0-9-]+\.md$")
SESSION_HEADERS = ("**Session:**", "**Topic:**", "**Curriculum identifiers:**", "**Participants and record:**")
SESSION_HEADINGS = ("## Exchanges", "## Unresolved misconceptions", "## Assessment decisions", "## Coverage updates",
                    "## Next question or exercise", "## Addenda")
EXCHANGE_FIELDS = ("Question (exact)", "Student response (verbatim)", "Student questions", "Hints given", "Tutor explanation",
                   "Tutor evaluation", "Misconception", "Item ids", "Source references")


def err(msg):
    ERRORS.append(msg)


def warn(msg):
    WARNINGS.append(msg)


# ------------------------------------------------------------------ the restricted YAML subset
def load_register(path):
    """Parse '- key: value' records whose values are JSON (see the header of coverage.yaml). Duplicate keys are errors."""
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
        key = m.group(2)
        if key in cur:
            err(f"{path.name}:{n}: duplicate key {key!r} in record {cur.get('id', '?')}")
        try:
            cur[key] = json.loads(m.group(3))
        except json.JSONDecodeError as e:
            err(f"{path.name}:{n}: value is not valid JSON ({e.msg})")
    return records


# ------------------------------------------------------------------ syllabus register
def check_ids(cov):
    seen = set()
    for r in cov:
        i = r.get("id", "")
        m = re.fullmatch(r"IA-([A-Z]{2})-(N\d{2}|\d{3})", i)
        if not m:
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
        elif fp["chars"] < 1 or fp["sha256"] == EMPTY_SHA:
            err(f"coverage: {i} has a zero-length source fingerprint (every item must tie to a real source passage)")
        if "source" in r:
            err(f"coverage: {i} carries a verbatim 'source' field; the public register must not reproduce Cambridge text")
        if not isinstance(r.get("printed_page"), int) or not isinstance(r.get("pdf_page"), int):
            err(f"coverage: {i} needs integer printed_page and pdf_page")
        if m and m.group(1) in CODES:                       # locators must agree with the id's course
            code = m.group(1)
            name, page, _ = CODES[code]
            if r.get("course") != name:
                err(f"coverage: {i} course {r.get('course')!r} does not match its id (expected {name!r})")
            if r.get("pdf_page") != page or r.get("printed_page") != page - 2:
                err(f"coverage: {i} pages (printed {r.get('printed_page')}, PDF {r.get('pdf_page')}) do not match "
                    f"the {code} course pages {page - 2}/{page}")
            if r.get("block") is not None and not str(r["block"]).startswith(code + "-B"):
                err(f"coverage: {i} block {r.get('block')!r} does not belong to course {code}")
            for x in r.get("readings", []):
                if not str(x).startswith(f"RM-{code}-"):
                    err(f"coverage: {i} reading {x!r} does not belong to course {code}")
        elif m:
            err(f"coverage: {i} has an unknown course code {m.group(1)!r}")
    return seen


def check_relations(cov, ids):
    graph = {}
    counts = {"type": {}, "prov": {}, "approval": {}}
    status = {r["id"]: r.get("status") for r in cov}
    for r in cov:
        i = r["id"]
        edges = r.get("builds_on", [])
        if not isinstance(edges, list):
            err(f"coverage: {i} builds_on must be a list")
            continue
        seen = set()
        for e in edges:
            if not (isinstance(e, list) and len(e) == 4):
                err(f"coverage: {i} has a malformed relation {e!r} (want [id, type, provenance, approval])")
                continue
            tgt, typ, prov, appr = e
            if tgt not in ids:
                err(f"coverage: {i} relation to {tgt} - that id does not exist")
            elif status.get(tgt) == "course-note":
                err(f"coverage: {i} relates to {tgt}, which is a course note and not a teachable item")
            if tgt == i:
                err(f"coverage: {i} relates to itself")
            if tgt in seen:
                err(f"coverage: {i} lists {tgt} more than once")
            seen.add(tgt)
            if typ not in REL_TYPES:
                err(f"coverage: {i} -> {tgt} has invalid type {typ!r}")
            if prov not in PROVENANCE:
                err(f"coverage: {i} -> {tgt} has invalid provenance {prov!r}")
            if appr not in APPROVAL:
                err(f"coverage: {i} -> {tgt} has invalid approval {appr!r}")
            counts["type"][typ] = counts["type"].get(typ, 0) + 1
            counts["prov"][prov] = counts["prov"].get(prov, 0) + 1
            counts["approval"][appr] = counts["approval"].get(appr, 0) + 1
            if typ == "required":                      # only 'required' links impose an order (recommended links may be mutual)
                graph.setdefault(i, []).append(tgt)
    state = {}

    def visit(n, path):
        if state.get(n) == 2:
            return
        if state.get(n) == 1:
            err("coverage: ordering cycle among required links: " + " -> ".join(path + [n]))
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
        b = r.get("block")
        if b:
            members.setdefault(b, []).append(r)
    for b, rs in members.items():
        vals = [r.get("lectures_in_block") for r in rs]
        code = rs[0]["id"].split("-")[1]
        if any(v is None for v in vals) and any(v is not None for v in vals):
            err(f"lectures: block {b} mixes items with and without a lecture count")
        elif len(set(vals)) > 1:
            err(f"lectures: items in block {b} disagree on lectures_in_block {sorted(set(map(str, vals)))}")
        elif vals[0] is not None:
            per_block.setdefault(code, {})[b] = vals[0]
        for k, r in enumerate(rs, 1):
            if r.get("block_item") != f"{k} of {len(rs)}":
                err(f"coverage: {r['id']} block_item {r.get('block_item')!r} should be '{k} of {len(rs)}'")
    for code, want in LECTURES.items():
        got = sum(per_block.get(code, {}).values())
        if got != want:
            err(f"lectures: {code} blocks sum to {got}, expected {want}")


# ------------------------------------------------------------------ mastery register
def parse_date(s):
    m = re.fullmatch(r"(\d{2})/(\d{2})/(\d{4})", str(s or ""))
    if not m:
        return None
    try:
        return datetime.date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
    except ValueError:
        return None


def check_evidence(code, e, where):
    """An evidence path must be a real, non-empty student-work file in the right place, with the four required parts."""
    if not isinstance(e, str) or not e.strip():
        err(f"{where} evidence path is empty")
        return
    if e.startswith("/") or ".." in pathlib.PurePosixPath(e).parts:
        err(f"{where} evidence path {e!r} must be a relative path inside the repository")
        return
    p = (ROOT / e).resolve()
    try:
        p.relative_to(ROOT.resolve())
    except ValueError:
        err(f"{where} evidence path {e!r} points outside the repository")
        return
    if not p.is_file():
        err(f"{where} evidence path {e!r} is not an existing file")
        return
    m = STUDY_EVIDENCE.match(e)
    if m:
        folder = CODES.get(code, (None, None, None))[2]
        if folder is not None and m.group(1) != folder:
            err(f"{where} evidence {e!r} belongs to another course (expected studies/{folder}/work/)")
    elif not DIAG_EVIDENCE.match(e):
        err(f"{where} evidence {e!r} must be studies/<course>/work/YYYY-MM-DD-<slug>.md or assessments/diagnostic/<file>.md")
        return
    body = p.read_text(encoding="utf-8")
    if not body.strip():
        err(f"{where} evidence file {e!r} is empty")
        return
    for part in EVIDENCE_PARTS:
        pat = re.search(rf"^{re.escape(part)}[ \t]*\n(.*?)(?=^## |\Z)", body, flags=re.M | re.S)
        if not pat or not pat.group(1).strip():
            err(f"{where} evidence file {e!r} lacks a non-empty section '{part}'")
    if (ROOT / ".git").exists():
        r = subprocess.run(["git", "ls-files", "--error-unmatch", e], cwd=ROOT, capture_output=True, text=True)
        if r.returncode != 0:
            warn(f"{where} evidence file {e!r} is not tracked by git yet (commit it with the decision)")


def check_mastery(cov, mas):
    topic = {r["id"]: r for r in cov if r["status"] != "course-note"}
    mids = [m.get("id") for m in mas]
    if len(mids) != len(set(mids)):
        err("mastery: duplicate ids")
    for i in set(topic) - set(mids):
        err(f"mastery: {i} has no state record")
    for i in set(mids) - set(topic):
        err(f"mastery: {i} is not a syllabus item (or is a course note)")
    today = datetime.date.today()
    for m in mas:
        i = m.get("id")
        code = str(i).split("-")[1] if i else ""
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
        if not hist:
            if m.get("mastery") != "unassessed":
                err(f"mastery: {i} is {m.get('mastery')} but has no history of authorised decisions")
            elif m.get("evidence") or m.get("authorised_by") or m.get("authorised_date") or m.get("hints") is not None:
                err(f"mastery: {i} is unassessed with no history but carries evidence, hints or authorisation")
            continue
        prev_date = None
        entries = []                                   # (date, level, evidence set) for the durable rule
        for n, h in enumerate(hist, 1):
            where = f"mastery: {i} history[{n}]"
            if not isinstance(h, dict):
                err(f"{where} is not an object")
                continue
            lvl, hints, ev, by = h.get("level"), h.get("hints"), h.get("evidence", []), h.get("authorised_by")
            d = parse_date(h.get("date"))
            if lvl not in MASTERY:
                err(f"{where} has invalid level {lvl!r}")
            if d is None:
                err(f"{where} date must be DD/MM/YYYY")
            else:
                if prev_date and d < prev_date:
                    err(f"{where} is dated before the previous decision")
                if d > today:
                    err(f"{where} is dated in the future ({h.get('date')})")
                prev_date = d
            if by != ASSESSOR:
                err(f"{where} is not authorised by {ASSESSOR}")
            if lvl == "unassessed":                    # a withdrawal: the assessor removes a level without deleting history
                if hints is not None:
                    err(f"{where} is a withdrawal (level unassessed) and must have hints null")
                for e in ev:
                    check_evidence(code, e, where)
            else:
                if hints not in HINTS:
                    err(f"{where} has invalid hints {hints!r} (none, minor, substantial or unknown)")
                if not ev:
                    err(f"{where} has no evidence")
                for e in ev:
                    check_evidence(code, e, where)
                if lvl in ("independent-competence", "durable-mastery") and hints != "none":
                    err(f"{where} is {lvl} but hints are {hints!r}; {lvl} requires hints 'none'")
            if lvl == "durable-mastery" and d:
                run = []                                # the unbroken run of IC/durable decisions just before this one
                for e2 in reversed(entries):
                    if e2[1] in ("independent-competence", "durable-mastery"):
                        run.append(e2)
                    else:
                        break
                ok = any(e2[1] == "independent-competence" and e2[0] and (d - e2[0]).days >= DURABLE_INTERVAL_DAYS
                         and e2[2] != set(ev) for e2 in run)
                if not ok:
                    err(f"{where} is durable-mastery without an unbroken, earlier independent-competence decision at least "
                        f"{DURABLE_INTERVAL_DAYS} days before it resting on different evidence (a later downgrade or withdrawal breaks it)")
            entries.append((d, lvl, set(ev) if isinstance(ev, list) else set()))
        last = hist[-1] if isinstance(hist[-1], dict) else {}
        want = {"mastery": last.get("level"), "hints": last.get("hints"), "authorised_by": last.get("authorised_by"),
                "authorised_date": last.get("date")}
        for top, val in want.items():
            if m.get(top) != val:
                err(f"mastery: {i} top-level {top} does not mirror the last history entry")
        last_ev = last.get("evidence", [])
        if last.get("level") == "unassessed":
            if m.get("evidence"):
                err(f"mastery: {i} is unassessed after a withdrawal but still lists evidence")
        elif set(m.get("evidence") or []) != set(last_ev or []):
            err(f"mastery: {i} top-level evidence does not mirror the last history entry")
        if m.get("coverage") == "not-started" and m.get("mastery") != "unassessed":
            if not all(str(e).startswith("assessments/diagnostic/") for e in (m.get("evidence") or [])):
                err(f"mastery: {i} is {m.get('mastery')} while coverage is not-started; only diagnostic evidence "
                    "(assessments/diagnostic/) may establish competence before a topic is covered")


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
        m = re.match(r"^- ([A-Za-z ]+):[ ]?(.*)$", line)
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


def expand_range(text):
    m = re.fullmatch(r"\s*(IA-[A-Z]{2}-(\d{3}))(?: to (IA-[A-Z]{2}-(\d{3})))?\s*", text or "")
    if not m:
        return None
    code = m.group(1)[3:5]
    lo = int(m.group(2))
    hi = int(m.group(4)) if m.group(4) else lo
    return {f"IA-{code}-{n:03d}" for n in range(lo, hi + 1)}


def check_readings(cov, rm, bib):
    topic_readings = {}
    for r in cov:
        for x in r.get("readings", []):
            topic_readings.setdefault(x, set()).add(r["id"])
            if x not in rm:
                err(f"reading-map: {r['id']} cites {x}, which is not defined in curriculum/reading-map.md")
    for x, e in rm.items():                             # the reading map's item ranges must agree with the register
        want = expand_range(e.get("items"))
        if want is None:
            err(f"reading-map: {x} has an unreadable 'Items' line {e.get('items')!r}")
        elif want != topic_readings.get(x, set()):
            err(f"reading-map: {x} 'Items' range does not match the register items that cite it")
    p = ROOT / "curriculum" / "reading-map.md"
    text = p.read_text(encoding="utf-8") if p.exists() else ""
    for b in set(re.findall(r"\bBIB-\d{3}\b", text)):
        if b not in bib:
            err(f"reading-map: cites {b}, which is not defined in references/bibliography.md")


def check_syllabus_md(cov):
    """The readable view must show every item's current summary (the YAML is authoritative)."""
    p = ROOT / "curriculum" / "syllabus.md"
    lines = p.read_text(encoding="utf-8").splitlines() if p.exists() else []
    by_id = {}
    for ln in lines:
        m = re.match(r"^- \*\*(IA-[A-Z]{2}-(?:N\d{2}|\d{3}))\*\*", ln)
        if m:
            by_id[m.group(1)] = ln
    for r in cov:
        ln = by_id.get(r["id"])
        if ln is None:
            err(f"syllabus.md does not list {r['id']}")
        elif str(r.get("summary", "")) not in ln:
            err(f"syllabus.md shows a different summary for {r['id']} than coverage.yaml (the YAML is authoritative; regenerate the view)")


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
        for h in SESSION_HEADERS:
            if not re.search(rf"^{re.escape(h)}[ \t]*\S", text, flags=re.M):
                err(f"{rel}: missing or blank header line '{h}'")
        for h in SESSION_HEADINGS:
            if h not in text:
                err(f"{rel}: missing section '{h}'")
        if "Why this next:" not in text:
            err(f"{rel}: the next-question section must say 'Why this next:' (the pedagogical reason)")
        n_ex = len(re.findall(r"^### Exchange \d+", text, flags=re.M))
        if "## Exchanges" in text and n_ex == 0:
            err(f"{rel}: the Exchanges section has no '### Exchange N' entries")
        for blk in re.split(r"^### Exchange \d+", text, flags=re.M)[1:]:
            blk = re.split(r"^## ", blk, flags=re.M)[0]
            for f in EXCHANGE_FIELDS:
                m = re.search(rf"^- {re.escape(f)}:(.*?)(?=^- [A-Z]|\Z)", blk, flags=re.M | re.S)
                if not m:
                    err(f"{rel}: an exchange is missing the field '{f}'")
                elif not m.group(1).strip():
                    err(f"{rel}: the field '{f}' is blank; write 'none' or 'not captured' instead")
        for blk in re.findall(r"ASSESSMENT DECISION(.*?)(?=\n\n|\Z)", text, flags=re.S):
            lvl = re.search(r"^Level:[ \t]*(\S+)", blk, flags=re.M)
            hnt = re.search(r"^Hints:[ \t]*(\S+)", blk, flags=re.M)
            if lvl and hnt and lvl.group(1) in ("independent-competence", "durable-mastery") and hnt.group(1) != "none":
                err(f"{rel}: an Assessment Decision gives {lvl.group(1)} with hints {hnt.group(1)!r}; that level requires 'none'")
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
    checked, copy_hits, identical = 0, 0, 0
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
            if n < 1 or hashlib.sha256(piece.encode("utf-8")).hexdigest() != r["fingerprint"]["sha256"]:
                err(f"audit: {r['id']} does not match the Schedules text at its expected position "
                    "(different edition or extractor, or the register was edited)")
                if show_mismatch:
                    print(f"  local passage for {r['id']} ({n} chars expected): {piece!r}")
                broke = True
                break
            if not r["heading"].startswith("("):
                prev_head = r["heading"]
            a_s, a_p = alnum(r["summary"]), alnum(piece)
            if a_s == a_p:
                identical += 1
                if r["id"] not in ALLOW_IDENTICAL:
                    err(f"audit: the summary of {r['id']} is identical to its source passage; reword it "
                        "(only bare topic names listed in ALLOW_IDENTICAL may repeat the source)")
            elif len(a_s) >= COPY_RUN and any(a_s[i:i + COPY_RUN] in a_p for i in range(len(a_s) - COPY_RUN + 1)):
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
              f"({identical} identical bare topic names, all allowed; {copy_hits} possible-copy warnings)")
    else:
        print(f"audit: {len(ERRORS) - before} problem(s) found (see below)")
    print("audit: NOTE - this is a fingerprint match, not proof that any summary is a faithful rendering of its source.")


# ------------------------------------------------------------------ optional leak scan
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
        t = t.replace("’", "'").replace("M¨ obius", "Mobius")
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
    check_syllabus_md(cov)
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
    print("relations by type:", counts["type"], "| by provenance:", counts["prov"], "| by approval:", counts["approval"])
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
