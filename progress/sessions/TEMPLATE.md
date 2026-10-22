# Session checkpoint - TEMPLATE

Copy this file to `progress/sessions/YYYY-MM-DD-NN-<slug>.md` at the end of a study session, fill every field, then **commit and push, and confirm the push succeeded** (report a failure).
Write "none" or "unknown" rather than leaving a field blank or guessing: the validator rejects a blank field. **Do not invent or reconstruct anything**: if the exact question
or the student's exact response was not captured, write "not captured" and say why.

A saved record is historical evidence and is **append-only**. Never edit text that has been committed. Corrections go under "Addenda" as a dated entry that says what is being
corrected and why; the original text stays. `python3 scripts/validate.py` checks the required sections and fields, the item ids, and (using git) that committed text has not been altered.

---

**Session:** YYYY-MM-DD-NN (the stable session identifier; DD/MM/YYYY; start and end time if known)
**Topic:** one line
**Curriculum identifiers:** IA-XX-NNN, IA-XX-NNN (from `curriculum/coverage.yaml`)
**Participants and record:** who took part; where the full conversation is kept (a link or "not retained")

## Exchanges

Add one `### Exchange N` block per question or exercise put to the student, in order. Keep the text exact.

### Exchange 1
- Question (exact): the question or exercise as posed, word for word
- Student response (verbatim): the student's actual answer or argument, unedited (use a fenced block; if it was handwritten, give the path to the scan or transcription under `studies/<course>/work/`)
- Student questions: every question the student asked during this exchange, word for word, or "none"
- Hints given: each hint, in order, with its level (`none`, `minor`, `substantial`) and when it was given; or "none"; or "unknown" if the history is genuinely unavailable
- Tutor explanation: what the tutor explained, as opposed to asked (definitions given, results stated, examples worked), so that a new conversation knows what the student has already been told; or "none"
- Tutor evaluation: the tutor's assessment of the argument as given, including any errors found and any gaps left open
- Misconception: the specific misunderstanding revealed, or "none"
- Item ids: IA-XX-NNN, IA-XX-NNN
- Source references: the resource and section (BIB and RM ids from the reading map), or the Tripos paper and question label, that the exercise came from; "unlisted" if not in the bibliography

### Exchange 2
- Question (exact):
- Student response (verbatim):
- Student questions:
- Hints given:
- Tutor explanation:
- Tutor evaluation:
- Misconception:
- Item ids:
- Source references:

## Unresolved misconceptions

- Each misconception still open at the end of the session, the item ids affected, and which exchange showed it. These feed `progress/weaknesses.md`. "none" if none.

## Assessment decisions

- Paste each Assessment Decision issued in the session, in the format in `governance/assessment-standard.md` section 7, or write "none". Do not write a decision here that the assessor did not issue.

## Coverage updates

- Item ids and the new `coverage` value (`in-progress` or `covered`), or "none". Coverage is not mastery.

## Next question or exercise

- Question (exact): the exact first thing to do next session, word for word, so that a fresh conversation can begin immediately
- Item ids: IA-XX-NNN
- Source reference: the resource and section, or Tripos question label
- Hints already given that must not be repeated: or "none"
- Why this next: the pedagogical reason for choosing it

## Addenda (append only)
