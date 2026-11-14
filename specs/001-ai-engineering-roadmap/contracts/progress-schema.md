# Contract: `progress/progress.yaml` and `progress/journal.md`

**Feature**: 001-ai-engineering-roadmap | **Date**: 2026-11-14

The progress record is deliberately split: structured status that tooling queries, and prose that a
human writes and reads. See [data-model.md](../data-model.md) §10 for field definitions and the
status state machine.

## `progress/progress.yaml`

```yaml
version: 1
roadmap_version: 1
started: 2026-11-16

entries:
  - day: 1
    status: complete
    date: 2026-11-16
    commit: 44735e1
    gate_passed: true
    journal_ref: "day-001"

  - day: 2
    status: complete
    date: 2026-11-17
    commit: a91c3f0
    gate_passed: true
    journal_ref: "day-002"
    resolve_results:
      - topic: arrays-hashing
        passed: false

  - day: 3
    status: skipped
    date: 2026-11-18
    journal_ref: "day-003"

  - day: 4
    status: carried
    date: 2026-11-19
    journal_ref: "day-004"
```

### Rules

| Rule | Severity | Check |
|---|---|---|
| P-01 | error | `day` values are unique and contain no gaps from 1 up to the highest recorded day |
| P-02 | error | `status: complete` requires both `commit` and `gate_passed: true` |
| P-03 | error | `commit` must resolve to a real commit in this repository |
| P-04 | error | Every entry has a `journal_ref` resolving to an anchor in `journal.md` |
| P-05 | error | `day` must reference a DayEntry that exists in `roadmap.yaml` |
| P-06 | warn | A `carried` entry older than the current day should have been resumed |
| P-07 | warn | A topic with two `passed: false` resolve results triggers the FR-016 escalation path |

P-02 is the mechanical form of Principle I: a day is not complete because the learner says so, but
because a commit exists and the gate passed. P-03 prevents the record from drifting into fiction.

### Status semantics

- `pending` — not yet attempted. The default for every unrecorded day.
- `complete` — terminal. Commit exists, gate passed.
- `skipped` — terminal. Deliberately not done, and **recorded** rather than omitted (Principle II).
  FR-017's recovery rules operate on these.
- `carried` — started, out of time, resumes next session. Returns to `pending` on resume.

The **current day** is derived, never stored: the lowest `day` whose status is neither `complete`
nor `skipped`. This is what makes any gap self-healing — after a two-week absence, `roadmap today`
simply returns the next unfinished day. No renumbering, no re-dating.

## `progress/journal.md`

Append-only. One section per attempted day, newest at the bottom. The anchor must match the
`journal_ref` in `progress.yaml`.

```markdown
## Day 002 — 2026-11-17 — Two pointers {#day-002}

**Status**: complete · **Commit**: a91c3f0 · **Domain**: dsa · **Effort**: 4.0 h

**Built**: Two-pointer solutions for 4 problems plus a shared test harness that
checks both correctness and asserted complexity on generated inputs.

**Broke**: The harness silently passed quadratic solutions — it timed the whole
suite rather than per-input, so growth was invisible. Rewrote it to time across
input sizes and fit the growth curve.

**Non-obvious**: Asserting complexity is a measurement, not a comment. Until the
harness timed across sizes, "O(n)" was a claim I had never tested.

**Re-solve**: arrays-hashing — FAILED, could not reconstruct the prefix-sum
variant from scratch. Re-queued.
```

### Rules

| Rule | Severity | Check |
|---|---|---|
| J-01 | error | Every `journal_ref` in `progress.yaml` resolves to exactly one anchor here |
| J-02 | error | Entries appear in ascending day order |
| J-03 | warn | A `complete` entry should contain all three of Built / Broke / Non-obvious |

The three required prose fields are exactly what constitution Principle II asks for. J-03 is a
`warn` rather than an `error` because an honest "nothing broke today" is a legitimate entry and the
tooling should not push the learner toward inventing a failure to satisfy a checker.

## `progress/reviews/week-NN.md`

Written once per week by `roadmap review`, then completed by hand.

```markdown
# Week 01 Review — 2026-11-16 to 2026-11-22

## Generated

- Completed: 6 / 7 · Skipped: 1 · Carried: 0
- Core effort used: 26.0 h of 32.0 h budgeted
- Failed gates: day 5 (no benchmarks.json committed)
- Topics due for re-solve: arrays-hashing, two-pointers
- Role readiness: agentic-ai 14% · fde 22% · others 0%

## Re-solve results

| Topic | Result | Action |
|---|---|---|
| arrays-hashing | FAIL | Re-queued for week 3 |
| two-pointers | PASS | Next re-surface week 4 |

## Constitution audit

Principles I-VII checked against this week's commits. Violations found: day 5 claimed a
latency improvement with no committed measurement (Principle V). Fixed in a follow-up commit.

## Next week

Cutting: day 11 (optional). Keeping all core days.
```

The generated section is produced by tooling so the facts are not self-reported; the re-solve
results, audit, and cuts are written by the learner, because those are judgements.
