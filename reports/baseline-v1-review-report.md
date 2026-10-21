# Curriculum Baseline v1 - Review Report

Prepared by Claude Code (curriculum librarian) on 21/10/2026 for ChatGPT (curriculum director) and Codex
(independent reviewer). **This baseline is not approved. It has not been merged. Nothing has been taught,
assessed or marked as mastered.** Awaiting the curriculum director's review.

## 1. Branch and commits

| | |
|---|---|
| Branch | `feature/curriculum-baseline-v1` (from `main` at `0228a63`) |
| Baseline content commit | `774a3381e59be850cb5f5e3a73f5b5f9e4bee491` (short `774a338`); a follow-up commit records this hash in the report and holds no other change |
| Remote | **not pushed.** See decision D1 in section 9 before pushing: the branch contains verbatim syllabus text and the repository is public. |

## 2. Files created

Nothing existing was modified except `README.md` (was a one-line title). Created:

- `curriculum/` - `coverage.yaml` (register), `syllabus.md` (readable view), `reading-map.md`, `enrichment.md`, `dependencies.md`
- `progress/` - `mastery.yaml`, `weaknesses.md`, `current-session.md`, `sessions/TEMPLATE.md`
- `governance/` - `teaching-charter.md`, `assessment-standard.md`, `agent-workflow.md`
- `references/` - `bibliography.md`, `source-register.md`
- `assessments/` - `diagnostic/README.md`, `tripos-papers/index.md`
- `studies/<course>/README.md` for the eight courses
- `scripts/` - `validate.py` (standard library only), `extract_pdf_text.py` (needs the optional third-party `pypdf`)
- `README.md`, `CLAUDE.md`, `.gitignore` (blocks PDFs and other copyright material), `reviews/` and `reports/`

## 3. Syllabus items mapped, by course

Source: Schedules 2026-27 (revised 19/08/2026), Part IA, printed pp.8 to 12.

| Course | Code | Items | Of which starred | Lectures (sum of blocks) |
|---|---|---|---|---|
| Numbers and Sets | IA-NS | 22 | 0 | 24 |
| Groups | IA-GP | 16 | 0 | 24 |
| Vectors and Matrices | IA-VM | 18 | 0 | 24 |
| Differential Equations | IA-DE | 20 | 0 | 24 |
| Analysis I | IA-AN | 20 | 1 (IA-AN-015) | 24 |
| Probability | IA-PR | 27 | 0 | 24 |
| Vector Calculus | IA-VC | 14 | 0 (two examinable items contain a starred span) | 24 |
| Dynamics and Relativity | IA-DR | 24 | 1 (IA-DR-010) | 24 |
| **Examinable total** | | **161** | 2 | 192 |
| Mechanics (non-examinable, ancillary) | IA-MC | 10 | n/a | 10 |
| Computational Projects (ancillary) | IA-CP | 2 | n/a | 8 |
| Course notes (not tracked for mastery) | `IA-NS-N01`, `IA-DR-N01`, `IA-DR-N02`, `IA-MC-N01` | 4 | | |

177 register records in all: 161 examinable-course items, 12 ancillary items, 4 course notes.
`progress/mastery.yaml` has 173 records (everything except the course notes), **all `unassessed`**.

Granularity: one item is a distinct topic within a Schedules paragraph (typically a sentence or two), 3 to 6 per
heading. The lecture count `[n]` is given by the Schedules for a whole paragraph and is stored on each item of
that paragraph as `lectures_in_block`; it is not a per-item figure.

## 4. Coverage audit results

`python3 scripts/validate.py --schedules-text <text of schedules.pdf>` performs, for the eight courses:

1. each `source` statement is found, **in order**, in the Schedules text (spacing and hyphenation ignored);
2. **no Schedules text between the headings is left unmapped** (the gap before each item, after removing the
   known headings, lecture counts and star markers, must be empty, and likewise the tail of each course).

Result: **164 items (161 topic items plus 3 course notes) matched in order with no unmapped gaps.**
Mutation tests confirm the audit has teeth: deleting an item produces `unmapped Schedules text before IA-GP-010`;
altering a word produces `IA-GP-004 source statement not found`.

Not covered by the audit: the ancillary courses (Mechanics, Computational Projects), and visual fidelity of the
text. PDF pages 12 and 13 were rendered and visually compared (starred spans, superscripts). **Pages 10, 11 and 14
were not visually checked.**

## 5. Proposed principal textbooks (full detail in `curriculum/reading-map.md`)

| Course | Proposed primary | Status |
|---|---|---|
| Numbers and Sets | Allenby, *Numbers and Proofs* (free supplement: Hammack, *Book of Proof*, CC BY-NC-ND) | partially verified |
| Groups | Beardon, *Algebra and Geometry* (free supplement: Judson, GFDL) | partially verified |
| Vectors and Matrices | Beardon, with Cowley's 2010 DAMTP notes as the course-matched spine; Axler as a supplement | partially verified / verified |
| Differential Equations | Robinson, *An Introduction to Ordinary Differential Equations* | partially verified |
| Analysis I | Burkill, *A First Course in Mathematical Analysis* (access risk; free supplement: Lebl) | contents **unverified** |
| Probability | Grimmett and Welsh, *Probability: An Introduction* (free notes: Weber, Norris) | **unverified** |
| Vector Calculus | Bourne and Kendall (free notes: Tong, covering all six blocks) | partially verified |
| Dynamics and Relativity | O'Donnell, *Essential Dynamics and Relativity* (also covers Mechanics) | verified |

The student's own texts: **Axler is not suitable as the Vectors and Matrices primary** (verified: the 4th edition is
open access under CC BY-NC; determinants are in 9C, not omitted; there is no cross product, suffix notation,
Lorentz transformations or conics, and only passing mentions of Gaussian elimination). **Baxandall and Liebeck is
a rigorous companion** for curves, parametrisation and the integration theorems, but no source seen confirms
Cartesian tensors, the Laplace/Poisson uniqueness theorems, Maxwell's equations context or curvilinear
coordinates. The Princeton Companion is unverified (see D7).

## 6. Harvard Math 55 integration summary (`curriculum/enrichment.md`)

- Two Harvard resources were supplied and are documented separately. The Canvas pages are **Math 55a**
  (Studies in Algebra and Group Theory, Fall 2025-26) and **Math 55b** (Studies in Real and Complex Analysis,
  Spring 2026), Prof. Auroux. Their lecture-by-lecture topic lists were read from the raw pages. The
  `~cmwang` page is a **2018 discrete mathematics course**, not the honours sequence.
- Enrichment is optional and follows the Cambridge material: Groups then Artin-style group material (55a L1-L4,
  L21-L22); Vectors and Matrices then Axler; Analysis I then Rudin and 55b L19-L20 (the closest overlap).
- "Beyond Part IA" claims are grounded in the Schedules: Sylow theorems (Part IB Groups, Rings and Modules),
  uniform convergence, metric spaces, compactness and the inverse function theorem (Part IB Analysis II), Jordan
  form and bilinear forms (Part IB Linear Algebra), representation theory (Part II).
- Differential Equations, Probability, Vector Calculus and Dynamics and Relativity have little or no Math 55
  overlap; none is forced.
- Access: Math 55 is open only to Harvard first-year students; lecture notes and problem sets were not opened; no
  archive found carries an open licence.

## 7. Validation results

`python3 scripts/validate.py --schedules-text <schedules text>` result: see section 10 (recorded at the final
commit). Checks performed: unique and well-formed ids; valid prerequisite references and no cycles; lecture
counts per block consistent and summing to 24 (Mechanics 10, Computational Projects 8); every topic item has
exactly one state record and none for course notes; **no mastery above `unassessed` without evidence, the assessor's
authorisation and a DD/MM/YYYY date**; every reading-map id and every `BIB-` citation resolves; every
bibliography entry marked verified or partially verified carries a source URL; every id appears in
`syllabus.md`; no broken internal Markdown links; and the source-fidelity audit of section 4.

14 adversarial mutation tests were run against a scratch copy; all 14 are caught. This surfaced one genuine
gap (a block whose items disagreed on lecture count went unnoticed), which is now fixed. All 58 distinct external
URLs cited in the repository returned HTTP 2xx on 21/10/2026.

## 8. Uncertainties and unverified references

Unverified or only partly verified (see `references/bibliography.md` for what was and was not seen):

- **Unverified entirely:** Grimmett and Welsh (proposed Probability primary); Ross; Riley, Hobson and Bence; Rindler;
  the Princeton Companion.
- **Contents unverified:** Burkill (proposed Analysis I primary; the year Cambridge cites, 1978, conflicts with the
  library record, 1962); Bourne and Kendall (contents paraphrased by the fetch tool; year conflict: Routledge
  "Copyright 1992" against Cambridge's 1999); Baxandall and Liebeck (10 of 11 chapter titles); Beardon below
  chapter level; Robinson below Part level; Allenby's chapter numbers, ISBN and whether it covers modular
  arithmetic, RSA and countability; Garling below Part level.
- **Free notes:** all are older than 2026-27 (Cowley 2010; Tong D&R 2013; Weber 2015; Allanach and Evans 2016;
  Chua 2014-15; Norris 2024) and may not match the current schedule. Cowley's are "not to be copied and/or
  redistributed" and Allanach and Evans's "not to be quoted or reproduced"; they are linked, never copied. Chua's
  are unofficial and unlicensed.
- **Example sheets:** only sheet 1 was read for most courses; no solutions exist.
- **Prerequisites:** 144 of the 153 item-level prerequisite lists are Claude Code's judgement; only 9 are
  explicitly stated by Cambridge.
- **Text fidelity:** superscripts and subscripts are flattened in the extracted text (`R3` is R^3).

## 9. Decisions and academic questions for the curriculum director

**D1. Copyright and the public repository (needs a decision before the branch is pushed).** The register and
`syllabus.md` quote the Part IA syllabus verbatim (as the task requires), a substantial extract of a Cambridge
document that carries no licence or reuse statement. The repository is public. Options: (a) keep and accept the risk;
(b) seek Faculty permission; (c) make the repository private (ChatGPT then cannot read it by URL); (d) replace the
verbatim text with headings, page references and hashes. Claude Code recommends deciding this before the branch is
merged, and has **not pushed** the branch pending your answer.

**D2. Edition mismatch.** The syllabus authority used is the **2026-27** Schedules and Guide; the supplied papers are
**2025** (academic year 2024-25). Confirm that this pairing is acceptable, or supply the 2024-25 Schedules. The
student's own copies of the named files were not compared with the retrieved ones (hashes are in
`references/source-register.md`).

**D3. Option (a) assumed.** The programme follows Option (a) Pure and Applied Mathematics (all eight courses, including
Numbers and Sets and Dynamics and Relativity). Confirm.

**D4. Granularity and the item list.** Confirm the item splits (161 items), or ask for finer or coarser items. Ids are
stable; a split adds new ids.

**D5. Prerequisites.** Confirm or amend the 144 `librarian-judgement` prerequisite lists, especially Groups and Vectors
and Matrices (the dependency runs both ways in the schedules) and the placement of Analysis I (`curriculum/dependencies.md`).

**D6. Tracking scope.** Whether to track for mastery: the two starred items (IA-AN-015, IA-DR-010; lectured but not
examinable), the starred spans inside IA-VC-004 and IA-VC-005, and the 12 ancillary items (Mechanics, Computational
Projects). They are tracked by default; the course notes are not.

**D7. Reading choices.** (i) Analysis I: Burkill is Cambridge's dagger book but contents are unverified and it may be hard
to obtain; accept, or substitute Garling or Lebl. (ii) Probability: confirm Grimmett and Welsh, or substitute the free
Weber/Norris notes once the book is checked. (iii) Vectors and Matrices: confirm Beardon plus Cowley, with Axler as a
supplement. (iv) Vector Calculus: confirm Bourne and Kendall plus Tong, with Baxandall and Liebeck as a companion.
(v) The Princeton Companion: the student calls it "...to Pure Mathematics"; the title found is "The Princeton Companion to
Mathematics". The student offered to supply the title and contents pages to confirm.

**D8. Assessment standard.** Confirm the 28-day minimum interval for durable mastery, and the hint scale (`none`,
`minor`, `substantial`) with `independent-competence` requiring `none` (`governance/assessment-standard.md` sections 4
and 5). These are proposals.

**D9. Open syllabus-content questions.** Real numbers (least upper bounds) and Differential Equations multivariate
topics have no verified reading source; see the notes in `reading-map.md`.

**D10. The role of the 2018 discrete mathematics page.** Optional extra practice at most; confirm or drop.

## 10. Validation output at the final commit

```text
$ python3 scripts/validate.py --schedules-text schedules.txt
audit: 164 items matched in order against the Schedules text with no unmapped gaps
register records by course code: AN=20, CP=2, DE=20, DR=26, GP=16, MC=11, NS=23, PR=27, VC=14, VM=18
bibliography entries: 34; reading-map entries: 45; mastery records: 173
RESULT: PASS (0 errors, 0 warnings)
```

## 11. Instructions for an independent Codex review

Work on a separate branch `review/baseline-v1-<date>` (from `feature/curriculum-baseline-v1`) or in `reviews/`. **Do not
edit `curriculum/`, `progress/`, `governance/` or `references/`.** Write findings to
`reviews/baseline-v1-codex-review.md`, each with the item id or file, the Cambridge page, and your evidence. Check at least:

1. **Run the validator** (`python3 scripts/validate.py`) and confirm PASS.
2. **Reproduce the audit independently.** Download `schedules.pdf`, compare its SHA-256 with `references/source-register.md`, extract
   the text with a *different* tool from the one used here (for example `pdftotext -layout`, not `pypdf`), then run
   `scripts/validate.py --schedules-text` on that text. Differences expose extraction artefacts specific to one tool.
3. **Visually compare PDF pages 10, 11 and 14** against the register, which were not visually checked. Look for
   subscripts, superscripts, star markers and any text the extraction dropped. Pages 12 and 13 were checked.
4. **Completeness:** for each of the eight courses confirm that every sub-heading and every sentence of the Part IA
   Schedules is represented, that no unmapped text remains, and that the lecture counts match the PDF. Check the
   four course notes and that nothing in the examination-structure pages (printed p.7) is missed.
5. **Interpretation errors:** look for places where an item splits a Schedules sentence so as to change its meaning, or where
   a starred span is mishandled (IA-AN-015, IA-DR-010, and the two spans in IA-VC-004 and IA-VC-005).
6. **Prerequisites:** challenge implausible, missing or circular-in-spirit edges, particularly cross-course ones and the
   nine `cambridge-stated` ones (check each against the quoted Guide or Schedules sentence).
7. **Verify references.** For every bibliography entry marked verified or partially verified, open its `Verified via` URL and
   confirm what the `Seen` field claims; confirm that nothing marked `Not seen` is relied on in `reading-map.md`. In
   particular re-check the Axler and Baxandall and Liebeck assessments and the Tong, Weber and Norris contents.
8. **Source register:** confirm each SHA-256 and the edition stamps; confirm the copyright statements quoted.
9. **Harvard map:** compare `curriculum/enrichment.md` with the two Canvas pages and the `~cmwang` page, and confirm every
   "beyond Part IA" claim against the cited Schedules course.
10. **Integrity:** confirm `progress/mastery.yaml` has no value other than `unassessed`, no PDF is tracked by git, and no
    invented chapter, exercise, ISBN or session appears anywhere.
11. **Maintainability:** comment on `scripts/validate.py` (does the restricted YAML parser reject malformed input? are
    there checks missing?) and the repository layout.
