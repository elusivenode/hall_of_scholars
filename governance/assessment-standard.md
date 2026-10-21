# Assessment and mastery standard

Status: **proposed in Baseline v1, awaiting curriculum-director approval.** Items marked
**[PROPOSED]** are Claude Code's drafting choices, not academic decisions.

## 1. Principles

- Mastery is an **evidence-based judgement**, never a completion percentage.
- Every judgement above `unassessed` points to **actual student work** or a documented assessment.
- Only ChatGPT, acting as academic assessor in the teaching workflow, can authorise a change to
  demonstrated mastery. Claude Code implements authorised changes and never infers them.
- Initial state for every syllabus item is `unassessed`. Nothing is assumed from prior schooling,
  prior conversations or general descriptions of the student's background.

## 2. The four levels

| Level (`mastery` value) | Meaning | Typical evidence |
|---|---|---|
| `unassessed` | No judgement has been made. This is the starting state. | none |
| `familiarity` | Recognises definitions and ideas. | Correctly states or identifies definitions and results; recognises examples and non-examples. |
| `understanding` | Explains reasoning and reconstructs proofs **with guidance**. | Reconstructs a proof after a guided discussion; explains why each hypothesis is needed. |
| `independent-competence` | Constructs proofs and solves unfamiliar problems **without hints**. | A written solution to a problem not previously seen, produced without hints, judged correct and rigorous by the assessor. |
| `durable-mastery` | Applies the knowledge independently **after a meaningful interval**, including in new contexts. | Fresh independent work on the item after the interval, in a context that differs from earlier practice. |

`unassessed` is a state, not a level of attainment. Levels are ordered; a record holds the
highest level currently supported by evidence.

## 3. What can never justify a level

A topic must **not** be marked `independent-competence` or `durable-mastery` solely because:

- it was discussed;
- the student read the relevant chapter;
- an AI supplied a correct proof;
- the student followed a worked example;
- an exercise was completed with substantial hints.

These may support `familiarity`, and in some cases `understanding`, but only if the assessor
records them as evidence of that level.

## 4. Meaningful interval for durable mastery **[PROPOSED]**

Durable mastery requires fresh independent work at least **28 days** after the evidence that
established `independent-competence`, on a problem that is new to the student, ideally in a
different context (for example an application in another course). The assessor may require longer.
The director should confirm or amend the 28-day default.

## 5. Hints **[PROPOSED]**

Record hint use on every piece of evidence as one of:

- `none` - no hints at any point;
- `minor` - a pointer to a definition or a restatement of the question;
- `substantial` - a proof strategy, a key lemma, or a worked analogous example.

`independent-competence` and `durable-mastery` require `none`. `understanding` may rest on
`minor` or `substantial`. If hint use is unknown, the evidence supports `familiarity` at most.

## 6. Evidence

Evidence is a file in this repository (or a stable reference to one) containing:

1. the problem or prompt, with its source (for example an exact Tripos question number);
2. the student's actual work, transcribed or attached (a typed or scanned copy, not a summary);
3. the hints or assistance given, per section 5;
4. the assessor's evaluation of the argument, including errors found.

Store evidence under `studies/<course>/work/YYYY-MM-DD-<slug>.md`, or under
`assessments/diagnostic/` for the diagnostic. The exact paths go in the `evidence` list of the
relevant record in `progress/mastery.yaml`.

Do not reconstruct evidence from memory or from general descriptions of earlier study. If the work
was not captured, the evidence does not exist.

## 7. Authorising a change

The assessor issues an **Assessment Decision** in this form (in the teaching conversation, to be
pasted into the repository by the student or by Claude Code on request):

```text
ASSESSMENT DECISION
Date: DD/MM/YYYY
Assessor: ChatGPT-assessor
Items: IA-XX-NNN, IA-XX-NNN
Level: familiarity | understanding | independent-competence | durable-mastery
Evidence: path/to/evidence-file.md
Hints: none | minor | substantial
Rationale: one or two sentences naming what was demonstrated and what was not
```

Claude Code then:

1. checks the decision against sections 3 to 6, and **refuses to record it** if the evidence file is
   missing, the hint level is inconsistent with the level, or an interval is required but absent;
2. updates the matching records in `progress/mastery.yaml` (`mastery`, `evidence`,
   `authorised_by: "ChatGPT-assessor"`, `authorised_date`);
3. appends the decision to the session record;
4. runs `python3 scripts/validate.py`.

Downgrades follow the same route: only the assessor can lower or raise a level, and the old
evidence stays in the version history.

## 8. Coverage is not mastery

`coverage` in `progress/mastery.yaml` (`not-started`, `in-progress`, `covered`) records what has been
taught or read. Setting it carries no mastery claim and never changes `mastery`. Claude Code may
update `coverage` from a session record; it may not touch `mastery` without an Assessment Decision.

## 9. Non-examinable and ancillary items

Items with status `starred-not-examinable` must be lectured at Cambridge but cannot be set in the
Tripos. `ancillary-non-examinable` items (Mechanics, Computational Projects) are prerequisites or
preparation, not Part IA examination material. All of them can be assessed with the same standard.
Whether the student should be assessed on them is the curriculum director's call.
