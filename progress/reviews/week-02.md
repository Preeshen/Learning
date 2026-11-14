# Week 02 Review — 2026-11-23 to 2026-11-29

## Generated

- Completed: 6 / 7 · Skipped: 0 · Carried: 0
- Core effort used: 26 h of 32 h budgeted
- Topics due for re-solve: sliding-window, two-pointers

## Re-solve results

| Topic | Result | Action |
|---|---|---|
| sliding-window | PASS | Next re-surface day 26 (first_day 5 + 21) |
| two-pointers | PASS | Second occurrence — now resurfaced twice per FR-015; keep in rotation at wider intervals going forward |

## Constitution audit

Principles I-VII checked against this week's commits:

- **I (Learn By Building)**: every day 8-13 artifact is runnable and tested; 48/48 CLI tests and
  the full domain test suite (122 tests) pass. No violation.
- **II (Daily Deliverable)**: all 7 days attempted, no silent gaps. No violation.
- **III (From Scratch Before Framework)**: day 10's gradient descent (scratch) preceded its
  scikit-learn comparison in the same day, consistent with Principle III's pairing requirement.
- **IV (Explain It Back)**: every day's `NOTES.md` was written and committed.
- **V (Measure, Don't Guess)**: day 10 (accuracy vs scikit-learn) and day 12 (cost/latency vs
  day-6 baseline) each committed a `benchmarks.json`.
- **VI (Spaced Repetition)**: both resolves ran from a blank file and passed; two-pointers has
  now resurfaced twice (days 7 and 14), satisfying FR-015 for that topic.
- **VII (Playground Here, Production Elsewhere)**: no production-project code built here.

**Tooling finding, not a content violation**: discovered during day 7 that the `roadmap check`
gate unconditionally failed every review day, because the generic check assumed a code artifact
(ran pytest against a nonexistent test dir, looked for a sibling NOTES.md that review days don't
have). Fixed in commit 9a67c33 before completing day 7 — flagging here since it affected every
week's review day, not just this one, and is exactly the kind of tooling bug the weekly audit
exists to catch.

## Next week

On schedule, slightly under core budget (26h used of 32h for completed core days). No cuts
needed. Week 3 continues DSA (heaps, backtracking per the locked 18-day pattern plan) alongside
Applied AI's retrieval subtopics.
