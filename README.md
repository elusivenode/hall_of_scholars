# hall_of_scholars

A long-term programme of rigorous mathematical study based on the **University of Cambridge Mathematical
Tripos Part IA**, aimed at a firm foundation in pure and applied mathematics and, later, computational
mathematical physics. It prizes mathematical maturity, independent proof construction and durable
understanding over speed or syllabus completion.

**Status: Curriculum Baseline v1, remediated twice (director feedback, then the independent Fable review) - awaiting the curriculum director's final decision. Merge authorisation has not been granted.**
Nothing has been taught, assessed or marked as mastered. See [reports/baseline-v1-r2-readiness.md](reports/baseline-v1-r2-readiness.md) and
[governance/director-decisions.md](governance/director-decisions.md) for what is decided and what is open. The authoritative branch is named in
[progress/current-session.md](progress/current-session.md).

## Who does what

| Agent | Role |
|---|---|
| **ChatGPT** | Curriculum director, Socratic tutor and academic assessor. Chooses the sequence, tutors, evaluates arguments, and alone authorises mastery judgements. |
| **Claude Code** | Curriculum librarian and repository maintainer. Keeps the registers, sources and session records; implements authorised changes; never infers mastery. |
| **Codex** | Independent reviewer. Checks the baseline against the Cambridge sources and challenges unsupported claims; does not edit authoritative records. |

Details: [governance/agent-workflow.md](governance/agent-workflow.md).

## For the student and ChatGPT: how to use this repository

1. Read [governance/teaching-charter.md](governance/teaching-charter.md) and
   [governance/assessment-standard.md](governance/assessment-standard.md).
2. Read [governance/director-decisions.md](governance/director-decisions.md): what the director has decided and what is still open.
3. Open [progress/current-session.md](progress/current-session.md). It is the resume pack, names the authoritative branch, and says exactly
   where to start; it also has a suggested opening message for a new ChatGPT conversation.
4. Find syllabus items in [curriculum/syllabus.md](curriculum/syllabus.md) (readable) or
   [curriculum/coverage.yaml](curriculum/coverage.yaml) (the register). Items have ids such as `IA-GP-004`. The descriptions are the
   librarian's own summaries, not Cambridge's wording; the Schedules are the authority.
5. Pick readings from [curriculum/reading-map.md](curriculum/reading-map.md) (alignment evidence in
   [curriculum/reading-alignment.md](curriculum/reading-alignment.md)). Prerequisites and the suggested order are guidance, not gates:
   see [curriculum/dependencies.md](curriculum/dependencies.md). Optional Harvard Math 55 enrichment is in
   [curriculum/enrichment.md](curriculum/enrichment.md).
6. After a session, ChatGPT writes a checkpoint using
   [progress/sessions/TEMPLATE.md](progress/sessions/TEMPLATE.md), recording the exact question, the student's actual response and questions, what the tutor explained, the hints given and the tutor's
   evaluation. Claude Code files it (saved records are append-only), refreshes the resume pack, applies any **Assessment Decision** issued by ChatGPT, then commits and **pushes, confirming the push succeeded**.

Mastery is recorded as an evidence-based level, never as a percentage:
`unassessed` -> `familiarity` -> `understanding` -> `independent-competence` -> `durable-mastery`. A level above
`unassessed` needs real student work as evidence **and** the assessor's authorisation. Discussion, reading,
an AI-supplied proof, a followed worked example, or an exercise done with substantial hints never suffices. Durable mastery needs
fresh independent work at least 28 days later on genuinely new material. The validator checks that these records are well formed;
it cannot judge mathematical correctness or authenticate a decision ([governance/assessment-standard.md](governance/assessment-standard.md)).

## Layout

```text
curriculum/   syllabus register, readable syllabus, reading map and alignment, enrichment map, dependencies and sequence
progress/     mastery state, weaknesses, the resume pack, and archived session records
studies/      one folder per Part IA course, for the student's work and evidence
assessments/  diagnostic (not started) and an index of the Tripos papers (pointers only)
references/   bibliography (four statuses per resource), source register, outstanding verification tasks
governance/   teaching charter, assessment standard, agent workflow
reports/      review reports and open decisions
reviews/      independent review findings (Codex)
scripts/      validate.py and selftest.py (standard library only) and a PDF text helper
```

## Checking the repository

```text
python3 scripts/validate.py
```

It checks unique ids, valid references between registers, that no mastery claim lacks evidence and
authorisation, that every bibliography entry marked verified cites a source, and that internal links work.
With `--schedules-text` (see [scripts/extract_pdf_text.py](scripts/extract_pdf_text.py)) and a local copy of the Cambridge Schedules it also
checks each item's fingerprint against the original and reports any unmapped syllabus text; adding `--guide-text` scans the repository for
copied Cambridge wording. `python3 scripts/selftest.py` tests the validator itself with synthetic defects.

## Sources and copyright

The syllabus authority is the Cambridge *Schedules of Lecture Courses* (2026-27). This repository is public and Cambridge's text is copyright, so it
holds **original summaries, exact locators and fingerprints**, not Cambridge's wording; no textbook, examination paper or Cambridge PDF is stored (PDFs are
excluded by `.gitignore`). Details, and the position on material already published, are in
[references/source-register.md](references/source-register.md).
Because this repository is public, **do not put personal or sensitive information in the progress records.**
