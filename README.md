# hall_of_scholars

A long-term programme of rigorous mathematical study based on the **University of Cambridge Mathematical
Tripos Part IA**, aimed at a firm foundation in pure and applied mathematics and, later, computational
mathematical physics. It prizes mathematical maturity, independent proof construction and durable
understanding over speed or syllabus completion.

**Status: Curriculum Baseline v1 - awaiting independent review and curriculum-director approval.** Nothing has
been taught, assessed or marked as mastered. See
[reports/baseline-v1-review-report.md](reports/baseline-v1-review-report.md).

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
2. Open [progress/current-session.md](progress/current-session.md). It is the resume pack and says exactly
   where to start; it also has a suggested opening message for a new ChatGPT conversation.
3. Find syllabus items in [curriculum/syllabus.md](curriculum/syllabus.md) (readable) or
   [curriculum/coverage.yaml](curriculum/coverage.yaml) (the register). Items have ids such as `IA-GP-004`.
4. Pick readings from [curriculum/reading-map.md](curriculum/reading-map.md). Optional Harvard Math 55
   enrichment is in [curriculum/enrichment.md](curriculum/enrichment.md).
5. After a session, ChatGPT writes a checkpoint using
   [progress/sessions/TEMPLATE.md](progress/sessions/TEMPLATE.md). Claude Code files it, refreshes the
   resume pack, and applies any **Assessment Decision** issued by ChatGPT.

Mastery is recorded as an evidence-based level, never as a percentage:
`unassessed` -> `familiarity` -> `understanding` -> `independent-competence` -> `durable-mastery`. A level above
`unassessed` needs real student work as evidence **and** the assessor's authorisation. Discussion, reading,
an AI-supplied proof, a followed worked example, or an exercise done with substantial hints never suffices.

## Layout

```text
curriculum/   syllabus register, readable syllabus, reading map, enrichment map, dependencies and sequence
progress/     mastery state, weaknesses, the resume pack, and archived session records
studies/      one folder per Part IA course, for the student's work and evidence
assessments/  diagnostic (not started) and an index of the Tripos papers (pointers only)
references/   bibliography and source register, with verification status
governance/   teaching charter, assessment standard, agent workflow
reports/      review reports and open decisions
reviews/      independent review findings (Codex)
scripts/      validate.py (standard library only) and a PDF text helper
```

## Checking the repository

```text
python3 scripts/validate.py
```

It checks unique ids, valid references between registers, that no mastery claim lacks evidence and
authorisation, that every bibliography entry marked verified cites a source, and that internal links work.
With `--schedules-text` (see [scripts/extract_pdf_text.py](scripts/extract_pdf_text.py)) it also confirms
every syllabus statement against the Cambridge Schedules text and reports any unmapped syllabus text.

## Sources and copyright

The syllabus authority is the Cambridge *Schedules of Lecture Courses* (2026-27). No textbook and no
examination paper is stored here; PDFs are excluded by `.gitignore`. The register does quote syllabus
statements; the licensing question that raises is recorded in
[references/source-register.md](references/source-register.md) and awaits the director's decision.
Because this repository is public, **do not put personal or sensitive information in the progress records.**
