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
| D-04 | Syllabus granularity | The existing core-course topic records are accepted provisionally: **159 examinable items plus 2 wholly starred items (161 in all)**, corrected from "161 examinable" in R2 (D-28) |
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

## Decisions of 22/10/2026 (Fable review adjudication and second remediation, "R2")

Source: the director's "Curriculum Director Decision R2", received as the file `hall-of-scholars-curriculum-director-r2.md` on 22/10/2026. The file summarises the director's finding-by-finding decisions on
the independent review and refers to a fuller adjudication in a separate conversation that Claude Code has **not** seen; where the summary does not settle a finding, the readiness report says so.

| # | Question | Decision |
|---|---|---|
| D-19 | Independent reviewer | The Fable review is accepted as sufficient for this baseline. A further Codex review is not mandatory |
| D-20 | "Homogeneous equations" (IA-DE-012; Fable F-04) | Do not silently equate it with equidimensional equations; record the interpretation as unresolved until Cambridge teaching material clarifies it ([ambiguities.md](../curriculum/ambiguities.md)) |
| D-21 | Provenance (F-17) | Distinguish explicit course-level Cambridge statements from inferred item-level edges; provenance is separate from director approval |
| D-22 | Relationship types (F-18) | Introduce `assumed` for prior knowledge that can be established by diagnostic; retain `required` for mathematically necessary dependencies |
| D-23 | Connections (F-19) | IA-VC-011 needs IA-VM-012; IA-VM-018 is a conceptual connection; add connections between inertia tensors and moments of inertia, and between orthogonal groups and rotation matrices; retain the Lorentz link with appropriate provenance |
| D-24 | Working reading choices | Analysis I: Lebl with the Gowers-lecture notes, provisionally. Probability: Norris with Grimmett and Welsh. Vector Calculus: Tong with Baxandall and Liebeck (contents not yet verified). Dynamics and Relativity: O'Donnell provisionally. Numbers and Sets: Allenby selectively, Hammack for proofs, Lebl for reals and cardinality, Davenport for number theory. Robinson and Beardon stay as unconfirmed primary selections; the Groups and Differential Equations primary selections remain **open** |
| D-25 | Diagnostic and coverage | A valid diagnostic may establish competence before a topic is marked formally covered. No mastery judgement is authorised in this remediation |
| D-26 | Publication | Prepare a clean merge candidate from `main` that does not inherit the commits reproducing substantial Cambridge text; verify ancestry and content; then the obsolete remote branch `feature/curriculum-baseline-v1` may be deleted. Do not delete the remediation or Fable review branches yet. Deletion does not guarantee removal of cached or otherwise retained Git objects |
| D-27 | Session close | Commit and push the checkpoint successfully; report failures. The resume pack identifies the authoritative branch and a stable session identifier, and does not embed its own commit hash |
| D-28 | Counts | 159 examinable items plus 2 wholly starred core-course items |
| D-29 | Wording | Correct IA-AN-006, IA-GP-016, IA-VM-002 and IA-MC-N01; restore neutral wording for IA-DE-012 |
| D-30 | Public text | Reword the five summaries identical to a full Cambridge sentence; retain necessary short mathematical terminology; add whole-summary identity checks; keep personal machine and employer details out of the public agent instructions |
| D-31 | Merge | **Not authorised.** The baseline is not approved |

## Not yet decided (do not treat as approved)

- Whether the baseline is approved for merge (D-10: not granted).
- Whether any further step is wanted beyond deleting the obsolete remote branch, given that deletion does not guarantee removal of retained Git objects and that the remediation and Fable review branches
  still carry the earlier history until they too are removed.
- Each `librarian-draft` summary in `curriculum/coverage.yaml`: all are librarian work awaiting comparison with the source by the director or the independent reviewer.
- The relationships other than the five listed in [dependencies.md](../curriculum/dependencies.md) section 3, which are provisional.
- The unresolved interpretations in [ambiguities.md](../curriculum/ambiguities.md).
- The primary reading selections beyond the working choices in D-24, and the Groups and Differential Equations primaries (open).
- The questions listed in `reports/baseline-v1-r2-readiness.md`.
