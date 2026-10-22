# Source register

Every external document that the curriculum baseline rests on, with edition, retrieval details and status. Retrieval date for all entries:
**21/10/2026**, by `curl` from the working VM. The SHA-256 lets the student check that the copies they hold are identical to the ones used here.

## 1. Documents the student named

The student supplied these file names: `schedules.pdf`, `coursesIA.pdf`, `paperia_1_2025.pdf` to `paperia_4_2025.pdf`. No copies were found in the
repository or on the VM, so the same-named files were retrieved from the Faculty's public site and the student later supplied the URLs below. Whether
the student's own copies are the same editions has **not been confirmed**: compare hashes.

| ID | Document | Edition stamped on the document | URL | Server `Last-Modified` | Pages | SHA-256 |
|---|---|---|---|---|---|---|
| SRC-01 | Schedules of Lecture Courses and Form of Examinations for the Mathematical Tripos | **2026-27, revised 19 August 2026** | https://www.maths.cam.ac.uk/undergrad/files/schedules.pdf | Fri 18/09/2026 | 46 | `5eedbdd40aef930178266ac2cf196d05447c391b8e2fb013369bd3a34dc8acf4` |
| SRC-02 | Mathematical Tripos Guide to Courses in Part IA | **2026-27, revised 18 August 2026** | https://www.maths.cam.ac.uk/undergrad/files/coursesIA.pdf | Fri 28/08/2026 | 14 | `f3fa103bb4517f90451f7726f089436a9d745820a9f899fecdb1f89e6ced2adc` |
| SRC-03 | Part IA examination Paper 1 | 2025 (sat 05/06/2025) | https://www.maths.cam.ac.uk/undergrad/pastpapers/files/2025/paperia_1_2025.pdf | Fri 04/07/2025 | 9 | `1a849ff0c6a746bdedfedd2df8b99ca1c0b56ddd479cec85b743d9e4394efe40` |
| SRC-04 | Part IA examination Paper 2 | 2025 (06/06/2025) | .../paperia_2_2025.pdf | Fri 04/07/2025 | 9 | `4882b4cb40767bd6c1674b587e835158fba449a278f6b9d76db719811905cdde` |
| SRC-05 | Part IA examination Paper 3 | 2025 (09/06/2025) | .../paperia_3_2025.pdf | Fri 04/07/2025 | 9 | `8eef8878b319660886af7ff03a35645c5f252facad47041e1a5d6d8c48063f3b` |
| SRC-06 | Part IA examination Paper 4 | 2025 (11/06/2025) | .../paperia_4_2025.pdf | Fri 04/07/2025 | 8 | `8bf66fdd2fc95504789b8e671465095703a6019dac454e8900269682ff967bde` |
| SRC-07 | Past papers index page, Part IA 2025 | n/a | https://www.maths.cam.ac.uk/undergrad/pastpapers/maths-ia/2025 | n/a | n/a | n/a |
| SRC-08 | Harvard Math 55A syllabus (Canvas) | Fall 2025-26, Auroux | https://canvas.harvard.edu/courses/154983/assignments/syllabus | n/a | n/a | n/a |
| SRC-09 | Harvard Math 55B syllabus (Canvas) | Spring 2025-26, Auroux | https://canvas.harvard.edu/courses/162402/assignments/syllabus | n/a | n/a | n/a |
| SRC-10 | Harvard "Math 55" worksheets (discrete mathematics, 2018) | Spring 2018 | https://people.math.harvard.edu/~cmwang/teaching/55/ | n/a | n/a | n/a |

The Guide (SRC-02) links to the Schedules at `https://www.maths.cam.ac.uk/undergrad/course/schedules.pdf`. That URL redirects to `/undergrad/files/schedules.pdf`,
the file used here; the two downloads have identical SHA-256 hashes (checked 21/10/2026).

### Decisions already taken about these sources

| Matter | Decision (see [governance/director-decisions.md](../governance/director-decisions.md)) |
|---|---|
| Programme | Part IA Option (a), Pure and Applied Mathematics (D-01) |
| Syllabus authority | The 2026-27 Schedules (D-02) |
| Examination practice | The 2025 papers are accepted, with the edition difference acknowledged (D-03). The 2026-27 Schedules note a new merit-mark formula and a new Part IB Easter course (Geometry) and may differ in Part IA content from the year the papers were set; a question touching material absent from the 2026-27 Schedules is treated as out of syllabus |

## 2. Representation of Cambridge text in this public repository

**Director decision D-16:** the public repository must not reproduce substantial Cambridge syllabus text. The Schedules and Guide carry no copyright, licence or reuse
statement that was found (searched for "copyright", "licence" and "Creative Commons"), so redistribution rights are **not established**. The Faculty states of the
examination papers: "All papers are copyright by the University of Cambridge and may not be reproduced without permission."

What the repository therefore holds:

| Held | Not held |
|---|---|
| For each syllabus item: an **original summary** written by the librarian, the **exact Cambridge sub-heading** (a short label), the source document, **printed and PDF page**, the **paragraph** (block) and the item's **position within it** | The Schedules' syllabus sentences |
| A **fingerprint** per item: the length and SHA-256 of the normalised source passage | The Cambridge PDFs, the extracted text, and the examination papers (`.gitignore` blocks PDFs) |
| Scope tags (for example `statement-only`, `informal-treatment`) derived from the source wording | Any textbook or lecture notes |
| Short quotations in prose (a clause or a sentence) where needed for a documented argument, for example in [dependencies.md](../curriculum/dependencies.md) | Reproduction of lists or paragraphs |

The summaries are **librarian drafts** (`summary_status: librarian-draft`). They are written to preserve mathematical meaning and scope, including qualifiers such as "statement only" or
"informal"; none has yet been compared with the source by the director or the independent reviewer. They must not be relied on as a statement of Cambridge's syllabus: the Schedules are.

### Already-published material (needs a director decision)

Before this remediation, the branch `feature/curriculum-baseline-v1` was pushed to the public repository (commits `774a338` and `c337c7a`, 21/10/2026) and contained the verbatim
syllabus statements in `curriculum/coverage.yaml` and `curriculum/syllabus.md`. It was readable anonymously (checked 21/10/2026; `main` was clean; no forks, stars or pull requests).
Replacing the text on a later commit **does not remove it from the already-published history**. Options for the director, none of which Claude Code has taken: (a) leave the history as it is
and accept the risk; (b) delete the remote branch and republish from a history that never contained the text, which needs a force push or deleting and recreating the branch (and GitHub may
retain cached objects reachable by commit hash until garbage collected); (c) ask GitHub to purge cached views; (d) seek Faculty permission. Deleting the branch is destructive and outward-facing, so it
needs the owner's explicit instruction.

## 3. Auditing an item against the original Schedules (optional, local)

Without a local copy the register can be checked only structurally. With a copy of the Schedules PDF on the reviewer's machine:

1. Download `schedules.pdf` and confirm its SHA-256 matches SRC-01.
2. Extract the text with `scripts/extract_pdf_text.py` (needs the optional third-party package `pypdf`; the fingerprints were calibrated on `pypdf` 6.21.2).
3. Run `python3 scripts/validate.py --schedules-text schedules.txt`.

The audit normalises the source (straight apostrophes, repaired extraction artefacts such as "M¨ obius" to "Möbius" and "V ector" to "Vector", no spaces or hyphens), then walks each course in order.
For every item it takes the passage of the recorded length at the expected position, hashes it, and compares the hash with the register. It also requires that the passages **tile** the
course's text with nothing left over except the known headings and lecture counts, so any omitted syllabus text is reported. It warns if a summary shares about nine consecutive words with its
source passage (a check against copying).

**What a pass means, and does not mean.** A pass shows that each item was built from this edition of the document and that no syllabus text is unmapped. It is a **structural and text-matching
audit**. It is **not** proof of semantic equivalence: it cannot tell whether a summary is a faithful, complete and accurate rendering of its source. That is an academic judgement for the director
and the independent reviewer, who should compare each summary with the PDF page cited. A different extractor may produce different spacing, ligatures or accents and so different fingerprints
(use `--show-mismatch` to see the local passage).

Known limitations of the source text:

- Text extraction flattens superscripts and subscripts (R^3 appears as `R3`, S_n as `Sn`). The summaries write them with `^` and `_`.
- PDF pages 12 and 13 were rendered and visually compared with the extracted text (starred spans, superscripts). Pages 10, 11 and 14 were **not** visually checked.
- The audit covers the eight examinable courses and the course notes in them; the ancillary courses (Mechanics, Computational Projects) are not covered by the fingerprint audit and need a manual check.
- Two spans are starred inside otherwise examinable items (general orthogonal curvilinear coordinates, in IA-VC-004 and IA-VC-005); whole starred items are IA-AN-015 and IA-DR-010.

## 4. Part IA structure facts used

From Schedules 2026-27, printed p.7: two options, (a) Pure and Applied Mathematics and (b) Mathematics with Physics. This programme follows **option (a)** (D-01); option (b) replaces Numbers and
Sets and Dynamics and Relativity with the Natural Sciences Physics course. Papers 1 to 4 pair the courses as shown in
[assessments/tripos-papers/index.md](../assessments/tripos-papers/index.md).

## 5. Statuses

- **Retrieved and read (SRC-01 to SRC-06):** the PDF was downloaded, hashed and its text read.
- **Fetched (SRC-07 to SRC-10):** the page was fetched on 21/10/2026 and its text read; SRC-08 and SRC-09 were read as raw HTML (not only as a tool summary). They carry no licence statement of their own.
- Textbook and lecture-note sources are listed with their own four-part verification status in [bibliography.md](bibliography.md), and the outstanding checks in [verification-tasks.md](verification-tasks.md).
