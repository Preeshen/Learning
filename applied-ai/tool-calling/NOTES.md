# Tool-calling loops

**Problem it solves**: letting a model take actions (query a weather API, run a linter, call a
search index) rather than only producing text, and surviving the model occasionally producing a
tool call the code can't execute as-is.

**Mechanism**: the loop sends the model a conversation, parses its tool-call response, executes
the named tool, and feeds the result back in as a new user turn — repeating until the model
produces a final answer instead of another tool call. Offline by default: `FixtureModel` replays
a scripted sequence of responses instead of calling a live API (R-006), which is what makes this
day's tests fully deterministic and network-free.

**Failure modes**: a malformed tool call (invalid JSON arguments, a hallucinated tool name) is not
a transient failure — simply re-sending the same conversation reproduces the same bad output,
because nothing about the conversation changed. The fix is to tell the model what broke
(`"Error: ... Fix the arguments and retry."`) before retrying, which is a different conversation
and therefore has a real chance of a different (correct) response. `benchmarks.json` proves this
is not just a plausible story: with retry, 20/20 scripted trials succeeded; without retry, only
12/20 did — the exact 8-trial gap matches the fraction of trials that were scripted to start with
a malformed call.

**Trade-offs**: capping retries at `max_retries=2` trades "never give up" for "fail predictably and
say why" — an unbounded retry loop against a model that's genuinely confused about the tool's
schema would burn cost and latency with no better odds of success, since the underlying confusion
(not transient noise) doesn't go away just because you ask again a third time.
