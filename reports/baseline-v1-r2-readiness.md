# Curriculum Baseline v1 - Second Remediation (R2) Readiness Report

Prepared by Claude Code (curriculum librarian) on 22/10/2026 in response to the director's decision R2 on the independent Fable review. **The baseline is not approved. Merge into `main` has not been
authorised and has not been done (D-31).** Nothing has been taught or assessed, and **no mastery has been assigned**: all 173 mastery records are `unassessed` with empty history.

**Provenance of the instructions.** The director's R2 file summarises the finding-by-finding decisions and refers to a fuller adjudication in a conversation that Claude Code did **not** receive. Dispositions
below that rest on the R2 summary are marked **D**; dispositions where the summary does not settle the finding and the librarian chose a course are marked **L**, for the director to confirm or reverse.

## 1. Branches and commits for review

BRANCH_IDS

## 2. Disposition of every Fable finding (F-01 to F-39)

Status: **Fixed**, **Fixed in part**, **No action** (the finding is a note or an accurate observation) or **Open** (needs the director). Basis: **D** director's R2 decision, **L** librarian's choice.

| Finding | Status | Basis | What was done |
|---|---|---|---|
| F-01 IA-AN-006 drops "bounded" | Fixed | D | Summary now says "closed bounded interval" |
| F-02 IA-GP-016 adds "proof" | Fixed | D | Reads "Simple groups, and the simplicity of A_5" |
| F-03 IA-VM-002 widens the informal qualifier | Fixed | D | The summary now says the informal qualifier applies to the first part only, then lists de Moivre's theorem separately |
| F-04 "Homogeneous equations" | Fixed | D (D-20) | Neutral wording; the ambiguity is logged as unresolved in `curriculum/ambiguities.md` (A-01); IA-DE-012 has two connection links so no reading is privileged |
| F-05 IA-MC-N01 weakens "prerequisite" | Fixed | D | Restored |
| F-06 other added words | Fixed in part | L | IA-GP-005 neutralised (logged as A-03). Retained as harmless glosses: "of the extended plane" (IA-GP-003), "in a central force" (IA-DR-008), "review" and "single-variable" (IA-DE-001). Director to confirm |
| F-07 structural and notation checks pass | No action | | Recorded |
| F-08 examinable count | Fixed | D (D-28) | 159 examinable plus 2 wholly starred core-course items in the readable view, dependencies, decisions and the README-level statements; earlier reports carry correction banners |
| F-09 no Differential Equations alignment | Fixed | D | 20-row table added (161 rows now); Robinson stays an unconfirmed selection; the Groups and Differential Equations primaries are listed as open; task B7 now blocks the selection |
| F-10 Cowley IA-VM-012 cell | Fixed | D | Cell is covered (Cowley 3.6.8); the table and note are corrected |
| F-11 Tong "maximum principle" | Fixed | L | Entry now says the notes prove no interior maximum or minimum and do not use the phrase |
| F-12 Allenby print facts rest on Open Library | Fixed | L | The entry says which facts were seen directly and which rest on Open Library, and that Open Library could not be reopened |
| F-13 weak primaries | Fixed | D (D-24) | Working choices recorded; Beardon and Robinson stay unconfirmed; Groups and Differential Equations open |
| F-14 sample verification | No action | | Recorded |
| F-15 four statuses not conflated | No action | | Recorded |
| F-16 reading-map ranges agree | No action | | Now also enforced by the validator (see F-32) |
| F-17 provenance inconsistent | Fixed | D (D-21) | New provenance `cambridge-course-level` for Cambridge's course-level statements (Mechanics assumed, "vector methods", the Probability links); item-level `cambridge-stated` is empty at present; approval is a separate field |
| F-18 `required` overloaded | Fixed | D (D-22) | Type `assumed` added. I applied it to the Mechanics links and to links whose source is revision-level school knowledge (complex numbers, vector algebra): **L**, provisional |
| F-19 link targets and missing links | Fixed | D (D-23) | IA-VC-011 now requires IA-VM-012 and is connected to IA-VM-018; connections added for inertia tensor and moments of inertia, and for orthogonal groups and rotation matrices; the Lorentz link retained as `inferred-from-cambridge`. These five links are `director-approved` |
| F-20 reviewed relationships | No action | | Recorded; the section was rewritten for the new model |
| F-21 validator accepts forbidden records | Fixed | D | All eight counterexamples (a) to (h) are rejected, with the one exception the director made: competence on diagnostic evidence is accepted before a topic is covered (D-25). Evidence must be a real, non-empty file in the right folder for the item's course, from the template, with four non-empty parts; no future dates; durable mastery needs an unbroken chain |
| F-22 zero-length fingerprint | Fixed | D | Rejected in the structural check and in the audit |
| F-23 valid records wrongly rejected | Fixed | D | (a) withdrawal recorded as a decision with level `unassessed`, history kept; (b) only `required` links form the cycle check; (c) evidence compared as a set |
| F-24 session checks | Fixed in part | L | Misconception required; blank fields rejected; the four header lines checked; Student questions, Tutor explanation and Why this next added; a pasted decision with the wrong hint level is rejected; evidence files validated. **Not done:** cross-checking a pasted decision against `mastery.yaml` (declared limitation) |
| F-25 self-test coverage | Fixed | D | 80 tests: each demonstrated defect, positive cases for valid unusual records, a leak-scan test, and id-keyed mutations. A sensitivity check confirmed that 66 tests fail against a blinded validator |
| F-26 mastery all unassessed | No action | | Confirmed again |
| F-27 identical summaries | Fixed | D (D-30) | Five full-sentence summaries reworded; whole-summary identity check added (an error unless the item is one of seven bare topic names kept on an allow-list). `COPY_RUN` left at 56 letters: the director asked for identity checks, not a lower threshold |
| F-28 leak counts | No action | | Explained: the extra warnings quoted the report's own earlier output. Current result in section 5 |
| F-29 where the old text is | Fixed in part | D (D-26) | See section 7. The librarian's local scratch copies of the verbatim register were deleted; the Cambridge PDFs and their text extracts stay for audits |
| F-30 personal details in public instructions | Fixed | D (D-30) | Moved to an untracked, git-ignored `CLAUDE.local.md` |
| F-31 YAML reader and locators | Fixed | D | Duplicate keys rejected; course name, page numbers, block and reading prefixes checked against the id |
| F-32 other weak checks | Fixed in part | D | A null lecture count can no longer hide in a counted block (the Computational Projects paragraph was split); a link to a course note is rejected; the reading map's item ranges are compared with the register; an empty `Verified via` without a trailing space is accepted; the readable syllabus must show each item's current summary. **Not done:** anchors in internal links |
| F-33 limits of the audit | No action | L | Restated in the validator's documentation. It still cannot see swapped summaries or unrelated text, and the routine run does not exercise it without a local PDF; not changed, to avoid over-engineering |
| F-34 session close never pushes | Fixed | D (D-27) | Workflow step 7 requires commit and a confirmed push, and says to report a failed push |
| F-35 resume pack names `main` | Fixed | D | The pack names the authoritative branch and a stable session id and never its own commit hash; the opening message names the branch |
| F-36 what the template lacks | Fixed | D | Student questions, Tutor explanation and Why this next added |
| F-37 recovery in principle | No action | | Recorded |
| F-38 stale "not pushed" | Fixed | D | Correction banners on the earlier reports; README and resume pack updated |
| F-39 report claims accurate | No action | | Recorded |

## 3. Syllabus coverage and source-fidelity status

| Course | Examinable items | Wholly starred | Lectures |
|---|---|---|---|
| Numbers and Sets | 22 | 0 | 24 |
| Groups | 16 | 0 | 24 |
| Vectors and Matrices | 18 | 0 | 24 |
| Differential Equations | 20 | 0 | 24 |
| Analysis I | 19 | 1 (IA-AN-015) | 24 |
| Probability | 27 | 0 | 24 |
| Vector Calculus | 14 | 0 (starred spans inside IA-VC-004 and IA-VC-005) | 24 |
| Dynamics and Relativity | 23 | 1 (IA-DR-010) | 24 |
| **Core courses** | **159** | **2** (161 records) | 192 |
| Mechanics and Computational Projects (ancillary, retained, D-06) | 12 | n/a | 10 and 8 |
| Course notes (not tracked for mastery) | 4 | | |

177 register records; 173 mastery records; **all 177 identifiers are unchanged** in set and order since v1 (checked by comparison).

**Source fidelity.**
- The register holds **no Cambridge syllabus sentences**: each item has an original summary, an exact locator (document, edition, printed and PDF page, heading, paragraph, position) and a fingerprint. A leak scan of every tracked file against the Schedules and Guide text reports only document and book titles.
- The local fingerprint audit matches every item for the eight core courses (164 passages including the three core course notes) in order with **no unmapped syllabus text**, rejects zero-length fingerprints, and rejects a summary identical to its source unless the item is one of seven bare topic names kept on an allow-list.
- **This is a structural and text-matching audit. It is not proof of semantic equivalence**: it cannot tell whether a summary is faithful, and it cannot see summaries swapped between items.
- Semantic fidelity rests on the independent Fable review, which compared all 177 summaries with the rendered PDF pages 10 to 14 and judged 172 faithful; the five issues were corrected here. Notation, starred spans and qualifier tags were confirmed. All summaries stay `librarian-draft`.
- Known limitations: text extraction flattens superscripts and subscripts (the summaries write `^` and `_`); fingerprints are calibrated on `pypdf` 6.21.2; the Mechanics and Computational Projects items are not covered by the fingerprint audit.

## 4. Relationships

256 links: 157 required, 74 recommended, 10 assumed, 15 connection. By provenance: 221 librarian judgement, 19 inferred from Cambridge, 16 Cambridge course-level, none item-level. By approval: **5 director-approved, 251 provisional**.

**Approved (5):**

| Link | Type | Provenance |
|---|---|---|
| IA-VC-011 builds on IA-VM-012 | required | librarian judgement |
| IA-VC-011 and IA-VM-018 | connection | librarian judgement |
| IA-VC-014 and IA-DR-014 (inertia tensor, moments of inertia) | connection | inferred from Cambridge |
| IA-GP-012 and IA-VM-018 (orthogonal groups, rotation matrices) | connection | inferred from Cambridge |
| IA-DR-019 and IA-VM-018 (Lorentz transformations) | connection | inferred from Cambridge |

**Still provisional:** all other links, including the 8 required cross-course links and the 10 `assumed` links, which are listed in [dependencies.md](../curriculum/dependencies.md) sections 3 and 4. "Leave unreviewed
relationships provisional" has been followed: none was approved by the librarian.

## 5. Validation and regression results

VALIDATION_RESULTS

## 6. Reading selections and verification gaps

Working choices recorded from D-24; none is a claim of full verification.

| Course | Working choice | Main verification gaps |
|---|---|---|
| Numbers and Sets | Allenby (selectively), Hammack, Lebl for reals and cardinality, Davenport | Allenby section titles; Burn and Hamilton library check; IA-NS-017 (e), 018, 020 shown by no source |
| Groups | **Open.** Beardon is an unconfirmed selection | Beardon verified to chapter titles only |
| Vectors and Matrices | Cowley as the spine, Axler for the conceptual development | Cowley is the 2010 course; nine items must come from outside Axler |
| Differential Equations | **Open.** Robinson is an unconfirmed selection | Robinson verified to Part titles only; no verified reading covers most items |
| Analysis I | Lebl with the Gowers-lecture notes, provisionally | Lebl has no complex analysis; the student notes are unlicensed and student-written |
| Probability | Norris with Grimmett and Welsh | Compressed notes; Grimmett and Welsh does not show four items |
| Vector Calculus | Tong with Baxandall and Liebeck | **Baxandall and Liebeck contents unverified** |
| Dynamics and Relativity | O'Donnell, provisionally | Three items not named (dimensional analysis, parallel axis theorem, Foucault pendulum) |

Detail: [reading-map.md](../curriculum/reading-map.md), [reading-alignment.md](../curriculum/reading-alignment.md), [bibliography.md](../references/bibliography.md), [verification-tasks.md](../references/verification-tasks.md).

## 7. Clean merge-candidate history and the obsolete branch

ANCESTRY_EVIDENCE

## 8. Matters still unresolved (not described as approved)

1. **The per-finding adjudication** was not received; dispositions marked **L** need the director's confirmation (F-06, F-11, F-12, F-18's reclassification, F-24, F-29, F-32, F-33).
2. **Summaries** remain `librarian-draft`. The Fable review compared all 177 and judged 172 faithful at `93bb00f`; I have **not** marked any `reviewed`, which would be the director's call. Five were found to be issues and have been
   corrected; five more were reworded (F-27). All changed summaries need comparison with the source.
3. **Relationships:** 251 of 256 are provisional.
4. **Open interpretations:** [ambiguities.md](../curriculum/ambiguities.md) A-01 (homogeneous equations), A-02 (the Guide's Probability and Vectors and Matrices link), A-03 (groups of small order).
5. **Reading:** the Groups and Differential Equations primaries are open; Baxandall and Liebeck, Robinson and Beardon are unverified or only partly verified.
6. **Retained Git objects:** deleting the obsolete branch does not guarantee removal of cached or retained objects, and the remediation and Fable review branches still carry the earlier history until the director has them deleted too.
7. **Pushing at session close** (D-27) is now routine; the owner should confirm that standing arrangement.
8. The live session-continuity test has not been run; it needs a real session after approval.
9. Not fixed, by design: internal-link anchors; cross-checking pasted Assessment Decisions against `mastery.yaml`; the audit's blindness to swapped summaries.

## 9. Confirmation

- **No mastery has been assigned.** Every record in `progress/mastery.yaml` is `unassessed`, with empty history, no evidence and no authorisation (validated and self-tested).
- The baseline is **not approved** and **not merged**.
