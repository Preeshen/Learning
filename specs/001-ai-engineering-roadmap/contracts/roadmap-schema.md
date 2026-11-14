# Contract: `roadmap/roadmap.yaml`

**Feature**: 001-ai-engineering-roadmap | **Date**: 2026-11-14

The single source of truth for the programme. `roadmap/ROADMAP.md` is generated from this file and
must never be hand-edited. Entity field definitions live in [data-model.md](../data-model.md); this
contract fixes the on-disk shape and the validator rules.

## Shape

```yaml
version: 1
start_date: 2026-11-16
end_date: 2027-01-24
total_days: 70
weekday_hours: 4
weekend_hours: 6
primary_role: agentic-ai
secondary_role: fde

domains:
  applied-ai:
    name: Applied AI Engineering
    directory: applied-ai
    target_days: 24
    min_depth: >-
      Build, evaluate and debug a tool-using agent and a retrieval pipeline end to end.
    supports_roles: [agentic-ai, fde, test-validation]
  # ... python, dsa, git, systems, ml

roles:
  agentic-ai:
    name: AI / Agentic AI Engineer
    tier: primary
    supporting_domains: [applied-ai, ml, python, systems]
  inference:
    name: Inference Engineer
    tier: remaining
    supporting_domains: [ml, python]
    evidence_required:
      - One artifact measuring inference latency and memory against a baseline
  # ... fde, ml-engineer, embedded-ml, test-validation

topics:
  sliding-window:
    name: Sliding window
    domain: dsa
    first_day: 8
    resurface_after: [7, 21]
    references:
      - title: "Longest Substring Without Repeating Characters"
        url: "https://leetcode.com/problems/longest-substring-without-repeating-characters/"
  # ... ~25 topics

weeks:
  - number: 1
    theme: "Python depth and DSA patterns I"
    domains: [python, dsa]
    outcome: "Typed, tested, packaged Python; arrays/hashing and two-pointer patterns solved cold."
    days:
      - id: 1
        date: 2026-11-16
        day_type: weekday
        objective: "Stand up the repo toolchain and complete the worked example day."
        domain: python
        topic: project-tooling
        artifact: python/project-tooling/env_report.py
        verification: "pytest python/project-tooling/ passes; roadmap validate exits 0"
        notes_topic: "Why a committed lockfile is the difference between reproducible and 'works here'"
        effort_hours: 4
        tier: primary
        priority: core
        gate:
          - "uv run roadmap validate exits 0"
          - "pytest python/project-tooling/ passes"
          - "python/project-tooling/NOTES.md modified in this commit"
        minimum_viable: "Toolchain installed and `roadmap today` runs; defer the notes."
      - id: 2
        # ...
    review:
      week: 1
      day: 7
      resolves: [arrays-hashing, two-pointers]
      procedure:
        - "Re-solve each topic in `resolves` from a blank file; record pass/fail."
        - "Run `roadmap review` and read the failed-gate report."
        - "Audit the week's commits against constitution Principles I-VII."
        - "Cut optional days from next week if behind; never carry a backlog."
      output_path: progress/reviews/week-01.md

milestones:
  - id: rag-service
    name: "Evaluated RAG service"
    after_day: 35
    prerequisite_days: [22, 24, 28, 31, 34]
    purpose: >-
      A deployable retrieval service with a real evaluation harness, demonstrating that
      retrieval quality is measured rather than asserted.
    demonstrates:
      - "Ingestion, chunking and retrieval over a non-trivial corpus"
      - "An evaluation set with recall and faithfulness reported against a baseline"
      - "Deployed behind an API with latency and cost instrumented"
    supports_roles: [agentic-ai, fde]
    external: true
    record_path: promoted/README.md
```

## Validator rules

`roadmap validate` implements these. Each returns a rule id, severity, and a message naming the
offending day or topic. Exit code 0 only when no `error`-severity rule fires.

| Rule | Severity | Check | Traces to |
|---|---|---|---|
| V-01 | error | `end_date` equals `start_date` + `total_days` − 1; all day `date` values derived consistently; `day_type` matches the weekday/weekend of `date` | FR-001 |
| V-02 | error | Every DayEntry has a non-empty `artifact`, `verification`, `notes_topic`, `minimum_viable`, and ≥1 `gate` entry | FR-004, FR-005, SC-002, Principle I |
| V-03 | error | Exactly 10 weeks, exactly 7 days each, day ids contiguous 1..70 with no gaps or duplicates | FR-002, FR-003 |
| V-04 | error | `effort_hours` ≤ 4 for `weekday`, ≤ 6 for `weekend` | FR-027 |
| V-05 | error | For any day with `from_scratch_of: N`, N < that day's id and N's topic matches | FR-010, Principle III |
| V-06 | error | If `measurement` present, all of `metric`/`baseline`/`results_path`/`method` are non-empty | FR-012, Principle V |
| V-07 | error | Every topic has ≥2 strictly increasing `resurface_after` intervals, and appears in ≥2 checkpoints' `resolves` | FR-014, FR-015, Principle VI |
| V-08 | error | No milestone references a path inside this repository other than its `record_path`; `external` is `true` | FR-021, Principle VII |
| V-09 | error | No day references a `topic`, `domain` or `tier` that is not declared | referential integrity |
| V-10 | error | All 6 domains and all 6 roles declared; exactly one `primary` and one `secondary` role | FR-008, FR-029 |
| V-11 | error | Every id in `prerequisites` is lower than the referencing day's id | FR-011 |
| V-12 | error | `language != python` requires `language_exception`; `offline: false` requires `offline_fallback` | FR-034, constitution Scope |
| V-13 | warn | No domain exceeds 40% of `total_days` | SC-003 |
| V-14 | warn | Sum of `effort_hours` where `priority == core` ≤ 272 | SC-009 |
| V-15 | warn | Each tier's day share within ±5 points of 60 / 25 / 15 | SC-012 |
| V-16 | warn | Every `remaining`-tier role's `evidence_required` items are each satisfied by ≥1 day | FR-032, SC-013 |
| V-17 | warn | ≥3 milestones declared | FR-019 |

Severity rationale: structural and constitutional breaches are `error` because they make the
roadmap wrong. The budget and distribution rules are `warn` because they are targets the learner may
knowingly trade against during a re-plan — but `roadmap validate --strict` promotes all warnings to
errors, and the weekly review runs it in strict mode.

## Compatibility

`version: 1`. A breaking change to this shape increments it and requires a migration note in
`roadmap/ROADMAP.md`'s header. The loader refuses an unknown version rather than guessing.
