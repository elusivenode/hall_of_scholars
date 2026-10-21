# Source register

Every external document that the curriculum baseline rests on, with edition, retrieval details and
status. Retrieval date for all entries: **21/10/2026**, by `curl` from the working VM. The SHA-256 lets
the student check that the copies they hold are identical to the ones used here.

## 1. Documents the student named

The student supplied these file names: `schedules.pdf`, `coursesIA.pdf`, `paperia_1_2025.pdf` to
`paperia_4_2025.pdf`. No copies were found in the repository or on the VM, so the same-named files were
retrieved from the Faculty's public site and the student later supplied the URLs below. Whether the
student's own copies are the same editions has **not been confirmed** - compare hashes.

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

The Guide (SRC-02) links to the Schedules at `https://www.maths.cam.ac.uk/undergrad/course/schedules.pdf`.
That URL redirects to `/undergrad/files/schedules.pdf`, the file used here; the two downloads have
identical SHA-256 hashes (checked 21/10/2026).

### Edition mismatch (open question for the director)

The Schedules and Guide are the **2026-27** editions; the supplied examination papers are the **2025**
papers (academic year 2024-25). The 2026-27 Schedules note a new merit-mark formula and a new Part IB
Easter Term course (Geometry), and may differ in Part IA content from the year the papers were set. The
baseline uses the 2026-27 Schedules as the syllabus authority. The director should confirm that, or ask
for the 2024-25 Schedules, which this baseline did not obtain.

### Copyright and redistribution (open question for the director)

- The Faculty states of the examination papers: "All papers are copyright by the University of Cambridge
  and may not be reproduced without permission." **No paper is stored here**; `.gitignore` excludes PDFs.
- SRC-01 and SRC-02 carry **no copyright, licence or reuse statement** that was found (searched for
  "copyright", "licence", "Creative Commons"). Redistribution rights are therefore **not established**.
- The syllabus register ([coverage.yaml](../curriculum/coverage.yaml)) and its readable form
  ([syllabus.md](../curriculum/syllabus.md)) quote the Part IA syllabus statements verbatim, as the task
  requires ("exact source heading or syllabus statement"). This is a substantial extract of a Cambridge
  document in a **public** repository. Options for the director: (a) keep as is and accept the risk,
  (b) obtain Faculty permission, (c) keep the repository private, or (d) replace the verbatim text with
  headings, page references and a hash, keeping the register as pointers only. Claude Code recommends
  deciding this before the branch is merged.

## 2. How the syllabus text was extracted

- Tool: `pypdf` 6.21.2 (`page.extract_text()`), run in a throwaway virtual environment outside the
  repository. `scripts/extract_pdf_text.py` reproduces this.
- Pages used: Schedules PDF pp.10 to 14 (printed pp.8 to 12) for the courses, and printed p.7 for the
  examination structure.
- Normalisation applied to produce the `source` field of each register record (nothing else was altered):
  1. line breaks joined with a single space;
  2. line-end hyphenation removed where it is a word break (for example "isomor-" + "phic"), and kept where
     the hyphen is real ("(1 + 1)-dimensional", "two-dimensions");
  3. extraction artefacts of accented letters repaired: "M¨ obius" to "Möbius", "Hˆ opital" to "Hôpital";
     spurious spaces repaired: "V ector" to "Vector"; curly apostrophes made straight;
  4. the lecture-count marker `[n]` removed from the statement and stored as `lectures_in_block`;
  5. everything else kept exactly as extracted, including the asterisk and `∗` star markers.
- **Known limitation:** text extraction flattens superscripts and subscripts (R^3 appears as `R3`, S_n as
  `Sn`, A_5 as `A5`, nabla-squared as `∇2`) and drops the typographic distinction of blackboard-bold R and C.
- Visual check: PDF pages 12 and 13 were rendered to images and compared with the extracted text
  (starred spans and superscripts). Pages 10, 11 and 14 were **not** visually checked.
- Automated check: `python3 scripts/validate.py --schedules-text <extracted text>` confirms that every
  statement for the eight examinable courses occurs in order in the Schedules text and that **no Schedules
  text between the headings is left unmapped**. The ancillary courses (Mechanics, Computational Projects)
  are not covered by that audit; Codex should check them by hand.

## 3. Part IA structure facts used

From Schedules 2026-27, printed p.7: two options (a) Pure and Applied Mathematics and (b) Mathematics with
Physics. This programme follows **option (a)**, all eight examinable courses; Option (b) replaces Numbers and
Sets and Dynamics and Relativity with the Natural Sciences Physics course. Whether the student follows
option (a) is an assumption to be confirmed. Papers 1 to 4 pair the courses as shown in
[assessments/tripos-papers/index.md](../assessments/tripos-papers/index.md).

## 4. Statuses

- **Retrieved and read (SRC-01 to SRC-06):** the PDF was downloaded, hashed and its text read.
- **Fetched (SRC-07 to SRC-10):** the page was fetched on 21/10/2026 and its text read; SRC-08 and
  SRC-09 were read as raw HTML (not only as a tool summary). They carry no licence statement of their own.
- Textbook and lecture-note sources are listed with their own verification status in
  [bibliography.md](bibliography.md).
