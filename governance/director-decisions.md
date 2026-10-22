# Curriculum director decisions

A record of decisions taken by the curriculum director (ChatGPT) and relayed to Claude Code by the student. Claude Code
records them but cannot authenticate where they came from; each entry names the document it was taken from. A decision
listed here is a decision. Nothing listed under "Not yet decided" may be described as approved.

## Decisions of 21/10/2026 (feedback and remediation directive on Baseline v1)

Source: the director's "Curriculum Baseline v1 - Curriculum Director Feedback and Remediation Directive", pasted by the student
on 21/10/2026.

| # | Question | Decision |
|---|---|---|
| D-01 | Cambridge programme | Part IA Option (a), Pure and Applied Mathematics |
| D-02 | Syllabus authority | 2026-27 Schedules |
| D-03 | Examination practice | 2025 papers accepted, with the edition differences acknowledged |
| D-04 | Syllabus granularity | The existing 161 examinable-topic records are accepted provisionally |
| D-05 | Starred material | Retained, and tracked separately from examinable material |
| D-06 | Ancillary courses | Mechanics and Computational Projects are retained |
| D-07 | Harvard discrete mathematics worksheets | Low-priority optional practice |
| D-08 | Detailed personal study plan | Deferred until after the diagnostic assessment |
| D-09 | Mastery status | All items remain `unassessed` |
| D-10 | Merge authorisation | **Not granted** |
| D-11 | Architecture | Retained; the repository is not to be rebuilt |
| D-12 | Durable mastery interval | 28 days is the normal minimum between evidence of independent competence and a fresh durable-mastery assessment. The interval is necessary but not sufficient: the later assessment must require independent reasoning on genuinely new material, preferably in a different context |
| D-13 | Hint levels | `none`, `minor`, `substantial` retained; `unknown` is permitted where historical hint information is genuinely unavailable. Unknown hint history is never converted automatically into a claim of familiarity or competence; the assessor decides what, if anything, the evidence supports |
| D-14 | Four-level model | Familiarity, understanding, independent competence, durable mastery, with `unassessed` as the initial state, are approved |
| D-15 | Assessor | ChatGPT retains exclusive responsibility for authorising mastery judgements within the agreed teaching workflow |
| D-16 | Public source representation | The public repository must not reproduce substantial Cambridge syllabus text. Items are represented by original summaries plus exact locators; the Cambridge documents stay outside the tracked repository |
| D-17 | Prerequisite model | Relationships are of three kinds (required prerequisite, recommended preparation, conceptual connection) and their provenance is recorded separately. The sequence is a teaching recommendation, not an inflexible algorithm, and demonstrated mastery of every predecessor is not required before starting a topic |
| D-18 | Harvard enrichment | Optional, never displacing the complete Cambridge Pure and Applied curriculum; prioritised towards proof construction, abstract linear algebra, group theory, rigorous analysis and the connections between structures. The pace and breadth of Math 55 are not objectives |

## Not yet decided (do not treat as approved)

- Whether the baseline is approved for merge (D-10: not granted).
- Whether the original verbatim syllabus text should be removed from the already-published git history of the pushed branch (see
  the remediation report).
- Each `librarian-draft` summary in `curriculum/coverage.yaml` and the typed relationships: all are librarian work awaiting
  review by the director and the independent reviewer. No relationship carries `director-approved` provenance.
- The choice of primary reading resources (see `curriculum/reading-map.md` and `references/verification-tasks.md`).
- The questions listed in section 9 of `reports/baseline-v1-remediation-report.md`.
