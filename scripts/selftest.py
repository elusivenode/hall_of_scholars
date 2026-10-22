#!/usr/bin/env python3
"""Self-test for scripts/validate.py. Standard library only.

    python3 scripts/selftest.py
    python3 scripts/selftest.py --schedules-text path/to/schedules.txt     # also tests the local source audit

It copies the repository (without .git) to a temporary directory, applies one deliberate defect at a time and checks that
the validator reports the expected error; it also checks that some valid-but-unusual records are ACCEPTED.

Any "student" evidence, mastery decisions or session records used here are SYNTHETIC, exist only in the temporary copy, are never
written under progress/ in the repository, and are not records of any real study. Do not copy them anywhere.
"""
import argparse
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
FAILED = []


def run(tmp, *extra):
    r = subprocess.run([sys.executable, str(tmp / "scripts" / "validate.py"), *extra], capture_output=True, text=True, cwd=tmp)
    return r.stdout + r.stderr


def fresh():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="hos-selftest-"))
    shutil.copytree(ROOT, tmp / "r", ignore=shutil.ignore_patterns(".git", "__pycache__"))
    return tmp, tmp / "r"


def edit(repo, rel, fn):
    p = repo / rel
    p.write_text(fn(p.read_text(encoding="utf-8")), encoding="utf-8")


def record(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + ("" if ok else "\n      " + detail[-400:]))
    if not ok:
        FAILED.append(name)


def expect_error(name, rel, fn, needle, extra=()):
    tmp, repo = fresh()
    try:
        edit(repo, rel, fn)
        out = run(repo, *extra)
        record(name, "RESULT: FAIL" in out and needle in out, out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def expect_pass(name, setup, extra=()):
    tmp, repo = fresh()
    try:
        setup(repo)
        out = run(repo, *extra)
        record(name, "RESULT: PASS" in out, out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def sub1(a, b):
    def f(s):
        assert a in s, f"selftest mutation target not found: {a[:50]!r}"
        return s.replace(a, b, 1)
    return f


def mastery(level, hints, evidence, history):
    """Return a function that turns the first mastery record into the given synthetic state."""
    import json

    def f(s):
        top = (f'mastery: {json.dumps(level)}\n  hints: {json.dumps(hints)}\n  evidence: {json.dumps(evidence)}\n'
               f'  authorised_by: "ChatGPT-assessor"\n  authorised_date: {json.dumps(history[-1]["date"])}\n  history: {json.dumps(history)}')
        old = 'mastery: "unassessed"\n  hints: null\n  evidence: []\n  authorised_by: null\n  authorised_date: null\n  history: []'
        assert old in s
        return s.replace(old, top, 1)
    return f


def H(date, level, hints, ev):
    return {"date": date, "level": level, "hints": hints, "evidence": ev, "authorised_by": "ChatGPT-assessor"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schedules-text")
    args = ap.parse_args()

    # ---- baseline
    tmp, repo = fresh()
    out = run(repo)
    shutil.rmtree(tmp, ignore_errors=True)
    record("baseline repository validates", "RESULT: PASS" in out, out)

    # ---- register structure
    expect_error("verbatim source field is rejected", "curriculum/coverage.yaml",
                 sub1('  summary_status: "librarian-draft"', '  source: "x"\n  summary_status: "librarian-draft"'), "verbatim 'source' field")
    expect_error("malformed fingerprint", "curriculum/coverage.yaml",
                 lambda s: re.sub(r'(fingerprint: \{"chars": \d+, "sha256": ")', r'\1zz', s, count=1), "malformed fingerprint")
    expect_error("duplicate id", "curriculum/coverage.yaml", sub1('- id: "IA-GP-002"', '- id: "IA-GP-001"'), "duplicate id")
    expect_error("invalid relation type", "curriculum/coverage.yaml", sub1('"recommended", "librarian-judgement"', '"mandatory", "librarian-judgement"'), "invalid type")
    expect_error("invalid provenance", "curriculum/coverage.yaml", sub1('"librarian-judgement"]', '"guess"]'), "invalid provenance")
    expect_error("relation to a missing id", "curriculum/coverage.yaml", sub1('["IA-NS-002", "recommended"', '["IA-NS-999", "recommended"'), "does not exist")
    expect_error("ordering cycle among required links", "curriculum/coverage.yaml",
                 lambda s: re.sub(r'(- id: "IA-GP-001"(?:.|\n)*?builds_on: )\[\]', r'\1[["IA-GP-002", "required", "librarian-judgement"]]', s, count=1),
                 "ordering cycle")

    def add_mutual_connection(repo):
        edit(repo, "curriculum/coverage.yaml",
             lambda s: re.sub(r'(- id: "IA-GP-001"(?:.|\n)*?builds_on: )\[\]', r'\1[["IA-GP-002", "connection", "librarian-judgement"]]', s, count=1))
    expect_pass("a connection may point 'backwards' (no ordering constraint)", add_mutual_connection)
    expect_error("block lecture counts must agree", "curriculum/coverage.yaml", sub1("lectures_in_block: 4", "lectures_in_block: 5"), "disagrees")
    expect_error("block_item position must be right", "curriculum/coverage.yaml", sub1('block_item: "1 of 3"', 'block_item: "2 of 3"'), "block_item")
    expect_error("missing syllabus.md entry", "curriculum/syllabus.md", sub1("IA-VC-007", "IA-VC-0xx"), "does not list IA-VC-007")
    expect_error("reading id must exist", "curriculum/coverage.yaml", sub1('"RM-GP-02"', '"RM-ZZ-99"'), "not defined in curriculum/reading-map.md")

    # ---- mastery
    ev = "studies/groups/work/2026-01-01-synthetic.md"

    def with_evidence(*fns):
        def setup(repo):
            (repo / "studies/groups/work").mkdir(parents=True, exist_ok=True)
            for n in ("2026-01-01-synthetic.md", "2026-03-01-synthetic.md"):
                (repo / "studies/groups/work" / n).write_text("# synthetic test evidence\n", encoding="utf-8")
            for f in fns:
                edit(repo, "progress/mastery.yaml", f)
        return setup

    def err_with(name, f, needle):
        tmp, repo = fresh()
        try:
            with_evidence(f)(repo)
            out = run(repo)
            record(name, "RESULT: FAIL" in out and needle in out, out)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    ev2 = "studies/groups/work/2026-03-01-synthetic.md"
    err_with("mastery above unassessed needs a history", sub1('mastery: "unassessed"', 'mastery: "understanding"'), "no history")
    err_with("unassessed must carry nothing", sub1("authorised_by: null", 'authorised_by: "ChatGPT-assessor"'), "unassessed but carries")
    err_with("independent competence requires hints none",
             mastery("independent-competence", "minor", [ev], [H("01/01/2026", "independent-competence", "minor", [ev])]), "requires hints 'none'")
    err_with("independent competence cannot rest on unknown hints",
             mastery("independent-competence", "unknown", [ev], [H("01/01/2026", "independent-competence", "unknown", [ev])]), "requires hints 'none'")
    err_with("missing evidence file is caught",
             mastery("understanding", "minor", ["studies/groups/work/absent.md"], [H("01/01/2026", "understanding", "minor", ["studies/groups/work/absent.md"])]), "does not exist")
    err_with("durable mastery needs a 28 day interval",
             mastery("durable-mastery", "none", [ev2], [H("01/01/2026", "independent-competence", "none", [ev]), H("20/01/2026", "durable-mastery", "none", [ev2])]), "at least 28 days")
    err_with("durable mastery needs different evidence",
             mastery("durable-mastery", "none", [ev], [H("01/01/2026", "independent-competence", "none", [ev]), H("01/03/2026", "durable-mastery", "none", [ev])]), "different evidence")
    err_with("history must be chronological",
             mastery("understanding", "minor", [ev], [H("05/03/2026", "familiarity", "minor", [ev]), H("01/03/2026", "understanding", "minor", [ev])]), "dated before")
    err_with("top level must mirror the last history entry",
             mastery("understanding", "minor", [ev], [H("01/01/2026", "familiarity", "minor", [ev])]), "does not mirror")
    expect_pass("unknown hints may support a lower level (the assessor decides)",
                with_evidence(mastery("familiarity", "unknown", [ev], [H("01/01/2026", "familiarity", "unknown", [ev])])))
    expect_pass("durable mastery after 28 days on different evidence is structurally valid",
                with_evidence(mastery("durable-mastery", "none", [ev2],
                                      [H("01/01/2026", "independent-competence", "none", [ev]), H("01/03/2026", "durable-mastery", "none", [ev2])])))

    # ---- bibliography
    expect_error("verification claim needs a URL", "references/bibliography.md",
                 lambda s: re.sub(r"(### BIB-002.*?- Verified via: )\S+", r"\1", s, count=1, flags=re.S), "no 'Verified via' URL")
    expect_error("alignment cannot rest on unverified contents", "references/bibliography.md",
                 lambda s: re.sub(r"(### BIB-013.*?- Alignment: )not-checked", r"\1checked", s, count=1, flags=re.S), "alignment")
    expect_error("invalid status word", "references/bibliography.md", sub1("- Bibliographic: verified", "- Bibliographic: definitely"), "must be one of")
    expect_error("broken internal link", "README.md", lambda s: s + "\n[x](nope/missing.md)\n", "broken link")

    # ---- session records (synthetic, temporary only)
    good = ("# Session\n\n**Session:** 2026-01-01-01\n\n## Exchanges\n\n### Exchange 1\n- Question (exact): q\n- Student response (verbatim): r\n"
            "- Hints given: none\n- Tutor evaluation: e\n- Misconception: none\n- Item ids: IA-GP-001\n- Source references: unlisted\n\n"
            "## Unresolved misconceptions\n\nnone\n\n## Assessment decisions\n\nnone\n\n## Coverage updates\n\nnone\n\n"
            "## Next question or exercise\n\nn\n\n## Addenda (append only)\n")

    def add_session(text, name="2026-01-01-01-synthetic.md"):
        def setup(repo):
            (repo / "progress/sessions" / name).write_text(text, encoding="utf-8")
        return setup
    expect_pass("a well-formed synthetic session record is accepted", add_session(good))
    tmp, repo = fresh()
    try:
        add_session(good.replace("## Coverage updates\n\nnone\n\n", ""))(repo)
        out = run(repo)
        record("session record missing a section", "RESULT: FAIL" in out and "missing section '## Coverage updates'" in out, out)
        add_session(good.replace("- Hints given: none\n", ""))(repo)
        out = run(repo)
        record("session exchange missing a field", "RESULT: FAIL" in out and "missing the field 'Hints given'" in out, out)
        add_session(good.replace("IA-GP-001", "IA-GP-999"))(repo)
        out = run(repo)
        record("session cites an unknown item id", "RESULT: FAIL" in out and "IA-GP-999" in out, out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # ---- session immutability (needs git)
    if shutil.which("git"):
        tmp, repo = fresh()
        try:
            git = lambda *a: subprocess.run(["git", *a], cwd=repo, capture_output=True, text=True)
            git("init", "-q"); git("config", "user.email", "t@example.invalid"); git("config", "user.name", "selftest")
            add_session(good)(repo)
            git("add", "-A"); git("commit", "-q", "-m", "synthetic")
            out = run(repo)
            record("a committed session record validates", "RESULT: PASS" in out, out)
            p = repo / "progress/sessions/2026-01-01-01-synthetic.md"
            p.write_text(good + "\n### 02/01/2026 addendum\nCorrection: none needed.\n", encoding="utf-8")
            out = run(repo)
            record("appending an addendum to a committed record is allowed", "RESULT: PASS" in out, out)
            p.write_text(good.replace("- Question (exact): q", "- Question (exact): CHANGED"), encoding="utf-8")
            out = run(repo)
            record("altering committed session text is rejected", "RESULT: FAIL" in out and "may only be appended to" in out, out)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    else:
        print("SKIP  session immutability (git not found)")

    # ---- local source audit (optional)
    if args.schedules_text:
        extra = ("--schedules-text", args.schedules_text)
        expect_error("audit: a dropped item leaves unmapped text", "curriculum/coverage.yaml",
                     lambda s: re.sub(r'- id: "IA-GP-009"(?:.|\n)*?(?=\n- id: "IA-GP-010")', "", s, count=1), "audit:", extra)
        expect_error("audit: an altered fingerprint is detected", "curriculum/coverage.yaml",
                     lambda s: re.sub(r'("sha256": ")([0-9a-f])', lambda m: m.group(1) + ("0" if m.group(2) != "0" else "1"), s, count=1),
                     "does not match the Schedules text", extra)
    else:
        print("SKIP  source-audit tests (give --schedules-text to run them)")

    print()
    print("RESULT:", "ALL SELF-TESTS PASSED" if not FAILED else f"{len(FAILED)} SELF-TEST(S) FAILED: {FAILED}")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
