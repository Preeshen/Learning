# Phase 0 Research: AI Engineering Learning Roadmap

**Feature**: 001-ai-engineering-roadmap | **Date**: 2026-11-14

This document resolves every unknown in the plan's Technical Context. Each decision records what
was chosen, why, and what was rejected.

---

## R-001: How is the roadmap represented?

**Decision**: A machine-readable `roadmap/roadmap.yaml` is the single source of truth. A
human-readable `roadmap/ROADMAP.md` is **generated** from it and committed alongside. Neither is
edited by hand except `roadmap.yaml`.

**Rationale**: Five success criteria are counting criteria — SC-002 (100% of days have an artifact
and a gate), SC-003 (no domain exceeds 40% of days), SC-009 (core-day effort ≤ 272 h), SC-012
(role-tier split within 5 points of 60/25/15), SC-013 (each minimum-depth role has ≥1 artifact).
Verifying these by hand across 70 entries is guaranteed to drift the moment the roadmap is edited.
A structured source makes them a single validator run. The generated Markdown preserves SC-001
(open one place, start in under two minutes) and SC-010 (an independent reader can determine
progress) without asking the learner to read YAML daily.

**Alternatives considered**:

- *Markdown only, counts maintained by hand*. Rejected: the counting criteria become unverifiable
  after the first edit, and the plan's own quality gates would be unenforceable.
- *JSON source*. Rejected: no comments, and the roadmap carries substantial prose (objectives,
  gates, fallbacks) that is painful to author and diff in JSON.
- *A database or spreadsheet*. Rejected: not diffable, not reviewable in a pull request, and
  breaks the constitution's "runnable from a clean checkout" constraint.

---

## R-002: How does the learner find today's work in under two minutes?

**Decision**: A small CLI, `roadmap today`, prints the current day entry — objective, artifact,
verification, note topic, effort, prerequisites, and the minimum-viable fallback. The current day
is derived from `progress/progress.yaml` (the first day not marked `complete`), **not** from the
calendar date.

**Rationale**: Deriving "today" from the calendar breaks the instant the learner misses a day, which
FR-017 assumes will happen. Deriving it from progress makes a gap self-healing: after any absence
the next incomplete day is the re-entry point, satisfying FR-017's "named re-entry point" without
any renumbering. This directly serves SC-001.

**Alternatives considered**:

- *Calendar-date lookup*. Rejected: one missed day desynchronises the whole programme and the
  learner must manually re-map day numbers to dates forever after.
- *Scroll the Markdown file*. Rejected: a 70-entry file makes "where am I" a search task; measured
  against SC-001's two-minute budget this is the main thing that would blow it.

---

## R-003: How is progress recorded?

**Decision**: Two files. `progress/progress.yaml` holds machine-readable status per day
(`pending` | `complete` | `skipped` | `carried`) with the date and the commit SHA. `progress/journal.md`
is an append-only prose log, one entry per day: what was built, what broke, the non-obvious concept.

**Rationale**: FR-023 requires both a status and a one-paragraph log entry, and these have different
natures. Status is queried (by the CLI, by the validator, by the role-coverage report) and belongs in
structured data; the prose is written once and read by a human and belongs in Markdown. Splitting
them keeps the YAML small enough to stay diff-readable. Recording the commit SHA makes Principle I
("terminates in committed code") mechanically checkable rather than self-reported.

**Alternatives considered**:

- *Derive status entirely from git history*. Rejected: attractive, but it cannot distinguish a day
  deliberately skipped from one not yet reached, which FR-023 requires. Retained as a
  cross-check in the validator instead.
- *A single combined file*. Rejected: prose and status in one YAML produces unreadable diffs.
- *Checkboxes in the generated ROADMAP.md*. Rejected: the generated file would then be hand-edited,
  and the next regeneration destroys the record.

---

## R-004: How is spaced repetition scheduled?

**Decision**: Each topic declares `resurface_after: [N, M]` — intervals in **completed programme
days**, not calendar days. The validator enforces FR-015 (at least two re-surfacings at increasing
intervals). Review checkpoints pull the due topics. Default intervals are 7 and 21 completed days.

**Rationale**: Calendar-based intervals decay into meaninglessness after any gap — a topic "due in
7 days" when the learner took a fortnight off is simultaneously overdue and untouched. Anchoring to
completed days keeps the interval proportional to actual practice, which is what retention tracks.
7/21 approximates the standard expanding-interval shape without importing a full SRS algorithm.

**Alternatives considered**:

- *A real SRS algorithm (SM-2, FSRS)*. Rejected as disproportionate: it optimises per-item recall
  probability over hundreds of items, where this programme has roughly 25 topics and a fixed
  10-week horizon. The weekly checkpoint is a coarse enough instrument that the extra precision
  would not change which topics get re-solved.
- *Calendar-day intervals*. Rejected per the rationale above.
- *Ad-hoc "revisit when it feels shaky"*. Rejected: Principle VI exists precisely because
  self-assessed familiarity is a poor predictor of retrieval under pressure.

---

## R-005: Python environment and dependency management

**Decision**: A single root `pyproject.toml` managed by `uv`, with one optional-dependency group per
domain (`dsa`, `ml`, `applied-ai`, `systems`). `uv.lock` is committed. Python is pinned to 3.12.

**Rationale**: The constitution requires dependencies pinned per topic and reproducibility from the
repository alone. A committed `uv.lock` pins every transitive version exactly, and dependency groups
mean a learner working on DSA does not need to install PyTorch. `uv` is already present on this
machine (0.13.8) and resolves in seconds, which matters when the environment is rebuilt often.

**Alternatives considered**:

- *A separate virtualenv per topic directory*. Rejected: ~25 environments to maintain, no shared
  lock, and cross-topic imports (a DSA utility used in an ML day) become impossible.
- *requirements.txt + pip*. Rejected: pip alone does not produce a transitive lock, so "pinned" would
  be aspirational.
- *conda*. Rejected: not installed here, and heavier than this project needs.

**Environment note**: Python 3.12.3 is installed but reachable only via the `py` launcher — plain
`python` is not on PATH. `uv` creates and manages its own `.venv`, which sidesteps this entirely, so
no PATH change is required. Documented in quickstart.md.

---

## R-006: How do Applied AI days run without a paid API budget?

**Decision**: A thin provider-agnostic client wrapper with three interchangeable backends:

1. **Fixture backend** (default, offline): replays recorded request/response pairs from
   `applied-ai/_fixtures/`. Every Applied AI day's completion gate is reachable on this backend
   alone.
2. **Local backend**: a small instruction-tuned model run locally for days that need genuinely
   novel generations.
3. **Live backend**: a real provider API, used only when the learner opts in.

Fixtures are committed; API keys never are, and are read from environment variables only.

**Rationale**: This is the sharpest tension in the whole plan. FR-034 and the constitution forbid
requiring paid infrastructure, while the primary target role is the one domain where real API
behaviour — latency, cost, rate limits, refusals, tool-call malformation — is the actual subject
matter. Making the fixture backend the default satisfies the constraint absolutely: every gate is
reachable at zero cost. Making the live backend a first-class opt-in means the learner can spend a
small amount where it buys real signal, without the roadmap ever depending on it.

**Honest limitation**: fixtures teach the *shape* of LLM engineering — retries, parsing, evaluation
harnesses, cost accounting — but they cannot teach what a model actually does to a prompt the
learner just invented. Roughly 8–10 of the 24 Applied AI days are materially better with live
access. See the Decision Required note in plan.md; this is the learner's call, not the plan's.

**Alternatives considered**:

- *Require a live API from day one*. Rejected: violates FR-034 and the constitution outright.
- *Local model only*. Rejected: a small local model's tool-calling and instruction-following are
  weak enough that agentic days would teach workarounds for the model rather than the pattern.
- *Mock returning canned strings*. Rejected: too fake to exercise parsing, retries, or evaluation —
  the learner would be testing their own mock.

---

## R-007: DSA problem sourcing

**Decision**: The roadmap names problems by **title and canonical public URL** and groups them by
interview-frequency-weighted pattern. No problem statements, editorials, or third-party solutions
are reproduced in this repository. Only the learner's own solutions and their own tests are
committed.

**Rationale**: FR-035 forbids committing licensed course material, and problem statements on the
major judges are copyrighted. Titles and links are sufficient for the learner to find the problem,
and the committed artifact — their solution plus their tests plus their stated complexity — is the
part that has learning value anyway.

**Patterns, in the order the roadmap introduces them** (ordered by observed large-tech interview
frequency, highest first): arrays and hashing; two pointers; sliding window; binary search; stack and
monotonic stack; linked list; trees and BFS/DFS; heap and top-K; graphs including topological sort;
backtracking; dynamic programming (1-D then 2-D); intervals; tries; bit manipulation.

**Alternatives considered**:

- *Copy problem text locally for offline work*. Rejected: a licensing violation and a direct breach
  of FR-035.
- *Order by data-structure taxonomy*. Rejected by FR-009, and it is pedagogically worse — patterns
  transfer across problems in a way that "chapter on heaps" does not.

---

## R-008: What counts as a measurement, mechanically?

**Decision**: A shared `tools/bench` helper provides timing, memory, and comparison-against-baseline
utilities and writes results to a per-topic `benchmarks.json`. Days that make a performance,
accuracy, latency, or memory claim must commit that file, and the validator fails any such day whose
entry declares a measurement but whose artifact path has no results file.

**Rationale**: Principle V and FR-012 both require measurement, but "measured it" is unfalsifiable
without a committed artifact. Making the result a file turns the principle into a gate the validator
can check. A shared helper keeps the measurement methodology consistent so numbers from week 2 and
week 9 are comparable.

**Alternatives considered**:

- *Numbers written into NOTES.md prose*. Rejected: not machine-checkable, and not reproducible.
- *pytest-benchmark*. Reasonable, and may be adopted later for micro-benchmarks, but it does not
  cover accuracy or memory claims, so a thin shared helper is needed regardless.

---

## R-009: Testing approach

**Decision**: `pytest`, with tests colocated in each topic directory as `test_*.py` rather than
centralised under `tests/`. A root `tests/` holds only the tests for the roadmap tooling itself.

**Rationale**: A topic directory should be a self-contained, independently runnable unit — the
learner opens one folder and everything for that topic is in it, which is what makes a day's work
reviewable and a `NOTES.md` meaningful. Centralising tests would split every day's artifact across
two trees. The tooling is different: it is infrastructure, not learning material, and its tests
belong with other infrastructure.

**Alternatives considered**:

- *All tests under a root `tests/` mirror tree*. Rejected per the rationale above.
- *unittest*. Rejected: pytest's assertion rewriting and fixtures are both lighter to write and
  themselves part of the Python-depth material in FR-033.

---

## R-010: Enforcing the daily quality gate

**Decision**: A `roadmap check` command runs the day's completion gate: artifact path exists,
declared tests pass, `NOTES.md` for the topic has been modified, a measurement file exists if the
day declares one, and the working tree has a commit. Installed as an **optional** git pre-commit
hook that warns rather than blocks.

**Rationale**: The constitution's five-item day-completion gate is currently prose the learner must
self-assess. Mechanising it removes the judgement call that SC-002 and the plan's own gate depend
on. It warns rather than blocks because blocking a commit on an incomplete day would push the
learner toward `--no-verify` or, worse, toward not committing exploratory work — which Principle VII
explicitly wants kept.

**Alternatives considered**:

- *Blocking pre-commit hook*. Rejected per the rationale above.
- *CI on push*. Deferred, not rejected: valuable once the repo is on GitHub, but it cannot gate a
  local day's completion in the moment, which is when the signal is useful.
- *Pure self-assessment*. Rejected: it is what the constitution already asks for, and the whole
  point of this feature is to make it mechanical.

---

## Resolved unknowns summary

| Unknown from Technical Context | Resolved by |
|---|---|
| Roadmap storage format | R-001 — YAML source, generated Markdown |
| Daily navigation mechanism | R-002 — `roadmap today`, progress-derived |
| Progress record format | R-003 — split YAML status + Markdown journal |
| Spaced-repetition scheduling | R-004 — completed-day intervals, 7/21 default |
| Dependency management | R-005 — uv, single pyproject, committed lock |
| LLM access without paid infra | R-006 — fixture / local / live backends |
| DSA problem sourcing | R-007 — titles and links only, pattern-ordered |
| Measurement mechanism | R-008 — shared bench helper, committed results |
| Testing framework and layout | R-009 — pytest, colocated per topic |
| Quality-gate enforcement | R-010 — `roadmap check`, warning pre-commit hook |

No `NEEDS CLARIFICATION` items remain.
