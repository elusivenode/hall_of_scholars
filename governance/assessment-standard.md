# Assessment and mastery standard

Status: **approved by the curriculum director on 21/10/2026** (see [director-decisions.md](director-decisions.md), D-12 to D-15),
including the four levels, the 28-day interval and the hint scale. Items still marked **[PROPOSED]** are Claude Code's drafting
choices that the director has not yet addressed.

## 1. Principles

- Mastery is an **evidence-based judgement**, never a completion percentage.
- Every judgement above `unassessed` points to **actual student work** or a documented assessment.
- Only ChatGPT, acting as academic assessor in the teaching workflow, authorises a change to demonstrated mastery. Claude Code
  implements authorised changes and never infers them.
- Initial state for every syllabus item is `unassessed`. Nothing is assumed from prior schooling, prior conversations or
  general descriptions of the student's background.
- Prerequisite relationships ([curriculum/dependencies.md](../curriculum/dependencies.md)) are teaching guidance. **No rule
  requires a predecessor's mastery to be recorded before a topic is begun or assessed.** Cambridge teaches courses concurrently
  and this repository supports the same flexibility.

## 2. The four levels

| Level (`mastery` value) | Meaning | Typical evidence |
|---|---|---|
| `unassessed` | No judgement has been made. The starting state. | none |
| `familiarity` | Recognises definitions and ideas. | States or identifies definitions and results; recognises examples and non-examples. |
| `understanding` | Explains reasoning and reconstructs proofs **with guidance**. | Reconstructs a proof after a guided discussion; explains why each hypothesis is needed. |
| `independent-competence` | Constructs proofs and solves unfamiliar problems **without hints**. | A written solution to a problem not previously seen, produced without hints and judged correct and rigorous by the assessor. |
| `durable-mastery` | Applies the knowledge independently **after a meaningful interval**, including in new contexts. | Fresh independent work after the interval, on new material, ideally in a different context. |

`unassessed` is a state, not a level of attainment. Levels are ordered; a record holds the highest level currently supported by
evidence, and the assessor may lower or raise it.

## 3. What can never justify a level

A topic must **not** be marked `independent-competence` or `durable-mastery` solely because:

- it was discussed;
- the student read the relevant chapter;
- an AI supplied a correct proof;
- the student followed a worked example;
- an exercise was completed with substantial hints.

These may support `familiarity`, and in some cases `understanding`, only if the assessor records them as evidence of that level.

## 4. Durable mastery

The **normal minimum interval is 28 days** between the evidence that established `independent-competence` and the fresh
assessment that supports `durable-mastery`. **The interval is necessary but not sufficient.** The later assessment must also
require independent reasoning on genuinely new material, preferably in a different context (for example an application in
another course). The assessor may require a longer interval.

What the validator can and cannot check: it checks that a `durable-mastery` decision follows an **unbroken** earlier `independent-competence`
decision at least 28 days before it, resting on different evidence files; a later downgrade or withdrawal breaks the chain, so durable mastery
cannot rest on a decision the assessor has since lowered. It **cannot** judge whether the later work really was independent reasoning on new
material; that judgement is the assessor's alone.

## 5. Hints

Record the hint level on every piece of evidence:

- `none` - no hints at any point;
- `minor` - a pointer to a definition or a restatement of the question;
- `substantial` - a proof strategy, a key lemma, or a worked analogous example;
- `unknown` - the hint history is genuinely unavailable.

`independent-competence` and `durable-mastery` require `none`, so evidence with `unknown` hints cannot support them under this
standard. **Unknown hint history is never converted automatically into a claim of familiarity or competence**: the assessor decides
what, if anything, the available evidence supports, and records that decision as usual. Do not use `unknown` to avoid recording
hints that were in fact known.

## 6. Evidence

Evidence is a file in this repository containing:

1. the problem or prompt, with its source (for example an exact Tripos question label);
2. the student's actual work, transcribed or attached (a typed or scanned copy, not a summary);
3. the hints or assistance given, per section 5;
4. the assessor's evaluation of the argument, including errors found.

Store evidence under `studies/<course>/work/YYYY-MM-DD-<slug>.md` (the folder must be the item's own course), or under `assessments/diagnostic/`
for the diagnostic, written from [studies/EVIDENCE-TEMPLATE.md](../studies/EVIDENCE-TEMPLATE.md). The validator requires each evidence path to be
an existing, non-empty file in one of those places with the four parts (Problem, Student work, Hints given, Assessor evaluation) non-empty. The
paths go in `evidence` in `progress/mastery.yaml`. Do not reconstruct evidence from memory or from general descriptions of
earlier study. If the work was not captured, the evidence does not exist.

## 7. Authorising a change

The assessor issues an **Assessment Decision**:

```text
ASSESSMENT DECISION
Date: DD/MM/YYYY
Assessor: ChatGPT-assessor
Items: IA-XX-NNN, IA-XX-NNN
Level: familiarity | understanding | independent-competence | durable-mastery
Evidence: path/to/evidence-file.md
Hints: none | minor | substantial | unknown
Rationale: one or two sentences naming what was demonstrated and what was not
```

Claude Code then:

1. checks the decision against sections 3 to 6 and **refuses to record it** if the evidence file is missing, the hint level is
   inconsistent with the level, or an interval is required but absent;
2. appends an entry to `history` for each item in `progress/mastery.yaml` and updates the top-level fields to mirror it
   (`mastery`, `hints`, `evidence`, `authorised_by: "ChatGPT-assessor"`, `authorised_date`);
3. records the decision in the session record (as an addendum if the session record is already saved);
4. runs `python3 scripts/validate.py`.

Downgrades follow the same route: only the assessor lowers or raises a level. Earlier history entries are kept, so the record of
what was authorised, when and on what evidence is never overwritten.

**Withdrawal.** The assessor may withdraw a level altogether. This is recorded as a decision with level `unassessed` and hints null (with the rationale
file as evidence if there is one); the item returns to `unassessed` at the top level, the history is kept, and the withdrawal breaks any chain that durable
mastery would have relied on.

**Diagnostic competence before coverage.** A valid diagnostic may establish competence before a topic is marked formally covered (director decision D-25).
While an item's `coverage` is `not-started`, any level above `unassessed` must rest only on evidence under `assessments/diagnostic/`. Otherwise `coverage` and
`mastery` are independent.

## 8. Integrity of the assessment records: what validation cannot do

`scripts/validate.py` checks the **existence and structure** of evidence and authorisation records: required fields, valid levels,
hint rules, chronology (no future dates), the 28-day rule on an unbroken chain, that each evidence path is a real, non-empty file of the right kind, in the right
folder for the item's course, with the four required parts, and that the top-level fields match the latest decision. `scripts/selftest.py` tests each of these rules
with synthetic records that exist only in a temporary copy.

It **cannot** establish that:

- the student's argument is mathematically correct;
- the evidence file really contains the student's unaided work;
- an Assessment Decision genuinely came from the assessor (the label `ChatGPT-assessor` is text, not an authenticated identity);
- the 28-day work was on new material.

Those rest on the integrity of the workflow, on version control (every change is visible and attributable in git history), and on
the independent reviewer's challenge. Treat a passing validation as "the records are well formed", not as "the judgements are right".

## 9. Coverage is not mastery

`coverage` in `progress/mastery.yaml` (`not-started`, `in-progress`, `covered`) records what has been taught or read. Setting it
carries no mastery claim and never changes `mastery`. Claude Code may update `coverage` from a session record; it may not touch
`mastery` without an Assessment Decision.

## 10. Starred, non-examinable and ancillary items

Items with status `starred-not-examinable` must be lectured at Cambridge but cannot be set in the Tripos; they are tracked
separately from examinable material (D-05). `ancillary-non-examinable` items (Mechanics, Computational Projects) are retained
(D-06) as prerequisites or preparation, not Part IA examination material. All can be assessed with this standard; whether a
particular one is assessed is the director's call.
