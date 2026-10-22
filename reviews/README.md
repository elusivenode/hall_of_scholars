# Independent reviews

Findings from the independent reviewer (Codex) go here, one file per review, for example
`baseline-v1-codex-review.md`. Reviews may also live on a branch named `review/<topic>-<YYYY-MM-DD>`.

The reviewer does **not** edit `curriculum/`, `progress/`, `governance/` or `references/`. Each finding names
the item id or file, the Cambridge source page where relevant, and the evidence (command output, quoted text).
Accepted findings are applied by Claude Code after the curriculum director agrees; see
[governance/agent-workflow.md](../governance/agent-workflow.md).

The brief for the Baseline v1 review is section 11 of
[reports/baseline-v1-review-report.md](../reports/baseline-v1-review-report.md).

## Index

| Review | Reviewer | Date | Branch reviewed | Status |
|---|---|---|---|---|
| [baseline-v1-r1-fable-review.md](baseline-v1-r1-fable-review.md) | An independent **Fable-model** session (a fresh agent given only the repository, the Cambridge PDFs and the review brief; it was not given the librarian's conclusions) | 22/10/2026 | `remediation/baseline-v1-director-feedback` at `93bb00f` | Filed **unchanged**. Findings not yet triaged by the director; none applied. |

This is **not** a Codex review. Codex could not be used (login blocked by the owner's settings), so the director should decide whether the Fable review
stands in for the Codex review described in [governance/agent-workflow.md](../governance/agent-workflow.md) or whether a Codex review is still wanted. A Fable
review is from the same vendor family as the librarian, so it is less independent than a Codex review would be.
