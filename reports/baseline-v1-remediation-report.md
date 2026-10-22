# Curriculum Baseline v1 - Remediation Report

Prepared by Claude Code (curriculum librarian) on 21 to 22/10/2026 in response to the curriculum director's feedback and remediation directive. **The baseline is not
approved. Merge authorisation has not been granted (D-10).** Nothing has been taught, assessed or marked as mastered; all 173 mastery records remain `unassessed`.
Where this report says something is "decided" it points to [governance/director-decisions.md](../governance/director-decisions.md); anything else is a proposal.

## 1. Branch, commits and publication

| | |
|---|---|
| Branch | `remediation/baseline-v1-director-feedback`, based on `feature/curriculum-baseline-v1` at `c337c7a` so the review history is preserved |
| Remediation content commit | `fe09a422633f65097840cbd56f44280015482c66` (short `fe09a42`); a follow-up commit records this hash in the report and holds no other change |
| Earlier commits (unchanged) | `774a338`, `c337c7a` on `feature/curriculum-baseline-v1` |
| `main` | untouched at `0228a63` |
| Pushed? | **No.** The remediation branch has not been pushed, awaiting the owner's instruction. |

### Publication check (done before any change, as directed)

Checked on 21/10/2026 through the authenticated personal login and, separately, with anonymous requests:

- The repository `elusivenode/hall_of_scholars` is **PUBLIC**: not a fork, 0 forks, 0 stars, 0 pull requests; branches `main` (`0228a63`) and `feature/curriculum-baseline-v1` (`c337c7a`).
- **`main` is clean**: it holds only the one-line README (anonymous requests for `curriculum/coverage.yaml` and `curriculum/syllabus.md` on `main` return 404).
- **The pushed branch `feature/curriculum-baseline-v1` already publishes the verbatim syllabus text.** Anonymous requests for `curriculum/coverage.yaml` and `curriculum/syllabus.md` on that branch return 200.
  The text is in commits `774a338` and `c337c7a`.
- **Replacing the text on the remediation branch does not remove it from that published history.** This is the material that needs your attention; see decision Q1 in section 9. Claude Code has not deleted, force-pushed or rewritten anything.

## 2. Disposition of each directive item

| Directive | Disposition |
|---|---|
| 1. Overall assessment; retain the architecture, do not rebuild | **Done.** Architecture retained. All 177 stable identifiers are preserved (same set, same order). |
| 2. Priority 1: copyright and source representation | **Done, with a residual decision.** Verbatim statements replaced by original summaries (177), exact locators (document, edition, printed and PDF page, heading, paragraph, position) and fingerprints (length and SHA-256). Cambridge PDFs stay outside the tracked repository. Local audit supported. Leak scan added: only document and book titles remain shared with Cambridge text. **Already-published history: undecided (Q1).** Summaries are librarian drafts awaiting review (Q2). |
| 3. Priority 2: textbook selection and verification | **Done for the second pass; selection awaits director decision.** Four-status verification per resource; per-item alignment tables; working primaries proposed with gaps and outstanding tasks (sections 5 and 9). Not every reference is verified, by design. |
| 4. Priority 3: prerequisite model | **Done; awaiting approval.** Three relationship types and four provenance values, stored per link. The five flagged cross-course relationships reviewed (section 4). No link is `director-approved`. |
| 5. Priority 4: assessment governance | **Done.** Four levels, 28-day interval (necessary not sufficient), hints with `unknown`, history and structural transition rules, and an explicit statement of what validation cannot do. |
| 6. Priority 5: session continuity | **Done; live test deferred.** Template captures the exact question, verbatim response, hints, evaluation, misconception, item ids and source references; append-only records, git-checked; end-to-end test protocol written. No student interaction was fabricated. |
| 7. Harvard Math 55 enrichment | **Done.** Honours sequence and 2018 discrete worksheets kept distinct; priorities (proof construction, abstract linear algebra, group theory, rigorous analysis, connections); pace and breadth not objectives; discrete worksheets low priority (D-07). |
| 8. Confirmed curriculum decisions | **Recorded** as D-01 to D-18 in `governance/director-decisions.md`, with a separate "not yet decided" list. |
| 9. Validation and independent review readiness | **Done.** Validator strengthened; self-test suite added; review package in section 11. |
| 10. Implementation and reporting | **Done.** Remediation branch; not merged; this report. |
| 11. Governing principle | Observed: infrastructure kept simple and subordinate (standard library only, no new dependencies in the repository). |

## 3. Updated curriculum coverage counts

| Course | Items | Starred | Lectures |
|---|---|---|---|
| Numbers and Sets | 22 | 0 | 24 |
| Groups | 16 | 0 | 24 |
| Vectors and Matrices | 18 | 0 | 24 |
| Differential Equations | 20 | 0 | 24 |
| Analysis I | 20 | 1 (IA-AN-015) | 24 |
| Probability | 27 | 0 | 24 |
| Vector Calculus | 14 | 0 (starred spans inside IA-VC-004 and IA-VC-005) | 24 |
| Dynamics and Relativity | 24 | 1 (IA-DR-010) | 24 |
| **Examinable total** | **161** (accepted provisionally, D-04) | 2 | 192 |
| Mechanics and Computational Projects (ancillary, retained, D-06) | 12 | n/a | 10 and 8 |
| Course notes (not tracked) | 4 | | |

177 register records; 173 mastery records, all `unassessed`. Counts are unchanged from v1.

**Relationships:** 252 links (v1: 247 flat prerequisites). By type: 167 required, 75 recommended, 10 connection. By provenance: 219 librarian judgement, 27 inferred from Cambridge, 6 stated by Cambridge, 0 director-approved.

## 4. Prerequisite model: the five relationships reviewed

Full reasoning is in [curriculum/dependencies.md](../curriculum/dependencies.md) section 3. In brief:

- **Numbers and Sets and Groups:** two links, both recommended; no required link. v1 had made them prerequisites.
- **Groups and Vectors and Matrices:** two-way. Matrix-group items require matrices (three required links); the Vectors and Matrices item that names groups needs no group theory, so that link became a connection.
- **Differential Equations and Analysis I:** connection only; neither is required by the other.
- **Analysis I and Vector Calculus:** connection only; Vector Calculus is applied and imposes no analysis requirement.
- **Mechanics and Dynamics and Relativity:** five required links, inferred from Cambridge's course-level statement that Mechanics is assumed; "required" means assumed knowledge, to be established by the diagnostic, not by completing the ten lectures.

Only 18 of the 61 cross-course links are required (listed in dependencies.md section 4). Two v1 links were corrected (Jacobians now point to surface and volume integrals; "vector methods" now points to vector algebra).
**No rule requires a predecessor's mastery before a topic starts.**

## 5. Reference verification improvements

The second pass distinguished four statuses for every resource (bibliographic, contents, syllabus alignment, availability); see [references/bibliography.md](../references/bibliography.md) (40 entries) and
[curriculum/reading-alignment.md](../curriculum/reading-alignment.md) (141 item-by-resource rows, each marked covered, partial, not seen or unknown).

Main findings (all from sources opened on 21/10/2026):

- **Numbers and Sets.** Allenby's verified chapter titles name none of the real-number or countability items and only the number-system overview partly, so on verified evidence it needs a companion. Its print imprint is Arnold (the ebook is Butterworth-Heinemann).
  Lebl (free, verified) covers the least-upper-bound property, monotone sequences, cardinality and the uncountability of R, but not the irrationality of e, an explicit transcendental, the countable-union theorem, or a construction of R. Burn and Hamilton have only chapter titles verified.
- **Vectors and Matrices.** Axler's 4th edition is open access and was read section by section. It supports the conceptual development (vector spaces, linear maps, rank-nullity, eigenvalues, inner products, the spectral theorem, quadratic forms, determinants) but has no cross product, suffix notation, Lorentz transformations or conics and only passing Gaussian elimination. The reading map lists exactly which items must come from Cowley's notes or Beardon.
- **Analysis I.** Burkill: 1962 is the first edition and 1978 a paperback reprint; the author's preface omits Cauchy sequences and no Bolzano-Weierstrass was found; secondhand copies exist; contents were read from an unofficial scan that is deliberately not linked, so its contents status is only `partial`. Garling's section titles are login-walled and it is real-valued only. Lebl is free, verified at section level, and covers 15 of 20 items for the real case but has no complex analysis; the Gowers-lecture student notes cover all 20.
- **Probability.** Grimmett and Welsh is now verified (second edition, full contents list from the publisher's front matter) but does not show Stirling, simulation (Box-Muller, rejection), Simpson's paradox or combinatorial generating functions. Norris's 2024 notes name all 27 items; Weber's omit simulation.
- **Vector Calculus.** Tong's notes name all 14 items. Bourne and Kendall and Riley, Hobson and Bence now have verified contents. **Baxandall and Liebeck's contents could not be verified from any source**, so its alignment is unknown.
- **Dynamics and Relativity.** O'Donnell's publisher contents were compared with all 24 items: three items are not named (dimensional analysis, parallel axis theorem, Foucault pendulum, the last starred) and several are only partly named.
- **Corrections to earlier entries.** Weber's notes are stamped Lent 2014 (not 2015); O'Donnell's chapter numbers are not printed on the publisher page (chapters are now cited by title); Bourne and Kendall is on Cambridge's list (dagger, Vector Calculus); Davenport is the 8th edition with page ranges verified.

Prioritised outstanding checks, with what is usable meanwhile, are in [references/verification-tasks.md](../references/verification-tasks.md). Study is **not** delayed by them: the initial phase (Numbers and Sets, Vectors and Matrices, Groups) is Priority A.

## 6. Validation results

Run from the repository with a local copy of the Schedules and Guide:

```text
audit: 164 items matched their source passages in order with no unmapped gaps (0 possible-copy warnings)
audit: NOTE - this is a fingerprint match, not proof that any summary is a faithful rendering of its source.
leak-scan: 5 shared passage(s) of 70+ letters reported as warnings for review (document and book titles are expected; syllabus sentences are not)
register records by course code: AN=20, CP=2, DE=20, DR=26, GP=16, MC=11, NS=23, PR=27, VC=14, VM=18
relations by type: {'required': 167, 'recommended': 75, 'connection': 10} | by provenance: {'librarian-judgement': 219, 'inferred-from-cambridge': 27, 'cambridge-stated': 6}
bibliography entries: 40; reading-map entries: 45; mastery records: 173; session records: 0
WARNING: leak-scan: curriculum/coverage.yaml repeats 98 letters of Cambridge text: 'E: Schedules of Lecture Courses and Form of Examinations for the Mathematical Tripos 2026-'
WARNING: leak-scan: curriculum/syllabus.md repeats 98 letters of Cambridge text: 'e:** *Schedules of Lecture Courses and Form of Examinations for the Mathematical Tripos 20'
WARNING: leak-scan: references/bibliography.md repeats 92 letters of Cambridge text: 'K.F. Riley, M.P. Hobson and S.J. Bence, *Mathematical Methods for Physics and Engineering*'
WARNING: leak-scan: references/bibliography.md repeats 83 letters of Cambridge text: 'A.G. Hamilton, *Numbers, Sets and Axioms: The Apparatus of Mathematics*, Cambridge Univers'
WARNING: leak-scan: references/source-register.md repeats 95 letters of Cambridge text: 'Schedules of Lecture Courses and Form of Examinations for the Mathematical Tripos | **2026'
LIMITS: structural validation only - not mathematical correctness, not authentication of assessment decisions, not proof that summaries are faithful to Cambridge.
RESULT: PASS (0 errors, 5 warnings)
```

Self-test of the validator (synthetic defects, in a temporary copy only):

```text
PASS  baseline repository validates
PASS  verbatim source field is rejected
PASS  malformed fingerprint
PASS  duplicate id
PASS  invalid relation type
PASS  invalid provenance
PASS  relation to a missing id
PASS  ordering cycle among required links
PASS  a connection may point 'backwards' (no ordering constraint)
PASS  block lecture counts must agree
PASS  block_item position must be right
PASS  missing syllabus.md entry
PASS  reading id must exist
PASS  mastery above unassessed needs a history
PASS  unassessed must carry nothing
PASS  independent competence requires hints none
PASS  independent competence cannot rest on unknown hints
PASS  missing evidence file is caught
PASS  durable mastery needs a 28 day interval
PASS  durable mastery needs different evidence
PASS  history must be chronological
PASS  top level must mirror the last history entry
PASS  unknown hints may support a lower level (the assessor decides)
PASS  durable mastery after 28 days on different evidence is structurally valid
PASS  verification claim needs a URL
PASS  alignment cannot rest on unverified contents
PASS  invalid status word
PASS  broken internal link
PASS  a well-formed synthetic session record is accepted
PASS  session record missing a section
PASS  session exchange missing a field
PASS  session cites an unknown item id
PASS  a committed session record validates
PASS  appending an addendum to a committed record is allowed
PASS  altering committed session text is rejected
PASS  audit: a dropped item leaves unmapped text
PASS  audit: an altered fingerprint is detected

RESULT: ALL SELF-TESTS PASSED
```

All 177 register ids are preserved; a copyright leak scan against the Schedules and Guide text reports only the document title and book titles. All external URLs cited in the repository were rechecked (section 7).

What these results do **not** show: mathematical correctness; that any assessment decision is authentic (none exists); that any summary is a faithful rendering of its source (all are `librarian-draft`); that any reading resource is suitable beyond what its verified contents show.

## 7. External links

74 distinct URLs are cited in the repository's Markdown, YAML and Python files. On the recheck (22/10/2026) **70 returned HTTP 2xx** (following redirects). The rest, and why:

- Three Open Library records (`OL6898707M`, `OL7735892M`, `OL2730500W`) timed out on the first pass, and on a retry minutes later every Open Library record timed out; the research agents had reached Open Library earlier the same day, so this looks like an intermittent outage from this machine. Treat the edition facts that cite Open Library as verified earlier and not rechecked here.
- One Google Books page returned HTTP 429 (rate limiting).
- The Library of Congress contents record for Allenby is blocked live (HTTP 403); the repository now cites the web-archive capture the research agent actually read, which loads.

A 2xx response shows a page exists, not that its content still says what the entry records.

## 8. Uncertainties that remain

- All 177 summaries are drafts and **none has been compared with the source by anyone but the librarian.** PDF pages 10, 11 and 14 were not visually checked (pages 12 and 13 were). The ancillary courses are not covered by the fingerprint audit.
- 144 of 252 relationship links are librarian judgement; none is director-approved.
- Burkill's contents rest on a scan of uncertain copyright that is not cited; Baxandall and Liebeck's contents are unverified; Rindler, Ross and the Princeton Companion are unverified; Robinson (Differential Equations) is only verified to Part-title level.
- The free notes are older than the 2026-27 syllabus (Cowley 2010, Tong's Dynamics and Relativity 2013, Weber 2014, Allanach and Evans 2016, Chua 2014-15, Korner 2007) and several carry no licence statement or a restrictive one.
- Fingerprints were calibrated on `pypdf` 6.21.2; another extractor may differ.
- The live session-continuity test has not been run (it needs a real session).

## 9. Academic and operational decisions for the director

**Q1 (needs a decision before any push). Already-published verbatim text.** The pushed branch `feature/curriculum-baseline-v1` already exposes the Cambridge syllabus text in its history. Options: (a) leave it and accept the risk;
(b) delete the remote branch and publish only the remediation history, which means the owner deleting or force-pushing a branch (destructive and outward-facing; GitHub may retain objects reachable by commit hash for a time);
(c) ask GitHub to purge cached views after (b); (d) seek Faculty permission. Claude Code has not acted on this and recommends (b) with (c) if the exposure matters to you.

**Q2. Summary review.** Someone other than the librarian should compare each summary with the cited Schedules passage (page and heading are recorded) and set `summary_status` to `reviewed`. Suggested split: the director spot-checks, Codex reviews all.

**Q3. Relationship approval.** Review the 18 required cross-course links (dependencies.md section 4) and, where you agree, mark links `director-approved`.

**Q4. Reading choices** (evidence in the reading map and alignment tables):
1. Numbers and Sets: accept Allenby for logic and induction only, Hammack as the verified free companion, Lebl for the reals and cardinality, Davenport for number theory; and decide whether to commission a library check of Burn and Hamilton.
2. Analysis I: working primary Lebl plus the Gowers-lecture student notes for the complex material, or Burkill (Cambridge dagger, access risk, omits Bolzano-Weierstrass), or Garling.
3. Probability: working primary Norris's notes, Grimmett and Welsh as the companion book.
4. Vector Calculus: Tong primary; Baxandall and Liebeck as the companion once its contents are verified (a photo of the contents pages and the index entries listed in verification-tasks.md B5 would settle it).
5. Dynamics and Relativity: keep O'Donnell provisionally, filling three unnamed items from Tong's notes.
6. Vectors and Matrices: Cowley as the spine with Axler for the conceptual development, and the nine items that must come from outside Axler.

**Q5. Licences.** Several free notes are unlicensed or restrictive (Cowley "not to be redistributed"; Allanach and Evans "not to be quoted"; Chua and Korner unlicensed). They are linked, never copied. Confirm that linking is acceptable.

**Q6. Starred material.** D-05 says to retain starred material and track it separately: it is tracked via `status: starred-not-examinable`. Say whether a separate register or report view is wanted. The two starred spans inside otherwise examinable items remain recorded as `starred_part`.

**Q7. Princeton Companion.** The brief calls it "...to Pure Mathematics"; sources give "The Princeton Companion to Mathematics". The student offered to supply the title and contents pages.

**Q8. Live continuity test.** To be run after approval with a real session; confirm who runs it and where the result is recorded.

None of these is described as approved.

## 10. Files changed

Modified and created relative to `feature/curriculum-baseline-v1` (git diff --stat; the register files are regenerated, so their line counts are large):

```text
CLAUDE.md                                 |   26 +-
README.md                                 |   50 +-
assessments/tripos-papers/index.md        |   11 +-
curriculum/coverage.yaml                  | 2714 +++++++++++++++++++----------
curriculum/dependencies.md                |  223 +--
curriculum/enrichment.md                  |   26 +-
curriculum/reading-alignment.md           |  206 +++
curriculum/reading-map.md                 |  228 +--
curriculum/syllabus.md                    |  690 ++++----
governance/agent-workflow.md              |   23 +-
governance/assessment-standard.md         |  123 +-
governance/director-decisions.md          |   41 +
governance/session-continuity-test.md     |   47 +
governance/teaching-charter.md            |    3 +-
progress/current-session.md               |   53 +-
progress/mastery.yaml                     |  372 +++-
progress/sessions/README.md               |   21 +
progress/sessions/TEMPLATE.md             |   64 +-
references/bibliography.md                |  531 ++++--
references/source-register.md             |  142 +-
references/verification-tasks.md          |   34 +
reports/baseline-v1-remediation-report.md |  226 +++
reports/baseline-v1-review-report.md      |    6 +
scripts/selftest.py                       |  239 +++
scripts/validate.py                       |  425 ++++-
25 files changed, 4566 insertions(+), 1958 deletions(-)
```

Created: `curriculum/reading-alignment.md`, `governance/director-decisions.md`, `governance/session-continuity-test.md`, `progress/sessions/README.md`, `references/verification-tasks.md`, `reports/baseline-v1-remediation-report.md`, `scripts/selftest.py`. Modified: the register and its readable view, the bibliography and reading map, the dependencies, enrichment and source-register documents, the three governance documents, the validator, the session template and resume pack, the Tripos index, `README.md`, `CLAUDE.md`, and a banner on the historical v1 report.

## 11. Instructions for the independent Codex review

Work on a branch `review/baseline-v1-r1-<date>` from the remediation branch, or in `reviews/`. **Do not edit `curriculum/`, `progress/`, `governance/`, `references/` or `scripts/`.** Write findings to `reviews/baseline-v1-r1-codex-review.md`, each with the item id or file, the Cambridge page, and your evidence. Codex needs the Cambridge PDFs on its own machine (not stored here): download `schedules.pdf` and `coursesIA.pdf` from the URLs in `references/source-register.md` and confirm their SHA-256.

1. **Syllabus completeness and semantic fidelity.** For each of the eight courses, read the Schedules page cited by each item and judge whether the `summary` is faithful: nothing dropped, nothing added, no change of scope. Pay particular attention to the `qualifiers` tags (statement only, informal, proof sketch, proof given, brief, revision) and to any summary that merges or splits a source sentence. Run `python3 scripts/validate.py --schedules-text <text>` (extract the text with `scripts/extract_pdf_text.py`); remember a pass is a fingerprint match and does **not** show semantic equivalence. Mark reviewed summaries by listing their ids in your findings (do not edit `summary_status` yourself).
2. **Mathematical notation.** Superscripts and subscripts are flattened in the extracted text and written as `^` and `_` in the summaries. Compare PDF pages 10, 11 and 14 (not visually checked) and pages 12 and 13 against the summaries; check the two starred spans (IA-VC-004, IA-VC-005) and the starred items IA-AN-015 and IA-DR-010.
3. **Reading references.** For every bibliography entry, open the URLs under `Verified via` and confirm what `Seen` claims; confirm that nothing under `Not seen` is relied on in the reading map; re-check the Axler, Baxandall and Liebeck, Grimmett and Welsh, Norris, Tong and O'Donnell alignment rows against the actual contents. Verify the four statuses are not conflated. Re-check the Allenby verdict.
4. **Prerequisite classification.** Challenge the type and provenance of links, especially the 18 required cross-course links, the 6 stated by Cambridge (check each against the Guide or Schedules sentence), and the five reviewed relationships. Look for links that impose an ordering Cambridge does not, and for missing links.
5. **Assessment-record integrity.** Read `governance/assessment-standard.md`; confirm `progress/mastery.yaml` has only `unassessed`; run `python3 scripts/selftest.py` and review whether the self-tests cover the stated rules; try to construct a mastery record the validator wrongly accepts.
6. **Copyright-sensitive material.** Run `python3 scripts/validate.py --schedules-text <schedules text> --guide-text <guide text>` and inspect the leak-scan warnings (titles are expected, syllabus sentences are not). Search the repository for other reproduced Cambridge or textbook text, and for any tracked PDF. Note the already-published history (section 1) and say whether you can find the old text anywhere other than the pushed branch.
7. **Validator limitations and maintainability.** Review `scripts/validate.py` and `scripts/selftest.py`: the restricted YAML reader, the normalisation shared with the generator, the extractor-sensitivity of fingerprints, and any check that is missing or too weak.
8. **Long-term session continuity.** Read the template, the session README, the end-of-session routine and `governance/session-continuity-test.md`. Say whether a fresh conversation could recover the exact context from the repository alone, and whether anything the director listed (question, response, hints, evaluation, misconception, next step, ids, sources) is not captured. Do not fabricate a session to test it.

Report anything you could not check and why.
