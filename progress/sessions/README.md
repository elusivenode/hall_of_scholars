# Session records

Each study session leaves one record here, named `YYYY-MM-DD-NN-<slug>.md` (NN is the session number for that day), written
from [TEMPLATE.md](TEMPLATE.md). No session has taken place yet, so there are no records.

**Why these records matter.** They are the durable history of the programme: the exact questions, the student's actual
responses, the hints given, the tutor's evaluations and the decisions taken. They are how a new ChatGPT conversation recovers the
exact academic context, and the evidence behind any later mastery judgement.

**Immutability.** A saved record is append-only.

- Never edit committed text. Add a dated entry under "Addenda (append only)" that says what is being corrected and why.
- `scripts/validate.py` checks that the text first committed is still the start of each file (it uses git history).
- `progress/current-session.md` is rewritten after every session as the resume pack, but because every checkpoint is saved here
  first, nothing is lost.

**Never fabricate.** If the exact wording or the student's response was not captured, write "not captured". Do not rebuild a
record from a general description of a conversation.

**Close the session properly.** Commit the record, the resume pack and any evidence files, **push, and confirm the push succeeded**; a fresh conversation can see only what has been pushed. If the
push fails, say so: the session is not safely recorded.

See [governance/agent-workflow.md](../../governance/agent-workflow.md) for the end-of-session routine and
[governance/session-continuity-test.md](../../governance/session-continuity-test.md) for the end-to-end test of this mechanism.
