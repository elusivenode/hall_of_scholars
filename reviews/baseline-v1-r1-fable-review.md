# Independent review of Curriculum Baseline v1 (remediation branch)

> **Note on this copy.** This is the copy filed on the clean merge-candidate branch. Two short quotations of Cambridge text in the reviewer's findings F-01 and F-17 were replaced by paraphrase so that the public repository holds no Cambridge sentences. Nothing else is changed. The original, unaltered, is on branch `review/baseline-v1-r1-fable-2026-10-22`.

Reviewer: independent (Fable), 22/10/2026. Repository: /home/hamish/en_repos/hall_of_scholars, branch
`remediation/baseline-v1-director-feedback` at `93bb00f` (content commit `fe09a42`). Read-only review; nothing in the
repository was changed. Working copies and downloads are under
/tmp/claude-1000/-home-hamish/01021460-55c6-49fe-829b-d5cd3b764399/scratchpad/fable_work/.

Source check: `schedules.pdf` SHA-256 `5eedbdd4...8acf4` and `coursesIA.pdf` SHA-256 `f3fa103b...2adc` match
references/source-register.md (SRC-01, SRC-02). All five Part IA pages (PDF 10 to 14) were rendered with PyMuPDF and read
as images, not only as the pypdf extraction.

## 1. Verdict

Not yet ready for the director's approval, but close: the architecture, locators, fingerprints and governance text are
sound, and 172 of 177 summaries are faithful. Five things should be fixed or decided first.

1. The validator's assessment-record checks are weaker than the standard and the report claim. It accepts an evidence
   path that is a directory, an empty string, a path outside the repository or any file at all (README.md); it accepts
   decisions dated in the future; and it grants durable mastery on an independent-competence decision that was later
   downgraded. It also accepts an invented syllabus item carrying a zero-length fingerprint, and reports "no unmapped
   gaps".
2. Differential Equations has no reading-alignment table at all (the "141 rows" are the other seven courses) and its
   proposed primary (Robinson) is verified only to Part-title level. The report does not say so.
3. IA-AN-006 drops "bounded" from "closed bounded interval", which changes the theorem.
4. Twelve summaries are letter-for-letter identical to the Cambridge sentence (five are full sentences); the copy check
   cannot see runs shorter than 56 letters, so "original summaries (177)" is overstated.
5. Continuity: the end-of-session routine commits but never pushes, and the resume-pack opening message sends ChatGPT to
   the repository's default branch (`main`), which holds a one-line README. Also, the report's "not pushed" is now false:
   `origin/remediation/baseline-v1-director-feedback` exists at `93bb00f`.

## 2. Findings

Severity: blocker / major / minor / note. "Page" is the Schedules PDF page.

### Task 1 and 2: syllabus fidelity, notation, starred spans

F-01 (major) IA-AN-006, page 12. Source: the theorem that a continuous function on a closed and bounded interval is bounded and reaches its bounds. Summary: "A continuous function on a closed interval is bounded and achieves its upper and lower bounds." The
word "bounded" is dropped; a closed unbounded interval such as [0, infinity) is a counterexample. Fix: "closed bounded
interval".

F-02 (minor) IA-GP-016, page 10. Source: simple groups; simplicity of A5. Summary adds "including a proof that A_5 is
simple". The source does not say "proof"; CLAUDE.md rule 4 forbids silently expanding a requirement. Fix: drop "a proof
that" or record the interpretation.

F-03 (minor) IA-VM-002, page 10. Source: informal treatment of complex logarithm, n-th roots and complex powers; then a
separate sentence, de Moivre's theorem. Summary places de Moivre's theorem inside the informal treatment ("Informal
treatment of ... and de Moivre's theorem"). The qualifier's scope is widened. Fix: separate the two clauses.

F-04 (minor) IA-DE-012, page 11. Source: "Homogeneous equations." (two words). Summary: "Homogeneous (equidimensional)
equations." The reading is probably what Cambridge means, but it is an interpretation and is recorded nowhere in
reports/ (grep for "equidimensional" in reports/ and dependencies.md finds nothing). Fix: record it as an ambiguity for
the director, as rule 4 requires.

F-05 (minor) IA-MC-N01, page 14. The Schedules say the Mechanics material "is prerequisite for" Dynamics and Relativity;
the course note says Dynamics and Relativity "builds on them", which is weaker. Fix: keep "prerequisite".

F-06 (note) IA-GP-005 adds "Classification of" (source: groups of small order); IA-GP-003 adds "of the extended plane";
IA-DR-008 adds "in a central force"; IA-DE-001 adds "review" and "single-variable" without a `revision` tag (the Guide
does call it revision, so this is defensible). None changes scope materially.

F-07 (note) Structural checks all pass against the PDF: every block's lecture count, every printed and PDF page, the
sub-headings under which VM-011, VM-012, VM-017 and VM-018 sit, the block positions, and the course-note placement.
Notation: R^3, R^n, C^n, delta_ij, epsilon_ijk, S_n, A_n, A_5, 3 x 3, n x n, 2 x 2, square root of 2, O and o, R^n,
f(x+ct)+g(x-ct), log n!, nabla^2 ("the Laplacian"), u(theta), (1+1) and (3+1) dimensions, 4-vectors all match the
rendered pages. Starred spans: on page 13 the asterisks enclose exactly "and general orthogonal curvilinear" in both the
gradient sentence and the div/curl sentence (IA-VC-004 and IA-VC-005, `starred_part` correct); on page 12 the whole
sentence on direct proof of differentiability of a power series is starred (IA-AN-015); on page 13 the Foucault pendulum
sentence is starred (IA-DR-010). Pages 10, 11 and 14, which the report says were not visually checked, were checked here
and agree with the extraction (see section 4). Qualifier tags (8 statement-only, 4 proof-given, 4 informal-treatment, 4
brief, 3 revision, 1 proof-sketch, 1 informal-proof) are each supported by the source wording.

F-08 (note) Report section 3 calls the 161 course items "examinable"; two of them (IA-AN-015, IA-DR-010) are
`starred-not-examinable`, so the examinable count is 159.

### Task 3: reading references

F-09 (major) curriculum/reading-alignment.md has no table for Differential Equations: the 20 IA-DE items appear in no
row (script check: "examinable ids not in alignment" lists IA-DE-001 to IA-DE-020). The report's "141 item-by-resource
rows" is 161 minus 20 and section 5 of the report does not mention the gap. The proposed primary, BIB-011 Robinson, has
Contents `partial` (Part titles only; confirmed on the Cambridge Core page, which shows Parts I to VI and Appendices A
to C but no chapter titles) yet is the "Primary" in all five RM-DE entries. Fix: say plainly that Differential
Equations has no verified reading; add the (empty) table or a statement; mark verification-tasks B7 as blocking the
reading choice, not merely "Priority B".

F-10 (minor) curriculum/reading-alignment.md, Vectors and Matrices, IA-VM-012 against Cowley is `P` with the note that
the isotropic / symmetric trace-free / antisymmetric decomposition "is not named as a section". Cowley's notes have
section 3.6.8 "Decomposition of a Square Matrix into Isotropic, Symmetric Trace-Free and Anti-symmetric Parts" (p. 71 of
the PDF opened from the cited URL). The cell should be `C`; the "Items with no C in any column shown: IA-VM-012" line
is then wrong.

F-11 (minor) references/bibliography.md BIB-019 Tong says the body text covers "the maximum principle". The PDF never
uses that phrase; page 107 proves that a harmonic function has no interior maximum or minimum. The substance is there,
the name is not; say so, since the alignment code is about whether a topic is named.

F-12 (minor) BIB-001 Allenby: the print ISBN 0340676531, the Arnold imprint and "x + 274 pages" are cited to an Open
Library record that timed out on every attempt here (as it did for the librarian on the recheck). The Elsevier page
(opened) gives only the ebook ISBN 9780080928777 and Butterworth-Heinemann 1997; the LOC archive capture (opened) gives
the chapter titles exactly as recorded. The print facts are therefore verified by one source that nobody can currently
reopen. Not an error, but the entry should say which facts rest on Open Library.

F-13 (minor) Reliance on unverified contents in the reading map: BIB-018 Baxandall and Liebeck (Contents `unverified`)
is named as companion in RM-VC-01, RM-VC-02 and RM-VC-04, each time flagged "contents unverified"; BIB-023 Rindler
(Bibliographic `unverified`) is listed under RM-DR-05 "Also"; BIB-004 Beardon (chapter titles only) is the Primary for
all six RM-GP entries, two of them with "placement not visible from chapter titles". The flags are honest, but a
"Primary" with no verified section-level contents is a weak primary; the Groups and Differential Equations choices
should be put to the director as open, which the report's Q4 list does not do for Groups.

F-14 (note) Sample verification of `Seen` claims, all by opening the cited URL on 22/10/2026 (24 of 40 entries; the
eight Faculty example-sheet entries, Chua's other notes, Gowers's pages, Matthews, Ross, Rindler and the Princeton
Companion were not opened):
Lebl (version 6.3, 15/05/2026, 312 pages, dual CC licence, sections as listed, exercise 1.4.9 on transcendentals,
integration by parts only as exercise 5.3.5, no "hyperbolic", no "piecewise", countable-union theorem not stated):
supported. Norris (67 pages, dated 22/01/2024, sections 3.2, 8.6, 13.6, 19.2, 19.3, 20.3, 22.4, 23.1, 23.2): supported.
Tong Vector Calculus (137 pages, chapter and section names, quotient rule in text): supported except F-11. Cowley
(Michaelmas 2010, 148 pages, "not to be copied and/or redistributed" on every page, sections 1.3 to 1.9, 2.4 to 2.14,
3.3, 3.6, 3.7, 4.3.4, 4.4, 5.2 to 5.9, 6.5): supported, and see F-10. Axler (open-access PDF dated 16/08/2026, 404 pages,
CC BY-NC 4.0, section names 1A to 9C; full-text search: 0 hits for cross product, Lorentz, Levi-Civita, summation
convention, conic, shear, polar form; 3 hits for de Moivre; Gaussian elimination only in passing): supported.
Grimmett and Welsh (publisher sample front matter: copyright page with hbk 978-0-19-870996-1 and pbk 978-0-19-870997-8,
preface naming Markov and Jensen inequalities, contents through Part C and Appendices A and B): supported. O'Donnell
(Routledge page: 1st edition, copyright 2015, 336 pages, chapter titles with section topics, no "dimensional analysis",
"parallel axis" or "Foucault" on the page): supported. Beardon (Cambridge Core: fifteen chapter titles, 2005):
supported. Hammack (edition 3.4, 2018, CC BY-NC-ND, 380 pages, sections as listed; no "least upper", "supremum",
"completeness", "Dedekind", "RSA" or "Euclid's algorithm" in the text): supported. Judson (2021 print PDF, 387 pages,
GFDL, sections 5.2, 6.3, 10.2, 12.1 etc.): supported. Weber (117 pages, "Lent Term 2014" on the contents page):
supported. Chua Analysis I (61 pages, Lent 2015, disclaimer): supported. Korner (60 pages, 18/09/2007, no "Lagrange";
sinh and cosh treated): supported. Riley, Hobson and Bence (3rd edition front matter): supported. Tong Dynamics and
Relativity (166 pages, Lent Term 2013): supported. Allanach and Evans (81 pages, 2016 copyright line, torsion marked
"non-examinable and not lectured"): supported. Bourne and Kendall (Routledge: 3rd edition, copyright 1992, contents as
listed): supported. Davenport (Cambridge Core: 8th edition, chapters I to VIII with the page ranges recorded):
supported. Garling, Gregory, Burn, Hamilton (Cambridge Core chapter lists): supported. Dover page for Baxandall and
Liebeck: ISBN 9780486466200 present. No invented chapter, section, edition or ISBN was found in the sample. Open Library
records (five URLs) timed out on every attempt, so the facts resting only on them (F-12; Burkill's edition history;
Matthews) could not be rechecked.

F-15 (note) The four statuses are not conflated: every entry carries all four, and the validator enforces that
`checked` alignment needs `verified` contents. One nit: BIB-013 Ross and BIB-034 Princeton Companion are `unverified` on
the strength of a secondary mention or a search summary, which the entry says honestly.

F-16 (note) reading-map "Items:" lines agree with the register's `readings` fields for all 45 RM entries (script
check), and every summary in coverage.yaml appears verbatim in syllabus.md.

### Task 4: prerequisites

F-17 (minor) Provenance is applied inconsistently. The Schedules (page 14) say the Mechanics material "is prerequisite
for" Dynamics and Relativity and (page 13) that familiarity with it "is assumed": the strongest prerequisite statement
Cambridge makes anywhere in Part IA, yet the five MC links are `inferred-from-cambridge` on the ground that the
item-level mapping is the librarian's. The Guide (page 11) says the Dynamics course "relies heavily on vector methods",
a course-level remark of exactly the same kind, yet IA-DR-005 <- IA-VM-003 is `cambridge-stated` and `required`. Either
both are stated at course level (and the item mapping is noted) or both are inferred. The same Guide sentence on
Probability (page 8) names links with Vectors and Matrices, the counting in Numbers and Sets, the difference equations in Differential Equations, and the calculus of Vector Calculus and Analysis; the register marks the NS and DE
links `cambridge-stated` but the AN, VC and DE-calculus links on IA-PR-017 and IA-PR-019 `inferred-from-cambridge`, and
has no PR link to any VM item.

F-18 (minor) "required" is overloaded. The model defines it as "mathematically necessary for the intended treatment";
dependencies.md 3.5 then redefines it for the five Mechanics links as "assumed knowledge ... established by the
diagnostic". A fourth type (`assumed`) or a `recommended` type with a note would keep the semantics clean. Four of the
"18 hard cross-course constraints" point at revision-level items (IA-VM-001 complex-number review, IA-VM-003 vector
review), so they are school knowledge rather than constraints between Part IA courses; the table in dependencies.md
section 4 would read more honestly if it said so.

F-19 (minor) Link targets. IA-VC-011 (tensor transformation laws) requires IA-VM-018 (rotation matrices and Lorentz
transformations as transformation groups); what tensors need is orthogonal matrices, IA-VM-012, which is not linked.
Missing links of the kind the model's own `inferred-from-cambridge` criterion (same topic in two courses) would create:
IA-VC-014 (inertia tensor example) with IA-DR-014 (moments of inertia); IA-GP-012 (orthogonal and special orthogonal
groups) with IA-VM-018 (rotation matrices as transformation groups); IA-DR-019 (Lorentz transformations) with IA-VM-018
is present as librarian judgement although the Guide (page 5) names "the symmetry group of Special Relativity" in the
Vectors and Matrices description, so it could be `inferred-from-cambridge`.

F-20 (note) The five reviewed relationships (dependencies.md section 3) are reasonable and the reasoning is sourced:
Numbers and Sets / Groups as recommended only (Cambridge runs them concurrently), Groups / Vectors and Matrices two-way
with matrix-group items required, Analysis / Differential Equations and Analysis / Vector Calculus as connections (both
Guide passages read and support this). No required cross-course link contradicts Cambridge's timetable: those from
Lent courses point at Michaelmas courses, and those within Michaelmas (Groups and Differential Equations needing Vectors
and Matrices items) connect courses Cambridge runs concurrently, which the model allows. The
counts in the report (252 links; 167 / 75 / 10; 219 / 27 / 6 / 0; 61 cross-course of which 18 required) were
recomputed and agree.

### Task 5: assessment-record integrity

F-21 (major) scripts/validate.py check_mastery accepts records that the standard forbids. Each of the following, placed
on the first mastery record in a temporary copy with the validator otherwise untouched, returned RESULT: PASS:
(a) `evidence: ["studies/groups"]` (a directory); (b) `evidence: [""]` (resolves to the repository root);
(c) `evidence: ["progress/sessions/TEMPLATE.md"]` and `["README.md"]` (any existing file counts as student work);
(d) `evidence: ["../../../etc/hostname"]` (a path outside the repository); (e) a decision dated 01/01/2099;
(f) `durable-mastery` on 01/03/2026 resting on an `independent-competence` decision of 01/01/2026 that the assessor
had lowered to `familiarity` with substantial hints on 15/01/2026 (the earlier IC entry is still counted);
(g) `coverage: "not-started"` with `mastery: "durable-mastery"`; (h) an evidence file for a Groups item stored under
studies/probability/. The cause is `(ROOT / e).exists()` with no further test. Fix: require a regular file, resolved
inside ROOT, under `studies/<course>/work/` or `assessments/diagnostic/`, with a date-prefixed name, non-empty, and
tracked by git; reject dates after today; for durable mastery use only the most recent decision before it; require
`coverage: covered` once mastery is above unassessed.

F-22 (major) The fingerprint audit accepts an invented item. Appending IA-AN-021 ("Lebesgue integration") with
`fingerprint: {"chars": 0, "sha256": <sha256 of the empty string>}` to the Analysis I register (and the matching
syllabus.md and mastery.yaml lines) gave "audit: 165 items matched their source passages in order with no unmapped
gaps" and RESULT: PASS. Fix: require `chars >= 1` in check_ids and in the audit.

F-23 (minor) Valid records the validator wrongly rejects. (a) The standard (section 2) says the assessor "may lower or
raise" a level, but a history entry with `level: "unassessed"` is rejected and a record with `mastery: "unassessed"`
may carry no history, so a decision to withdraw a level cannot be recorded without deleting history. (b) Two items that
`recommend` each other are rejected as an "ordering cycle", although dependencies.md defines recommended as "the topics
can run concurrently or in either order"; only `required` links should be in the cycle check. (c) Top-level `evidence`
listed in a different order from the last history entry is rejected ("does not mirror"); compare as sets or say the
order matters.

F-24 (minor) Session records: EXCHANGE_FIELDS omits "Misconception", which the template requires and the continuity
checklist (row 5) depends on; a record whose every field is present but blank (`- Question (exact):` with nothing
after it) passes; the header lines "**Topic:**", "**Curriculum identifiers:**" and "**Participants and record:**" are
not checked; and an Assessment Decision pasted into a session record (durable mastery with substantial hints) is not
cross-checked against the standard or against mastery.yaml. Evidence files under studies/*/work/ are not validated at
all, although section 6 of the standard lists four required parts.

F-25 (minor) scripts/selftest.py: 37 tests pass (run here with --schedules-text). They cover the stated rules at one
example each, but not F-21(a) to (h), F-22, F-23 or F-24; the leak scan and --guide-text path are untested; and several
mutations target the first occurrence of a literal (`lectures_in_block: 4`, `"RM-GP-02"`, `block_item: "1 of 3"`), so
a later edit of the data could make a test silently test something else. The "baseline repository validates" test
would also pass on a copy that contains a local PDF, since only .git and __pycache__ are excluded (harmless).

F-26 (note) progress/mastery.yaml: 173 records, all `mastery: "unassessed"`, `hints: null`, `evidence: []`,
`authorised_by: null`, `history: []` (grep counts 173 for each). Confirmed.

### Task 6: copyright-sensitive material

F-27 (major) Twelve summaries are identical, letter for letter after normalisation, to the Cambridge sentence they
summarise: IA-PR-002, IA-PR-016, IA-DE-015, IA-NS-014, IA-AN-007 (full sentences of six to eight words), and IA-NS-003,
IA-AN-005, IA-AN-020, IA-PR-013, IA-DR-003, IA-DR-018, IA-VC-002 (two- to six-word topic names where no other wording
exists). A further 14 share a run of 40 to 51 letters with the source and 49 of 164 share a run covering half or more of
the summary. COPY_RUN is 56 letters, so none of these is reported, and the report's "0 possible-copy warnings" and
"verbatim statements replaced by original summaries (177)" overstate what was done. The legal exposure of eight-word
topic sentences is small, but the director was told something stronger than is true. Fix: reword the five full
sentences; lower COPY_RUN or add a whole-summary identity check; state in the report that short topic names are
necessarily shared.

F-28 (note) Leak scan run here with the Schedules and Guide text: 9 warnings, not the 5 in the report; the 4 extra are
the report quoting its own earlier warnings (reports/baseline-v1-remediation-report.md). All 9 are document or book
titles. No syllabus sentence of 70+ letters is repeated anywhere in the tracked files. Tracked files: 32 .md, 2 .yaml, 3
.py, .gitignore; no PDF, EPUB or image in any commit on any branch (`git rev-list --all --objects`). The Cambridge
sub-headings are reproduced verbatim as `heading` labels (acknowledged in the register header). Quotations in prose
(dependencies.md, source-register.md, tripos index) are a clause each. enrichment.md reproduces Harvard Canvas lecture
lists "verbatim ... abbreviated"; that is Harvard's text, not Cambridge's, and is short.

F-29 (note) Where the old verbatim text is. Searching every ref and every object in the local .git for two distinctive
Schedules sentences finds them only in blobs `c4a092d1` (coverage.yaml) and `1e4bfef6` (syllabus.md), reachable from
commits `774a338` and `c337c7a` on `feature/curriculum-baseline-v1` (local and origin). One dangling blob exists
(`63836fc2`); it is the remediation report with a `REMEDIATION_COMMIT` placeholder, not Cambridge text. No stash, no
other branch. Outside the repository, the librarian's scratchpad (/tmp/.../scratchpad/old_records.json, ia_blocks.json)
still holds the verbatim text; it is not tracked and is session-local, but the director should know it exists.

F-30 (minor) CLAUDE.md "Account setup on this machine" names a personal SSH host alias, a wrapper at ~/.local/bin/gh and
an employer ("The McNab setup elsewhere on the machine"). The repository is public and rule 8 says no personal
information. Move this to a local, untracked file.

### Task 7: validator limitations and maintainability

F-31 (minor) Restricted YAML reader: a duplicate key in a record silently takes the last value (tested: a second
`summary:` line overwrote the first with no error); a value line that an editor re-indents fails the whole file; a
record's `course`, `heading`, `printed_page`, `pdf_page` and `block` code are never checked against the id's course
(tested: `printed_page: 99`, `course: "Probability"` on an Analysis item both pass, even with the audit, because the
audit walks the text in order and ignores locators). Fix: reject duplicate keys; check `block` prefix, page numbers and
course name against a per-course table.

F-32 (minor) Other weak or missing checks: `lectures_in_block: null` on one item of a block bypasses the "block counts
must agree" test (IA-CP-002 is null while IA-CP-001 says 8); a relation may target a course-note id; reading-map
"Items:" lines are not compared with the register (consistent today, F-16, but unchecked); the `Verified via:` line
must keep a trailing space when empty or the entry fails with "has no 'Verified via' line" (tested); internal links are
checked for existence but not for anchors; summary text in syllabus.md may diverge from coverage.yaml undetected
(tested) although CLAUDE.md says the two are kept consistent.

F-33 (note) What the audit does and does not show (confirmed by experiment). It proves that each item's recorded
passage, taken in order, tiles the pypdf 6.21.2 extraction of this edition with nothing left over except headings and
lecture counts, and it catches an item deleted without re-fingerprinting and a single altered hash. It does not notice
two summaries swapped between items (tested: passes), a summary replaced by unrelated text (tested: passes), or an
item whose summary quotes the source in runs under 56 letters (tested). Normalisation strips spaces and hyphens and
repairs three known pypdf artefacts; any other extractor, or a future pypdf, will change the fingerprints wholesale,
which the documentation says. The audit is run only when a local PDF is supplied, so the routine `validate.py` before
commit never exercises it.

### Task 8: long-term session continuity

F-34 (major) Nothing in the end-of-session routine (governance/agent-workflow.md steps 1 to 6) pushes. CLAUDE.md says
"Do not push without the owner's say-so" and the resume pack tells ChatGPT to read the repository at its GitHub URL.
Unless the owner pushes after every session, a fresh ChatGPT conversation recovers the state of the last push, not the
last session. Fix: add "push, or confirm the owner has pushed" as the final step, and have the resume pack record the
commit hash it was written at.

F-35 (minor) The opening message in progress/current-session.md gives the bare repository URL. The default branch is
`main`, which holds a one-line README; everything else is on `remediation/baseline-v1-director-feedback`. Until a
merge, a fresh conversation following the message finds nothing. The message should name the branch (or raw file URLs)
and say which files to read first.

F-36 (minor) What the template does not capture: the tutor's exposition (what was explained, as opposed to asked), so
a new conversation cannot tell what the student has already been told; the student's own questions; and the pedagogical
reason for the next question. The director's eight listed fields (question, response, hints, evaluation, misconception,
next step, ids, sources) are all present in TEMPLATE.md and in the recovery checklist. Row 5 of the checklist depends on
the per-exchange "Misconception" field that the validator does not require (F-24).

F-37 (note) Could a fresh conversation recover the exact context from the repository alone? In principle yes, if
(a) the record is written exactly as the template demands, (b) it is committed and pushed, and (c) the reader is told
the branch. The mechanism (append-only records checked by git, resume pack rewritten from the record, checklist with
acceptance criteria) is sound and the protocol rightly refuses to fabricate a session. No session exists, so this was
not tested, and the repository correctly says so.

### Report accuracy

F-38 (minor) reports/baseline-v1-remediation-report.md section 1 and README.md say the remediation branch "has not
been pushed". `git ls-remote origin` shows `refs/heads/remediation/baseline-v1-director-feedback` at `93bb00f`
(remote-tracking ref updated 22/10/2026 01:06, after the report's commit). The statement is stale, and Q1 (the
already-published verbatim text) is now joined by a published remediation branch; both documents should be corrected.

F-39 (note) Other report claims checked and found accurate: commit hashes; `main` at `0228a63`; feature branch at
`c337c7a`; 177 ids unchanged in set and order (compared against the feature-branch register); counts 161 / 12 / 4 and
173 mastery records; 40 bibliography entries (ids run 001 to 036 and 038 to 041; BIB-037 does not exist and is not
referenced); 45 reading-map entries; validator and self-test output reproduced exactly (apart from the leak-scan count,
F-28).

## 3. The 177 items (task 1)

Verdict OK means the summary preserves the source's terminology, meaning and qualifiers on comparison with the PDF page
(not only the extraction). VERBATIM means faithful but identical to the Cambridge wording after normalisation (F-27).

| Ids | Page | Verdict | Note |
|---|---|---|---|
| IA-GP-001, 002 | 10 | OK | |
| IA-GP-003 | 10 | OK | adds "of the extended plane" (harmless gloss) |
| IA-GP-004 | 10 | OK | |
| IA-GP-005 | 10 | OK | "Classification of" is an added word; source says "Groups of small order (up to order 8)" |
| IA-GP-006 to 015 | 10 | OK | GP-012 proof-given tag supported ("Proof (in R3)") |
| IA-GP-016 | 10 | ISSUE | adds "including a proof that A_5 is simple"; source has no "proof" (F-02) |
| IA-VM-001 | 10 | OK | revision tag supported ("Review of") |
| IA-VM-002 | 10 | ISSUE | informal qualifier extended to de Moivre's theorem (F-03) |
| IA-VM-003 to 018 | 10 | OK | VM-010 statement-only, VM-014 proof-given, VM-004 brief all supported |
| IA-NS-N01 | 11 | OK | course note (Option (b)) |
| IA-NS-001, 002 | 11 | OK | statement-only and brief tags supported |
| IA-NS-003 | 11 | VERBATIM | five-word topic name |
| IA-NS-004 to 013 | 11 | OK | |
| IA-NS-014 | 11 | VERBATIM | full sentence identical |
| IA-NS-015 to 022 | 11 | OK | |
| IA-DE-001 | 11 | OK | adds "review" / "single-variable"; informal-treatment tag supported |
| IA-DE-002 to 011 | 11 | OK | DE-002 statement-only and informal tags supported |
| IA-DE-012 | 11 | ISSUE | "(equidimensional)" is an unrecorded interpretation (F-04) |
| IA-DE-013, 014 | 11 | OK | DE-014 statement-only supported |
| IA-DE-015 | 11 | VERBATIM | full sentence identical |
| IA-DE-016 to 020 | 11 | OK | DE-016 statement-only supported |
| IA-AN-001 to 004 | 12 | OK | |
| IA-AN-005 | 12 | VERBATIM | theorem name |
| IA-AN-006 | 12 | ISSUE | "bounded" dropped from "closed bounded interval" (F-01) |
| IA-AN-007 | 12 | VERBATIM | full sentence identical |
| IA-AN-008 to 014 | 12 | OK | |
| IA-AN-015 | 12 | OK | whole item starred in the PDF; status and proof-given tag correct |
| IA-AN-016 to 019 | 12 | OK | |
| IA-AN-020 | 12 | VERBATIM | two-word topic name |
| IA-PR-001 | 12 | OK | |
| IA-PR-002 | 12 | VERBATIM | full sentence identical |
| IA-PR-003 to 012 | 12 | OK | PR-003 proof-given supported |
| IA-PR-013 | 12 | VERBATIM | two-word topic name |
| IA-PR-014, 015 | 12 | OK | |
| IA-PR-016 | 12 | VERBATIM | full sentence identical |
| IA-PR-017 to 027 | 12 | OK | PR-026 statement-only, PR-027 statement-only plus proof-sketch supported |
| IA-VC-001 | 13 | OK | |
| IA-VC-002 | 13 | VERBATIM | two-word topic name |
| IA-VC-003 | 13 | OK | |
| IA-VC-004, 005 | 13 | OK | starred spans match the asterisks on the page; VC-005 statement-only supported |
| IA-VC-006 to 014 | 13 | OK | VC-008 informal-proof, VC-013 revision supported |
| IA-DR-N01, N02 | 13 | OK | course notes |
| IA-DR-001, 002 | 13 | OK | |
| IA-DR-003 | 13 | VERBATIM | two-word topic name |
| IA-DR-004 to 007 | 13 | OK | |
| IA-DR-008 | 13 | OK | adds "in a central force" (harmless gloss) |
| IA-DR-009 | 13 | OK | |
| IA-DR-010 | 13 | OK | whole sentence starred in the PDF; status and brief tag correct |
| IA-DR-011 to 017 | 13 | OK | |
| IA-DR-018 | 13 | VERBATIM | three-word topic name |
| IA-DR-019 to 024 | 13 | OK | (1+1) and (3+1) rendered in words |
| IA-CP-001 | 14 | OK | |
| IA-CP-002 | 14 | OK | `lectures_in_block` is null while CP-001 in the same block says 8 (F-32) |
| IA-MC-N01 | 14 | ISSUE | "prerequisite" softened to "builds on" (F-05) |
| IA-MC-001 to 010 | 14 | OK | MC-001 brief tag supported; ten lectures match the page one to one |

Totals: 177 items; 172 OK (12 of them verbatim); 5 ISSUE (one major: IA-AN-006; four minor: IA-GP-016, IA-VM-002,
IA-DE-012, IA-MC-N01). Ancillary items IA-CP and
IA-MC are outside the fingerprint audit and were compared by hand against page 14.

## 4. What was checked and how; what could not be checked

Checked:
- Repository state: `git status`, `git log --all`, `git ls-remote`, `git for-each-ref`, `git fsck --lost-found`,
  `git rev-list --all --objects` with a content grep of every blob for two Schedules sentences; tracked-file listing by
  extension.
- Source hashes: sha256sum of the six local PDFs against source-register.md and the Tripos index (all match).
- Every item: a dump of id, heading, summary, qualifiers, starred_part, block, position, lectures, status and links
  (fable_work/dump.txt) read against the pypdf extraction and against PNG renders of PDF pages 10 to 14 (two halves per
  page at 2.2x; fable_work/png/). Lecture sums per course, page numbers, block codes, course names and heading
  placement were checked by script (fable_work/syl.py, final register script).
- Validator: run on a copy with and without `--schedules-text` and `--guide-text` (PASS, 0 errors; 9 leak warnings);
  selftest.py with `--schedules-text` (37 PASS). The attack scripts fable_work/attack.py and attack2.py hold the exact
  mutations behind F-21 to F-24 and F-31 to F-33; each ran the unmodified validator on a fresh copy.
- Overlap: the longest common letter-run between each summary and its source passage, using the validator's own
  normalisation (fable_work/overlap.py; passages.json).
- Bibliography: 33 URLs fetched with curl (28 reachable; 5 Open Library timeouts); 15 PDFs opened with PyMuPDF for
  page counts, dates, outlines and full-text searches; publisher pages stripped to text and searched.
- Prerequisites: all 61 cross-course links listed by script with type and provenance; the six `cambridge-stated` links
  and the five reviewed relationships compared with the Guide pages 5, 6, 8, 9, 11 and Schedules pages 13 and 14.
- Continuity: template, README, resume pack, workflow and test protocol read; validator session checks exercised with
  synthetic records in the temporary copy only.

Not checked, and why:
- Open Library records (Allenby print ISBN and imprint, Burkill editions, Matthews, Grimmett and Welsh page count):
  every request timed out from this machine, as the librarian also reported.
- Burkill's contents (the librarian's source is an unlinked scan; nothing citable exists to open).
- The 2025 examination papers were not compared with the register (out of the brief; the index maps questions to
  courses only).
- The 74-URL liveness recheck in report section 7 was not repeated in full (33 of the URLs were opened).
- Reading alignment cells for Numbers and Sets, Groups, Analysis I and Dynamics and Relativity were spot-checked
  through the sources opened (Lebl, Hammack, Judson, Chua, Korner, O'Donnell page) rather than cell by cell; the
  Vectors and Matrices (Axler, Cowley) and Probability (Norris, Weber, Grimmett and Welsh) tables were checked in full
  against the contents lists, with the one correction in F-10.
- The live continuity test (no session exists; none was fabricated).
- Mathematical quality or depth of any reading resource (a contents list cannot show it; the repository says the same).
