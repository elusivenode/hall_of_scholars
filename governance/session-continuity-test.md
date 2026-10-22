# Session continuity: end-to-end test protocol

Purpose: show that a new ChatGPT conversation can recover the exact academic context of an earlier session from the repository
alone. **The live test has not been run.** It is conducted after the curriculum director approves the baseline.

**Do not fabricate a student interaction to make the test pass.** No example session, exchange or student response exists in this
repository and none may be invented. Where the validator is tested, it uses synthetic records built in a temporary directory by
`scripts/selftest.py`; those are never stored under `progress/` and are not student records.

## Protocol

1. **Teach.** In a ChatGPT conversation, the tutor and the student complete a short real teaching interaction on one or two
   syllabus items, with at least one question put to the student and answered by them.
2. **Record.** Immediately afterwards, ChatGPT writes the checkpoint using [TEMPLATE.md](../progress/sessions/TEMPLATE.md), copying
   the exact question, the student's verbatim response, each hint (with level), the tutor's evaluation, any misconception, the item
   ids, the source references and the exact next question. Claude Code saves it as `progress/sessions/YYYY-MM-DD-NN-<slug>.md`.
3. **Refresh the resume pack.** Claude Code rewrites `progress/current-session.md` from the checkpoint and runs
   `python3 scripts/validate.py` (it must pass, including the session-structure and immutability checks).
4. **Commit.** Commit the session record and the resume pack together, so the repository state is a recoverable checkpoint.
5. **Restart.** Open a fresh ChatGPT conversation with no memory of step 1. Give it only the repository URL and the opening message
   in `progress/current-session.md`.
6. **Recover.** Ask the new conversation the checklist below, without prompting it with the answers, and compare each answer with
   the committed record.

## Recovery checklist (acceptance criteria)

The test passes only if the new conversation reproduces, from the repository, all of:

| # | It must state | Compared with |
|---|---|---|
| 1 | The exact question last posed to the student | "Question (exact)" in the session record |
| 2 | The student's actual response or argument | "Student response (verbatim)" |
| 3 | Each hint given and its level | "Hints given" |
| 4 | The tutor's evaluation | "Tutor evaluation" |
| 5 | Any unresolved misconception | "Unresolved misconceptions" |
| 6 | The syllabus ids and what they mean | `curriculum/coverage.yaml`, `curriculum/syllabus.md` |
| 7 | The source reference for the exercise | "Source references" and `curriculum/reading-map.md` |
| 8 | The exact next question or exercise | "Next question or exercise" |
| 9 | That no mastery has been recorded without an Assessment Decision | `progress/mastery.yaml` |

Record the result (pass or fail per row, and any paraphrase that lost precision) in a file under `reviews/` or `reports/`. A failure
is a defect in the template or the resume pack to be fixed, not a reason to adjust the checklist.

## What this test does not show

It shows that context can be recovered, not that the tutoring or the assessment was good. Mathematical correctness and assessment
quality remain the assessor's and the independent reviewer's concern.
