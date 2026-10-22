# Current session - resume pack

**State: no study session has taken place.** Curriculum Baseline v1 is awaiting the curriculum director's final decision; merge authorisation has not been granted. No diagnostic assessment
has been run and no mastery has been assessed.

- **Authoritative branch:** `candidate/baseline-v1-clean` until the director authorises the merge into `main`; after that, `main`. Always read the files from that branch (the default
  branch, `main`, holds only a one-line README until the merge).
- **Last session id:** none (no session has taken place). When a session is recorded, this line gives its `YYYY-MM-DD-NN` identifier; the record is `progress/sessions/<id>-<slug>.md`.
- This file never states its own commit hash. To check that you have the latest, compare the newest file in `progress/sessions/` with the session id above.

This file is rewritten at the end of every session from the checkpoint (see [governance/agent-workflow.md](../governance/agent-workflow.md)). The full record of each session is saved first,
unchanged, in [progress/sessions/](sessions/README.md), so overwriting this file loses nothing.

## How to resume (read in this order)

1. [README.md](../README.md) - what this repository is and who does what.
2. [governance/teaching-charter.md](../governance/teaching-charter.md) and [governance/assessment-standard.md](../governance/assessment-standard.md).
3. [governance/director-decisions.md](../governance/director-decisions.md) - what the director has decided and what is still open.
4. This file.
5. [progress/mastery.yaml](mastery.yaml) for state, [curriculum/syllabus.md](../curriculum/syllabus.md) for item ids and summaries.
6. The most recent file in `progress/sessions/` (none yet).

## Last session

Every field below is copied from the saved session record. All are "none" because no session has happened.

- Session record: none
- Date and topic: none
- Item ids and source references (reading-map and bibliography ids, or Tripos question labels): none
- Exact question posed: none
- Student's actual response or argument (verbatim): none
- Student questions: none
- Hints given, with levels: none
- Tutor explanation (what the student has already been told): none
- Tutor's evaluation: none
- Unresolved misconceptions: none recorded
- Assessment decisions: none
- Coverage updates: none

## Exact next step

Awaiting the director's final decision on the baseline ([reports/baseline-v1-r2-readiness.md](../reports/baseline-v1-r2-readiness.md)). After approval, the next step is the diagnostic assessment,
which ChatGPT designs and runs; its materials and the student's responses go under [assessments/diagnostic/](../assessments/diagnostic/README.md). The detailed personal study plan follows from it (D-08).

## Suggested opening message for a new ChatGPT conversation

> I am studying the Cambridge Mathematical Tripos Part IA using the repository at https://github.com/elusivenode/hall_of_scholars. **Use the branch named under "Authoritative branch" in
> `progress/current-session.md` (currently `candidate/baseline-v1-clean`; after the merge, `main`), not the default branch.** Please act as curriculum director, Socratic tutor and academic
> assessor as set out in `governance/teaching-charter.md` and `governance/assessment-standard.md`, and respect `governance/director-decisions.md`. Read `progress/current-session.md` and resume from
> "Exact next step". When you resume a session, first state back to me, from the saved record, the exact question last posed, my response, my questions, what you had explained, the hints given,
> your evaluation and the next question with the reason for it, so I can confirm nothing has been lost. Do not mark anything as mastered without evidence, and issue Assessment Decisions only in the
> format in `governance/assessment-standard.md` section 7. At the end of the session, give me the checkpoint to commit and push.
