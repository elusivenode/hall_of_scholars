#!/usr/bin/env python3
"""Self-test for scripts/validate.py. Standard library only.

    python3 scripts/selftest.py
    python3 scripts/selftest.py --schedules-text path/to/schedules.txt     # also tests the local source audit

It copies the repository (without .git) to a temporary directory, applies one deliberate defect at a time and checks that the
validator reports the expected error; it also checks that valid-but-unusual records are ACCEPTED. Mutations target records by
id and field, so a later edit of the data cannot make a test silently test something else.

Any "student" evidence, mastery decisions or session records used here are SYNTHETIC, exist only in the temporary copy, are never
written under progress/ or studies/ in the repository, and are not records of any real study. Do not copy them anywhere.
"""
import argparse
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
FAILED = []
EMPTY_SHA = hashlib.sha256(b"").hexdigest()


# ------------------------------------------------------------------ plumbing
def run(repo, *extra):
    r = subprocess.run([sys.executable, str(repo / "scripts" / "validate.py"), *extra], capture_output=True, text=True, cwd=repo)
    return r.stdout + r.stderr


class Case:
    def __init__(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp(prefix="hos-selftest-"))
        self.repo = self.tmp / "r"
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def close(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def edit(self, rel, fn):
        p = self.repo / rel
        p.write_text(fn(p.read_text(encoding="utf-8")), encoding="utf-8")

    def record(self, rel, rid, fn, key="id"):
        """Apply fn(block) to the record whose id is rid in a register file."""
        def f(s):
            m = re.search(rf'(- id: "{re.escape(rid)}"\n(?:(?!- id: ).*\n?)*)', s)
            assert m, f"record {rid} not found in {rel}"
            return s[:m.start()] + fn(m.group(1)) + s[m.end():]
        self.edit(rel, f)

    def setfield(self, rel, rid, field, value):
        def fn(block):
            new = f"  {field}: {json.dumps(value, ensure_ascii=False)}"
            out, n = re.subn(rf"^  {re.escape(field)}: .*$", lambda _: new, block, count=1, flags=re.M)
            assert n == 1, f"field {field} not found in {rid}"
            return out
        self.record(rel, rid, fn)

    def getfield(self, rel, rid, field):
        s = (self.repo / rel).read_text(encoding="utf-8")
        m = re.search(rf'- id: "{re.escape(rid)}"\n(?:(?!- id: ).*\n?)*?  {re.escape(field)}: (.*)\n', s)
        return json.loads(m.group(1))

    def evidence(self, name, body=None, folder="groups"):
        d = self.repo / "studies" / folder / "work"
        d.mkdir(parents=True, exist_ok=True)
        text = body if body is not None else ("# synthetic\n\n## Problem\np\n\n## Student work\nw\n\n## Hints given\nnone\n\n## Assessor evaluation\ne\n")
        (d / name).write_text(text, encoding="utf-8")
        return f"studies/{folder}/work/{name}"

    def mastery(self, rid, level, hints, evidence, history, coverage=None):
        top = {"mastery": level, "hints": hints, "evidence": evidence, "authorised_by": "ChatGPT-assessor",
               "authorised_date": history[-1]["date"], "history": history}
        if coverage:
            top["coverage"] = coverage
        for k, v in top.items():
            self.setfield("progress/mastery.yaml", rid, k, v)


def record(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + ("" if ok else "\n      " + detail[-500:]))
    if not ok:
        FAILED.append(name)


def expect_error(name, setup, needle, extra=()):
    c = Case()
    try:
        setup(c)
        out = run(c.repo, *extra)
        record(name, "RESULT: FAIL" in out and needle in out, out)
    finally:
        c.close()


def expect_pass(name, setup, extra=()):
    c = Case()
    try:
        setup(c)
        out = run(c.repo, *extra)
        record(name, "RESULT: PASS" in out, out)
    finally:
        c.close()


def H(date, level, hints, ev):
    return {"date": date, "level": level, "hints": hints, "evidence": ev, "authorised_by": "ChatGPT-assessor"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schedules-text")
    args = ap.parse_args()
    G1 = "IA-GP-001"

    # ---------------------------------------------------------------- baseline
    c = Case()
    out = run(c.repo)
    c.close()
    record("baseline repository validates", "RESULT: PASS" in out, out)

    # ---------------------------------------------------------------- register structure
    expect_error("verbatim source field is rejected", lambda c: c.record("curriculum/coverage.yaml", G1, lambda b: b.replace("  summary_status:", '  source: "x"\n  summary_status:', 1)), "verbatim 'source' field")
    expect_error("malformed fingerprint", lambda c: c.setfield("curriculum/coverage.yaml", G1, "fingerprint", {"chars": 5, "sha256": "zz"}), "malformed fingerprint")
    expect_error("F-22: zero-length fingerprint is rejected", lambda c: c.setfield("curriculum/coverage.yaml", G1, "fingerprint", {"chars": 0, "sha256": EMPTY_SHA}), "zero-length source fingerprint")
    expect_error("duplicate id", lambda c: c.edit("curriculum/coverage.yaml", lambda s: s.replace('- id: "IA-GP-002"', '- id: "IA-GP-001"', 1)), "duplicate id")
    expect_error("F-31: duplicate key in a record", lambda c: c.record("curriculum/coverage.yaml", G1, lambda b: b.replace("  summary_status:", '  summary: "second"\n  summary_status:', 1)), "duplicate key")
    expect_error("F-31: course name must match the id", lambda c: c.setfield("curriculum/coverage.yaml", "IA-AN-001", "course", "Probability"), "does not match its id")
    expect_error("F-31: page numbers must match the course", lambda c: c.setfield("curriculum/coverage.yaml", G1, "printed_page", 99), "do not match")
    expect_error("F-31: block must belong to the course", lambda c: c.setfield("curriculum/coverage.yaml", G1, "block", "PR-B01"), "does not belong to course")
    expect_error("F-31: reading must belong to the course", lambda c: c.setfield("curriculum/coverage.yaml", G1, "readings", ["RM-PR-01"]), "does not belong to course")
    expect_error("invalid relation type", lambda c: c.setfield("curriculum/coverage.yaml", "IA-GP-002", "builds_on", [[G1, "mandatory", "librarian-judgement", "provisional"]]), "invalid type")
    expect_error("invalid provenance", lambda c: c.setfield("curriculum/coverage.yaml", "IA-GP-002", "builds_on", [[G1, "required", "guess", "provisional"]]), "invalid provenance")
    expect_error("provenance 'director-approved' is not a provenance", lambda c: c.setfield("curriculum/coverage.yaml", "IA-GP-002", "builds_on", [[G1, "required", "director-approved", "provisional"]]), "invalid provenance")
    expect_error("invalid approval", lambda c: c.setfield("curriculum/coverage.yaml", "IA-GP-002", "builds_on", [[G1, "required", "librarian-judgement", "maybe"]]), "invalid approval")
    expect_error("old three-element relation is rejected", lambda c: c.setfield("curriculum/coverage.yaml", "IA-GP-002", "builds_on", [[G1, "required", "librarian-judgement"]]), "malformed relation")
    expect_error("relation to a missing id", lambda c: c.setfield("curriculum/coverage.yaml", "IA-GP-002", "builds_on", [["IA-GP-999", "required", "librarian-judgement", "provisional"]]), "does not exist")
    expect_error("F-32: relation to a course note", lambda c: c.setfield("curriculum/coverage.yaml", "IA-GP-002", "builds_on", [["IA-NS-N01", "recommended", "librarian-judgement", "provisional"]]), "course note")
    expect_error("self relation", lambda c: c.setfield("curriculum/coverage.yaml", "IA-GP-002", "builds_on", [["IA-GP-002", "required", "librarian-judgement", "provisional"]]), "relates to itself")
    expect_error("ordering cycle among required links", lambda c: c.setfield("curriculum/coverage.yaml", G1, "builds_on", [["IA-GP-002", "required", "librarian-judgement", "provisional"]]), "ordering cycle")

    def mutual(kind):
        def setup(c):
            c.setfield("curriculum/coverage.yaml", G1, "builds_on", [["IA-GP-002", kind, "librarian-judgement", "provisional"]])
            c.setfield("curriculum/coverage.yaml", "IA-GP-002", "builds_on", [[G1, kind, "librarian-judgement", "provisional"]])
        return setup
    expect_pass("F-23: mutually recommended items are allowed", mutual("recommended"))
    expect_pass("a mutual connection is allowed", mutual("connection"))
    expect_error("mutually required items are a cycle", mutual("required"), "ordering cycle")
    expect_error("lecture counts in a block must agree", lambda c: c.setfield("curriculum/coverage.yaml", G1, "lectures_in_block", 5), "disagree")
    expect_error("F-32: a null count may not hide in a counted block", lambda c: c.setfield("curriculum/coverage.yaml", G1, "lectures_in_block", None), "mixes items")
    expect_error("block_item position must be right", lambda c: c.setfield("curriculum/coverage.yaml", G1, "block_item", "2 of 3"), "block_item")
    expect_error("F-32/divergence: syllabus.md must show the YAML summary", lambda c: c.edit("curriculum/syllabus.md", lambda s: s.replace(c.getfield("curriculum/coverage.yaml", "IA-GP-004", "summary"), "A different summary.", 1)), "shows a different summary")
    expect_error("missing syllabus.md entry", lambda c: c.edit("curriculum/syllabus.md", lambda s: s.replace("- **IA-VC-007**", "- **IA-VC-0xx**", 1)), "does not list IA-VC-007")
    expect_error("reading id must exist", lambda c: c.setfield("curriculum/coverage.yaml", G1, "readings", ["RM-GP-99"]), "not defined in curriculum/reading-map.md")
    expect_error("F-32: reading-map item ranges must match the register", lambda c: c.edit("curriculum/reading-map.md", lambda s: s.replace("- Items: IA-GP-001 to IA-GP-003", "- Items: IA-GP-001 to IA-GP-002", 1)), "'Items' range does not match")

    # ---------------------------------------------------------------- mastery (synthetic evidence in the temporary copy only)
    def with_ev(fn):
        def setup(c):
            c.ev1 = c.evidence("2026-01-01-synthetic.md")
            c.ev2 = c.evidence("2026-03-01-synthetic.md")
            fn(c)
        return setup
    M = "progress/mastery.yaml"
    expect_error("mastery above unassessed needs a history", with_ev(lambda c: c.setfield(M, G1, "mastery", "understanding")), "no history")
    expect_error("unassessed must carry nothing", with_ev(lambda c: c.setfield(M, G1, "authorised_by", "ChatGPT-assessor")), "unassessed with no history")
    expect_error("IC requires hints none", with_ev(lambda c: c.mastery(G1, "independent-competence", "minor", [c.ev1], [H("01/01/2026", "independent-competence", "minor", [c.ev1])], "covered")), "requires hints 'none'")
    expect_error("IC cannot rest on unknown hints", with_ev(lambda c: c.mastery(G1, "independent-competence", "unknown", [c.ev1], [H("01/01/2026", "independent-competence", "unknown", [c.ev1])], "covered")), "requires hints 'none'")
    expect_error("F-21(a): a directory is not evidence", with_ev(lambda c: c.mastery(G1, "understanding", "minor", ["studies/groups"], [H("01/01/2026", "understanding", "minor", ["studies/groups"])], "covered")), "not an existing file")
    expect_error("F-21(b): an empty path is not evidence", with_ev(lambda c: c.mastery(G1, "understanding", "minor", [""], [H("01/01/2026", "understanding", "minor", [""])], "covered")), "evidence path is empty")
    expect_error("F-21(c): README.md is not evidence", with_ev(lambda c: c.mastery(G1, "understanding", "minor", ["README.md"], [H("01/01/2026", "understanding", "minor", ["README.md"])], "covered")), "must be studies/")
    expect_error("F-21(d): a path outside the repository", with_ev(lambda c: c.mastery(G1, "understanding", "minor", ["../../etc/hostname"], [H("01/01/2026", "understanding", "minor", ["../../etc/hostname"])], "covered")), "inside the repository")
    expect_error("F-21(e): a future-dated decision", with_ev(lambda c: c.mastery(G1, "understanding", "minor", [c.ev1], [H("01/01/2099", "understanding", "minor", [c.ev1])], "covered")), "in the future")
    expect_error("F-21(h): evidence for another course", with_ev(lambda c: c.mastery(G1, "understanding", "minor", [c.evidence("2026-01-01-wrong.md", folder="probability")], [H("01/01/2026", "understanding", "minor", ["studies/probability/work/2026-01-01-wrong.md"])], "covered")), "belongs to another course")
    expect_error("evidence file must have its four sections", with_ev(lambda c: c.mastery(G1, "understanding", "minor", [c.evidence("2026-01-02-thin.md", "# only a title\n")], [H("01/01/2026", "understanding", "minor", ["studies/groups/work/2026-01-02-thin.md"])], "covered")), "lacks a non-empty section")
    expect_error("evidence file must not be empty", with_ev(lambda c: c.mastery(G1, "understanding", "minor", [c.evidence("2026-01-02-empty.md", "")], [H("01/01/2026", "understanding", "minor", ["studies/groups/work/2026-01-02-empty.md"])], "covered")), "is empty")
    expect_error("evidence outside the permitted folders", with_ev(lambda c: c.mastery(G1, "understanding", "minor", ["progress/sessions/TEMPLATE.md"], [H("01/01/2026", "understanding", "minor", ["progress/sessions/TEMPLATE.md"])], "covered")), "must be studies/")
    expect_error("history must be chronological", with_ev(lambda c: c.mastery(G1, "understanding", "minor", [c.ev1], [H("05/03/2026", "familiarity", "minor", [c.ev1]), H("01/03/2026", "understanding", "minor", [c.ev1])], "covered")), "dated before")
    expect_error("top level must mirror the last history entry", with_ev(lambda c: c.mastery(G1, "understanding", "minor", [c.ev1], [H("01/01/2026", "familiarity", "minor", [c.ev1])], "covered")), "does not mirror")
    expect_error("durable needs a 28 day interval", with_ev(lambda c: c.mastery(G1, "durable-mastery", "none", [c.ev2], [H("01/01/2026", "independent-competence", "none", [c.ev1]), H("20/01/2026", "durable-mastery", "none", [c.ev2])], "covered")), "at least 28 days")
    expect_error("durable needs different evidence", with_ev(lambda c: c.mastery(G1, "durable-mastery", "none", [c.ev1], [H("01/01/2026", "independent-competence", "none", [c.ev1]), H("01/03/2026", "durable-mastery", "none", [c.ev1])], "covered")), "different evidence")
    expect_error("F-21(f): durable after a later downgrade", with_ev(lambda c: c.mastery(G1, "durable-mastery", "none", [c.ev2], [H("01/01/2026", "independent-competence", "none", [c.ev1]), H("15/01/2026", "familiarity", "substantial", [c.ev1]), H("01/03/2026", "durable-mastery", "none", [c.ev2])], "covered")), "unbroken")
    expect_error("durable after a withdrawal", with_ev(lambda c: c.mastery(G1, "durable-mastery", "none", [c.ev2], [H("01/01/2026", "independent-competence", "none", [c.ev1]), H("15/01/2026", "unassessed", None, []), H("01/03/2026", "durable-mastery", "none", [c.ev2])], "covered")), "unbroken")
    expect_error("F-21(g)/director: not-started needs diagnostic evidence", with_ev(lambda c: c.mastery(G1, "familiarity", "minor", [c.ev1], [H("01/01/2026", "familiarity", "minor", [c.ev1])], "not-started")), "only diagnostic evidence")
    def diagnostic_ok(c):
        d = c.repo / "assessments" / "diagnostic"
        (d / "d1.md").write_text("# diagnostic\n\n## Problem\np\n\n## Student work\nw\n\n## Hints given\nnone\n\n## Assessor evaluation\ne\n", encoding="utf-8")
        c.mastery(G1, "independent-competence", "none", ["assessments/diagnostic/d1.md"], [H("01/01/2026", "independent-competence", "none", ["assessments/diagnostic/d1.md"])], "not-started")
    expect_pass("diagnostic competence before formal coverage is accepted", diagnostic_ok)
    expect_pass("unknown hints may support a lower level (the assessor decides)", with_ev(lambda c: c.mastery(G1, "familiarity", "unknown", [c.ev1], [H("01/01/2026", "familiarity", "unknown", [c.ev1])], "covered")))
    expect_pass("F-23: evidence listed in a different order is accepted", with_ev(lambda c: c.mastery(G1, "understanding", "minor", [c.ev2, c.ev1], [H("01/03/2026", "understanding", "minor", [c.ev1, c.ev2])], "covered")))
    expect_pass("durable after 28 days on different evidence is structurally valid", with_ev(lambda c: c.mastery(G1, "durable-mastery", "none", [c.ev2], [H("01/01/2026", "independent-competence", "none", [c.ev1]), H("01/03/2026", "durable-mastery", "none", [c.ev2])], "covered")))
    expect_pass("F-23: a withdrawal keeps history and returns to unassessed", with_ev(lambda c: c.mastery(G1, "unassessed", None, [], [H("01/01/2026", "understanding", "minor", [c.ev1]), H("15/01/2026", "unassessed", None, [])], "covered")))
    expect_error("a withdrawal may not keep evidence at top level", with_ev(lambda c: c.mastery(G1, "unassessed", None, [c.ev1], [H("01/01/2026", "understanding", "minor", [c.ev1]), H("15/01/2026", "unassessed", None, [])], "covered")), "still lists evidence")

    # ---------------------------------------------------------------- bibliography
    expect_error("verification claim needs a URL", lambda c: c.edit("references/bibliography.md", lambda s: re.sub(r"(### BIB-002.*?- Verified via: )\S+", r"\1", s, count=1, flags=re.S)), "no 'Verified via' URL")
    expect_error("alignment cannot rest on unverified contents", lambda c: c.edit("references/bibliography.md", lambda s: re.sub(r"(### BIB-013.*?- Alignment: )not-checked", r"\1checked", s, count=1, flags=re.S)), "alignment")
    expect_error("invalid status word", lambda c: c.edit("references/bibliography.md", lambda s: s.replace("- Bibliographic: verified", "- Bibliographic: definitely", 1)), "must be one of")
    expect_pass("F-32: an empty 'Verified via' with no trailing space is accepted", lambda c: c.edit("references/bibliography.md", lambda s: re.sub(r"(### BIB-013.*?- Verified via:) ?\n", r"\1\n", s, count=1, flags=re.S)))
    expect_error("broken internal link", lambda c: c.edit("README.md", lambda s: s + "\n[x](nope/missing.md)\n"), "broken link")

    # ---------------------------------------------------------------- leak scan (synthetic Cambridge text in a temporary copy)
    c = Case()
    try:
        import importlib.util
        sentence = "a synthetic sentence standing in for copyright syllabus wording that must not be repeated anywhere public"
        (c.repo / "curriculum" / "leaky.md").write_text("# leaky\n\n" + sentence + "\n", encoding="utf-8")
        spec = importlib.util.spec_from_file_location("v_selftest", c.repo / "scripts" / "validate.py")
        v = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(v)
        v.leak_scan([sentence])
        record("leak scan reports a repeated passage", any("leak-scan: curriculum/leaky.md" in w for w in v.WARNINGS), str(v.WARNINGS))
    finally:
        c.close()

    # ---------------------------------------------------------------- session records (synthetic, temporary only)
    def good(**kw):
        t = ("# Session\n\n**Session:** 2026-01-01-01\n**Topic:** synthetic\n**Curriculum identifiers:** IA-GP-001\n**Participants and record:** synthetic\n\n## Exchanges\n\n### Exchange 1\n"
             "- Question (exact): q\n- Student response (verbatim): r\n- Student questions: none\n- Hints given: none\n- Tutor explanation: none\n- Tutor evaluation: e\n"
             "- Misconception: none\n- Item ids: IA-GP-001\n- Source references: unlisted\n\n## Unresolved misconceptions\n\nnone\n\n## Assessment decisions\n\nnone\n\n"
             "## Coverage updates\n\nnone\n\n## Next question or exercise\n\n- Question (exact): n\n- Why this next: because\n\n## Addenda (append only)\n")
        for a, b in kw.items():
            t = t.replace(a.replace("_", " "), b)
        return t

    def session(text, name="2026-01-01-01-synthetic.md"):
        def setup(c):
            (c.repo / "progress/sessions" / name).write_text(text, encoding="utf-8")
        return setup
    expect_pass("a well-formed synthetic session record is accepted", session(good()))
    expect_error("session: missing section", session(good().replace("## Coverage updates\n\nnone\n\n", "")), "missing section '## Coverage updates'")
    expect_error("session: missing header line", session(good().replace("**Topic:** synthetic\n", "")), "header line '**Topic:**'")
    expect_error("F-24: session exchange must have Misconception", session(good().replace("- Misconception: none\n", "")), "missing the field 'Misconception'")
    expect_error("session exchange must have Student questions", session(good().replace("- Student questions: none\n", "")), "missing the field 'Student questions'")
    expect_error("session exchange must have Tutor explanation", session(good().replace("- Tutor explanation: none\n", "")), "missing the field 'Tutor explanation'")
    expect_error("F-24: a blank field is rejected", session(good().replace("- Question (exact): q", "- Question (exact):")), "is blank")
    expect_error("session must say why the next question", session(good().replace("- Why this next: because\n", "")), "Why this next")
    expect_error("session cites an unknown item id", session(good().replace("IA-GP-001", "IA-GP-999")), "IA-GP-999")
    expect_error("session name must be dated", session(good(), "bad-name.md"), "must look like")
    expect_error("F-24: a pasted decision with substantial hints", session(good().replace("## Assessment decisions\n\nnone\n", "## Assessment decisions\n\nASSESSMENT DECISION\nLevel: independent-competence\nHints: substantial\n")), "requires 'none'")

    # ---------------------------------------------------------------- session immutability (needs git)
    if shutil.which("git"):
        c = Case()
        try:
            git = lambda *a: subprocess.run(["git", *a], cwd=c.repo, capture_output=True, text=True)
            git("init", "-q"); git("config", "user.email", "t@example.invalid"); git("config", "user.name", "selftest")
            session(good())(c)
            git("add", "-A"); git("commit", "-q", "-m", "synthetic")
            out = run(c.repo)
            record("a committed session record validates", "RESULT: PASS" in out, out)
            p = c.repo / "progress/sessions/2026-01-01-01-synthetic.md"
            p.write_text(good() + "\n### 02/01/2026 addendum\nCorrection: none needed.\n", encoding="utf-8")
            out = run(c.repo)
            record("appending an addendum to a committed record is allowed", "RESULT: PASS" in out, out)
            p.write_text(good().replace("- Question (exact): q", "- Question (exact): CHANGED"), encoding="utf-8")
            out = run(c.repo)
            record("altering committed session text is rejected", "RESULT: FAIL" in out and "may only be appended to" in out, out)
        finally:
            c.close()
    else:
        print("SKIP  session immutability (git not found)")

    # ---------------------------------------------------------------- local source audit (optional)
    if args.schedules_text:
        extra = ("--schedules-text", args.schedules_text)

        def drop(c):
            c.edit("curriculum/coverage.yaml", lambda s: re.sub(r'- id: "IA-GP-009"\n(?:(?!- id: ).*\n?)*', "", s, count=1))
        expect_error("audit: a dropped item leaves unmapped text", drop, "audit:", extra)
        expect_error("audit: an altered fingerprint is detected", lambda c: c.setfield("curriculum/coverage.yaml", "IA-GP-004", "fingerprint", {"chars": c.getfield("curriculum/coverage.yaml", "IA-GP-004", "fingerprint")["chars"], "sha256": "0" * 64}), "does not match the Schedules text", extra)

        def invented(c):
            blk = re.search(r'(- id: "IA-AN-020"\n(?:(?!- id: ).*\n?)*)', (c.repo / "curriculum/coverage.yaml").read_text(encoding="utf-8")).group(1)
            new = blk.replace("IA-AN-020", "IA-AN-021").replace('"block_item": "1 of 1"', '"block_item": "2 of 2"')
            new = re.sub(r"  fingerprint: .*", '  fingerprint: {"chars": 0, "sha256": "' + EMPTY_SHA + '"}', new)
            new = re.sub(r'  block_item: .*', '  block_item: "6 of 6"', new)
            c.edit("curriculum/coverage.yaml", lambda s: s.replace(blk, blk + "\n" + new, 1) if blk.endswith("\n") else s.replace(blk, blk + "\n\n" + new, 1))
        expect_error("F-22: an invented item with a zero fingerprint is rejected even with the audit", invented, "zero-length source fingerprint", extra)

        def identical(c):
            c.setfield("curriculum/coverage.yaml", "IA-PR-002", "summary", "Combinatorial analysis, permutations and combinations.")
            c.edit("curriculum/syllabus.md", lambda s: re.sub(r"(- \*\*IA-PR-002\*\*: )[^\n]*", r"\1Combinatorial analysis, permutations and combinations.  ", s, count=1))
        expect_error("F-27: a summary identical to its source is rejected", identical, "identical to its source passage", extra)

        def allowed(c):
            c.setfield("curriculum/coverage.yaml", "IA-NS-003", "summary", "Union, intersection and equality of sets.")
            c.edit("curriculum/syllabus.md", lambda s: re.sub(r"(- \*\*IA-NS-003\*\*: )[^\n]*", r"\1Union, intersection and equality of sets.  ", s, count=1))
        expect_pass("F-27: a bare topic name on the allow-list may repeat the source", allowed, extra)
    else:
        print("SKIP  source-audit tests (give --schedules-text to run them)")

    print()
    print("RESULT:", "ALL SELF-TESTS PASSED" if not FAILED else f"{len(FAILED)} SELF-TEST(S) FAILED: {FAILED}")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
