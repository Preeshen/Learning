# LLM cost & latency budgeting

**Problem it solves**: knowing what a tool-calling loop actually costs and how long it takes,
rather than just that it produces a correct answer eventually.

**Mechanism**: wrap each `generate` call with timing and a rough token estimate (4 characters per
token — good enough to budget against, not accurate enough to bill against), then roll those
per-call records up into total cost and p50/p95 latency across a batch of requests. Wrapping
rather than modifying `run_tool_loop` keeps the loop itself free of a tracking dependency.

**Failure modes**: this day's own `benchmarks.json` shows p50/p95 latency of ~0ms — that's honest,
not broken: `FixtureModel` returns scripted responses instantly with no network round-trip, so
there is no real latency to measure yet. That's the fixture-backed days' known limitation flagged
in `plan.md`'s Decision Required section — this day proves the *instrumentation* works, but the
actual latency numbers will only become meaningful once this tracker runs against a live API
client with a real network hop.

**Trade-offs**: character-based token estimation is deliberately approximate — using the real
tokenizer would be more accurate but adds a dependency and ties this day to one provider's
vocabulary, which doesn't matter for budgeting-order-of-magnitude decisions but would matter for
an actual billing reconciliation.
