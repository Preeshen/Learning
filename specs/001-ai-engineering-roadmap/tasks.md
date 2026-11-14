---

description: "Task list for AI Engineering Learning Roadmap"
---

# Tasks: AI Engineering Learning Roadmap

**Input**: Design documents from `D:\Learning\specs\001-ai-engineering-roadmap\`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Included. The spec's own success criteria (SC-001..SC-013) are mechanically checked by
`roadmap validate` and `pytest`, and `plan.md`'s Technical Context names `pytest` as the testing
tool, so contract/unit tests for the tooling are in scope. Tests for individual *learning* days
(`test_*.py` beside each topic) are produced day-by-day during the programme, not by this feature —
only Day 1's worked example is built here, per plan.md's Summary.

**Organization**: Tasks are grouped by user story (US1–US5, matching spec.md's priorities P1/P1/P2/P2/P3/P3)
so each story is independently testable per its spec.md "Independent Test" statement.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: US1–US5, matching spec.md
- File paths are repository-relative under `D:\Learning\`

## Path Conventions

Single project, flat domain directories at repo root (plan.md's Structure Decision). Tooling lives
under `tools/roadmap_cli/`; tooling tests under `tests/`; learning-artifact tests colocated with
their topic.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Make the repository buildable and the CLI installable before any content or logic exists.

- [ ] T001 Create `pyproject.toml` at repo root declaring the project, Python 3.12 requirement, and
  optional-dependency groups `python`, `dsa`, `ml` (numpy, torch, scikit-learn), `applied-ai`
  (an LLM SDK, `fastapi`, `uvicorn`, the Claude Agent SDK, an MCP package), per plan.md's Primary
  Dependencies and Technical Context
- [ ] T002 [P] Add core dependencies to `pyproject.toml`: `pytest`, `PyYAML`, `jsonschema`, `typer`,
  `rich`
- [ ] T003 [P] Create `D:\Learning\.gitignore` covering `.venv/`, `__pycache__/`, `*.pyc` if not
  already present
- [ ] T004 Run `uv sync` to create `.venv`, generate and commit `uv.lock` (quickstart.md Bootstrap
  step; FR-034/R-005 reproducibility)
- [ ] T005 [P] Create empty domain directories with a stub `NOTES.md` index each:
  `python/NOTES.md`, `dsa/NOTES.md`, `git/NOTES.md`, `systems/NOTES.md`, `ml/NOTES.md`,
  `applied-ai/NOTES.md` (plan.md Project Structure)
- [ ] T006 [P] Create `applied-ai/_fixtures/` (recorded LLM request/response pairs directory,
  empty placeholder `.gitkeep`) and `applied-ai/_mcp/` (shared MCP server/client stub directory,
  empty placeholder `.gitkeep`) per plan.md
- [ ] T007 [P] Create `promoted/README.md` with the pointer-record format (project name, source
  learnings, link) that `roadmap/roadmap.yaml` milestones will point at — FR-022, data-model.md §8
  `record_path`
- [ ] T008 [P] Create root `README.md`: what this repo is, how to run `roadmap today` to start a
  session (plan.md Project Structure)

**Checkpoint**: `uv sync` succeeds; repository has its skeleton; nothing runnable yet.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: The roadmap data, its schema, and the CLI's read path. Every user story depends on
`roadmap today` being able to load and print a day, so this phase builds that shared core.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [ ] T009 [P] Define `tools/roadmap_cli/models.py` — dataclasses mirroring data-model.md entities:
  `Roadmap`, `Week`, `DayEntry`, `Domain`, `Topic`, `Measurement`, `ReviewCheckpoint`,
  `PromotionMilestone`, `RoleTarget`, `DayProgress`. Every field listed in data-model.md §1–§10 must
  appear with its stated type and required/optional flag, including `DayEntry.serving` (optional
  string, must equal `"fastapi"` when set — FR-030a) and `DayEntry.generic_concept` (optional
  string, required whenever the day's tooling references Claude Code skills, the Claude Agent SDK,
  or MCP — FR-030b)
- [ ] T010 [P] Create the JSON Schema (or equivalent `jsonschema`-checkable schema) for
  `roadmap.yaml` in `tools/roadmap_cli/schema/roadmap.schema.json`, encoding every field and
  required/optional rule from contracts/roadmap-schema.md's Shape section, including `serving`
  restricted to the single enum value `fastapi` and `generic_concept` as a free-form string
- [ ] T011 [P] Create the JSON Schema for `progress.yaml` in
  `tools/roadmap_cli/schema/progress.schema.json`, encoding progress-schema.md's shape: `version`,
  `roadmap_version`, `started`, and `entries[]` with `day`, `status` (enum `pending`\|`complete`\|
  `skipped`\|`carried`), `date`, `commit`, `gate_passed`, `journal_ref`, `resolve_results[]`
- [ ] T012 `tools/roadmap_cli/loader.py`: load `roadmap/roadmap.yaml`, validate against the
  JSON Schema from T010, raise a clear error naming the expected path if missing and the supported
  version if `version` is unrecognized (cli-contract.md Error handling table), and construct the
  `Roadmap` dataclass tree from T009 (depends on T009, T010)
- [ ] T013 `tools/roadmap_cli/loader.py`: add `load_progress()` — load `progress/progress.yaml`
  (treat a missing file as a fresh start per cli-contract.md's Error handling table: exit `0`,
  `today` returns day 1), validate against T011's schema, construct `DayProgress` list (depends on
  T009, T011)
- [ ] T014 `tools/roadmap_cli/validate.py`: implement validator rules V-01 through V-12 from
  contracts/roadmap-schema.md (date arithmetic, required fields non-empty, week/day structure,
  effort budget, scratch-before-library ordering, measurement completeness, re-surfacing intervals,
  milestone external-only, referential integrity, domain/role completeness, prerequisite ordering,
  language/offline exception requirements) — each returning `(rule_id, severity, message)` (depends
  on T009)
- [ ] T015 `tools/roadmap_cli/validate.py`: implement validator rules V-13 through V-17 (domain
  ≤40% share, core-effort ≤272h, tier split ±5 points, remaining-tier evidence satisfied, ≥3
  milestones), V-18/V-19 (`serving` must be exactly `"fastapi"` when set — FR-030a; any day
  whose topic/tooling references Claude Code skills, Agent SDK, or MCP has a non-empty
  `generic_concept` — FR-030b), and V-20 (every milestone's `purpose`, `demonstrates`, and
  `supports_roles` are each non-empty — FR-020) (depends on T014)
- [ ] T016 `tools/roadmap_cli/validate.py`: implement progress-file rules P-01 through P-07 from
  contracts/progress-schema.md (day uniqueness/no-gaps, complete requires commit+gate_passed,
  commit resolves to a real git commit, journal_ref resolves, day references a real DayEntry,
  stale-carried warning, double-fail-resolve escalation trigger) (depends on T013)
- [ ] T017 `tools/roadmap_cli/validate.py`: implement journal rules J-01 through J-03
  (journal_ref resolves to exactly one `journal.md` anchor, ascending day order, complete entries
  should contain Built/Broke/Non-obvious) (depends on T016)
- [ ] T018 `tools/roadmap_cli/cli.py`: scaffold the `typer` app with the 7 commands as stubs
  (`today`, `check`, `complete`, `review`, `validate`, `coverage`, `render`), global `--json` flag
  convention and exit-code convention (0 success / 1 rule failure / 2 usage-or-load error) from
  cli-contract.md's Global conventions (depends on T012, T013)
- [ ] T019 `tools/roadmap_cli/cli.py`: implement `roadmap validate [--strict] [--json]` — run every
  rule from T014–T017, print the summary line (`N days · N weeks · N topics · N milestones`), exit
  `0` only when no `error`-severity rule fires (or, under `--strict`, no `warn` either), matching
  cli-contract.md's example output exactly in shape (depends on T014, T015, T016, T017, T018)
- [ ] T020 [P] `tests/test_validate.py`: unit tests for each validator rule V-01..V-21 and P-01..P-07,
  J-01..J-03 — one fixture YAML per rule that is known to pass and one known to fail, asserting the
  rule id and severity reported (depends on T019)
- [ ] T021 Create `roadmap/roadmap.yaml` with the full 70-day, 10-week structure: all 6 domains,
  all 6 roles (one `primary`: `agentic-ai`, one `secondary`: `fde`), ~25 topics each with
  `resurface_after` of ≥2 strictly increasing intervals, 10 weeks each with exactly 7 days and one
  `ReviewCheckpoint`, the 3 locked `PromotionMilestone` entries from
  contracts/roadmap-schema.md — `code-review-triage-agent` (agentic-ai/fde), `inference-gateway`
  (fde/inference), and `compression-validation-suite` (ml-engineer/inference/embedded-ml/
  test-validation) — each with non-empty `purpose`/`demonstrates`/`supports_roles` (FR-020/V-20),
  and an `interview_imminent_plan` naming a minimum drill-topic subset per role (FR-026/V-21) —
  content per plan.md's Day allocation and Role-tier split tables
  (24 applied-ai / 16 dsa / 14 ml / 8 python / 6 systems / 2 git; 42 primary / 18 secondary / 10
  remaining), each day entry carrying every required DayEntry field from data-model.md §3, at least
  one `serving: fastapi` day within applied-ai per FR-030a, and at least one day per applied-ai
  topic that uses Claude Code skills/Agent SDK/MCP carrying a non-empty `generic_concept` per
  FR-030b (depends on T010; this is the large content-authoring task the rest of Phase 2 exists to
  validate)
- [ ] T022 Run `uv run roadmap validate --strict` against T021's `roadmap.yaml` and fix every
  reported error/warning until exit code `0` (depends on T019, T021)

**Checkpoint**: `roadmap validate --strict` exits `0` against a complete, schema-valid
`roadmap.yaml`. Foundation ready — user stories can now build on top of real data.

---

## Phase 3: User Story 1 - Know and ship today's deliverable (Priority: P1) 🎯 MVP

**Goal**: The learner opens one place and within two minutes knows today's objective, artifact,
verification, and note topic, with an explicit pass/fail gate, a named prerequisite, and a
minimum-viable fallback.

**Independent Test**: Pick any day number, hand it to the learner cold — they begin within two
minutes without asking a question, and can state unambiguously whether the day passed its gate.

### Tests for User Story 1

- [ ] T023 [P] [US1] `tests/test_cli.py`: contract test for `roadmap today` (no args) — asserts the
  printed card contains day number, date, day_type, effort, tier, domain, topic, objective,
  artifact path, verification string, notes topic, the gate checklist, the "IF SHORT ON TIME"
  minimum-viable line, and named prerequisites with their status, matching cli-contract.md's
  example shape; runtime under 1 second (SC-001)
- [ ] T024 [P] [US1] `tests/test_cli.py`: contract test for `roadmap today <day>` and
  `roadmap today --json` (structured output) and `roadmap today --next N`
- [ ] T025 [P] [US1] `tests/test_cli.py`: contract test for `roadmap check [<day>] [--json]` —
  asserts all 5 gate items (artifact exists, tests pass, notes modified, measurement committed,
  commit exists) are each reported PASS/FAIL, exit `0` only when all pass
- [ ] T026 [P] [US1] `tests/test_cli.py`: contract test for `roadmap complete` — refuses
  (exit `1`) when `roadmap check` fails and `--force` is not given; with `--force` records the day
  with `gate_passed: false` rather than omitting the failure; refuses with exit `2` on a dirty
  working tree; requires `--built`/`--broke`/`--learned`
- [ ] T027 [P] [US1] `tests/test_cli.py`: integration test reproducing quickstart.md's S-4 "complete
  a real day end to end" scenario against Day 1's worked example (T030) using a temp git repo
  fixture: `today` → build → `pytest` → commit → `check` all green → `complete` → `today` advances
  to day 2

### Implementation for User Story 1

- [ ] T028 [US1] `tools/roadmap_cli/cli.py`: implement `roadmap today` — derive current day as the
  lowest `progress.yaml` entry not `complete`/`skipped` (falling back to day 1 if `progress.yaml`
  is absent), render the day card via `rich` matching cli-contract.md's example, including
  prerequisite status lookup and due-for-resolve topics (depends on T012, T013, T018)
- [ ] T029 [US1] `tools/roadmap_cli/cli.py`: implement `roadmap check` — run the 5-item gate
  (artifact file exists, its `pytest` path passes, `NOTES.md` modified since the day's
  `from_scratch_of`/prior commit, `measurement.results_path` exists when `measurement` is set,
  current commit exists) and print PASS/FAIL per item (depends on T012, T018)
- [ ] T030 [US1] `tools/roadmap_cli/cli.py`: implement `roadmap complete` — run `check` internally,
  refuse without `--force` on failure, resolve current commit SHA via `git rev-parse HEAD`, refuse
  with exit `2` if the tree is dirty, append to `progress.yaml` and `journal.md` per
  progress-schema.md's shape, support `--skip`, `--carry`, `--resolve topic:pass|fail` (repeatable)
  (depends on T013, T018, T029)
- [ ] T031 [US1] Build Day 1's worked example end to end: `python/project-tooling/env_report.py`
  (the artifact), `python/project-tooling/test_env_report.py`, `python/project-tooling/NOTES.md`,
  matching the Day 1 entry already authored in `roadmap.yaml` (T021) — this is the one day of
  learning content this feature delivers directly, per plan.md's Summary
- [ ] T032 [US1] Commit Day 1's artifact and record it complete via `roadmap complete`, proving
  `progress/progress.yaml` and `progress/journal.md` are created correctly from a real commit

**Checkpoint**: User Story 1 fully functional — `today`/`check`/`complete` work end to end against
real Day 1 content, independently testable per spec.md's Independent Test.

---

## Phase 4: User Story 2 - Retain what was learned (Priority: P2)

**Goal**: Completed topics resurface at increasing intervals for from-blank-file re-solve; failed
re-solves are re-queued rather than dropped; revision outranks new material when time is short.

**Independent Test**: Run the review slots in isolation against already-completed topics and
confirm each resurfaces at least twice at increasing intervals with a recorded pass/fail outcome.

### Tests for User Story 2

- [ ] T033 [P] [US2] `tests/test_cli.py`: contract test that `roadmap today`'s "DUE FOR RESOLVE"
  line lists exactly the topics whose `first_day + resurface_after[n]` has been reached by the
  completed-day count (data-model.md "Topics due" derived value)
- [ ] T034 [P] [US2] `tests/test_validate.py`: test that V-07 fails when a topic has fewer than 2
  strictly increasing `resurface_after` intervals, and when a topic never appears twice across all
  checkpoints' `resolves`
- [ ] T035 [P] [US2] `tests/test_cli.py`: test that recording a resolve as `fail` via
  `roadmap complete --resolve <topic>:fail` is visible in `coverage`/`review` output, and that a
  second consecutive `fail` for the same topic triggers the P-07 escalation warning

### Implementation for User Story 2

- [ ] T036 [US2] `tools/roadmap_cli/loader.py` / `cli.py`: implement the "topics due" derived value
  (data-model.md's Derived values table) and surface it in `roadmap today`'s output (depends on
  T028, T033)
- [ ] T037 [US2] `tools/roadmap_cli/cli.py`: extend `roadmap complete --resolve` handling to persist
  `resolve_results` entries and implement the P-07 escalation check (two `passed: false` results for
  the same topic) as a `roadmap validate` warning, per FR-016 (depends on T030, T016)
- [ ] T038 [US2] Author the FR-018 priority rule ("revision outranks new material when time is
  short") as explicit text in each week's `review.procedure` step list in `roadmap.yaml`, and assert
  it via a `tests/test_validate.py` check that every week's procedure contains this rule

**Checkpoint**: Re-solve scheduling, recording, and escalation work independently of US1's day-ahead
flow; US1 + US2 together still pass all US1 tests.

---

## Phase 5: User Story 3 - Weekly review and honest re-planning (Priority: P2)

**Goal**: Once a week, produce a factual record of what shipped/slipped/violated, with a named
cut-first rule and stretch material for being ahead.

**Independent Test**: Simulate a week with 3 of 7 days missed, run the review, and confirm it
produces a re-planned next week with named cuts and no accumulated backlog.

### Tests for User Story 3

- [ ] T039 [P] [US3] `tests/test_cli.py`: contract test for `roadmap review [N]` — asserts
  `progress/reviews/week-NN.md` is written with the Generated section pre-filled (completion
  counts, core effort used vs. budget, failed gates, topics due, role readiness) matching
  progress-schema.md's example, and that re-running without `--regenerate` refuses to overwrite
- [ ] T040 [P] [US3] `tests/test_cli.py`: contract test for `roadmap coverage [--role <id>]
  [--json]` — asserts the per-role table (tier, days, done, readiness %) and domain-share line match
  cli-contract.md's example shape
- [ ] T041 [P] [US3] Integration test reproducing spec.md US3's scenario: a fixture `progress.yaml`
  with 3 of 7 days of a week marked `skipped`, run `roadmap review`, assert the output names the
  skipped days and that FR-007's "optional cut first, core never cut" rule is reflected in the
  Generated section (no silent backlog — SC-006)

### Implementation for User Story 3

- [ ] T042 [US3] `tools/roadmap_cli/cli.py`: implement `roadmap review` — compute the Generated
  section's facts (completion counts, effort vs. budget, failed `roadmap check` gates for the week,
  topics due, role readiness) and write `progress/reviews/week-NN.md` with the judgement sections
  left blank, refusing to overwrite without `--regenerate` (depends on T028, T029, T036)
- [ ] T043 [US3] `tools/roadmap_cli/coverage.py` + `cli.py` wiring: implement `roadmap coverage` —
  per-role day counts, completed counts, readiness %, and domain-share line, using the derived
  values from data-model.md (depends on T012, T013)
- [ ] T044 [US3] Encode FR-017's recovery rules (missed day, 3 consecutive missed days, full missed
  week, named re-entry point) as explicit text that `roadmap review`'s Generated section surfaces
  when it detects the condition (e.g., "3+ consecutive skipped days detected — re-entry point: day
  N") (depends on T042)
- [ ] T044a [US3] Author FR-026's interview-imminent re-prioritisation path: add an
  `interview_imminent_plan` section to `roadmap/roadmap.yaml` naming the minimum subset of material
  to drill per role (referencing existing topic ids), and surface it from `roadmap today` (and
  `roadmap review`) when invoked with a `--days-until-interview N` flag — print only the drill
  subset for that many remaining days instead of the next-day card (depends on T021, T028)
- [ ] T044b [P] [US3] `tests/test_cli.py`: contract test that `roadmap today --days-until-interview
  N` returns the FR-026 drill subset rather than the normal next-day card, and
  `tests/test_validate.py` test that `roadmap.yaml` without an `interview_imminent_plan` section
  fails a new validator rule V-21 (depends on T044a)

**Checkpoint**: Weekly review and coverage reporting work independently; combined with US1/US2,
the full daily-plus-weekly loop is testable end to end.

---

## Phase 6: User Story 4 - Know when a topic is ready to become a CV project (Priority: P3)

**Goal**: At defined milestones, the learner sees the project's purpose, minimum capability, and
target roles, is directed to build it in a separate repository, and records only a pointer here.

**Independent Test**: Reach a promotion milestone with its prerequisite days complete and confirm
it states purpose, capability, roles, and the pointer record — with no project code in this repo.

### Tests for User Story 4

- [ ] T045 [P] [US4] `tests/test_validate.py`: test V-08 — a milestone referencing any path inside
  this repository other than `record_path`, or with `external` not `true`, fails validation
- [ ] T046 [P] [US4] `tests/test_cli.py`: test that `roadmap today` (or a dedicated milestone view)
  reports, for a milestone whose `prerequisite_days` are not all `complete`, which specific days are
  still unmet (spec.md US4 Acceptance Scenario 3)

### Implementation for User Story 4

- [ ] T047 [US4] `tools/roadmap_cli/cli.py`: add milestone status reporting — when a milestone's
  `prerequisite_days` are all `complete`, surface it (in `roadmap today`'s "all 70 days done"
  summary per cli-contract.md, and in `roadmap coverage`) with purpose, `demonstrates`, and
  `supports_roles`; when not all complete, list the unmet days (depends on T028, T043)
- [ ] T048 [US4] Verify `promoted/README.md` (T007) documents the exact pointer-record fields
  (project name, source learnings, link) that a learner fills in after building a milestone project
  externally, matching data-model.md §8's `record_path` contract

**Checkpoint**: Milestone readiness and the separate-repo boundary are enforced and visible,
independent of the daily/weekly stories.

---

## Phase 7: User Story 5 - Map progress to target roles (Priority: P3)

**Goal**: The learner sees each target role's coverage proportion from completed days, and the
domains weighted toward the primary role appear earlier and in greater depth.

**Independent Test**: With an arbitrary subset of days marked complete, the mapping identifies
which roles are adequately covered and which are not.

### Tests for User Story 5

- [ ] T049 [P] [US5] `tests/test_cli.py`: test that `roadmap coverage --role <id>` lists the
  specific days supporting that role and the correct readiness percentage for a fixture with a known
  subset of days complete
- [ ] T050 [P] [US5] `tests/test_validate.py`: test V-15 (tier split ±5 points of 60/25/15) and that
  the Week 1 theme in `roadmap.yaml` advances `python`/`dsa` (front-loaded per FR-033) ahead of
  lower-priority domains, confirming sequencing favors the primary role early (FR-031's "appear
  earlier and in greater depth")

### Implementation for User Story 5

- [ ] T051 [US5] `tools/roadmap_cli/coverage.py`: implement the `--role` detail view (list of
  specific supporting days and per-day done/pending status) building on T043 (depends on T043)
- [ ] T052 [US5] Cross-check `roadmap.yaml`'s week ordering against FR-029/FR-031 (AI/Agentic AI
  primary, FDE secondary, remaining four at minimum depth, Python depth front-loaded per FR-033) and
  adjust week themes/domain assignments in `roadmap.yaml` if the authored order does not already
  reflect this priority (depends on T021)

**Checkpoint**: All five user stories independently functional and testable.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Make the generated views and offline guarantees hold, and close out quickstart.md's
remaining validation scenarios.

- [ ] T053 [P] `tools/roadmap_cli/render.py` + `cli.py` wiring: implement `roadmap render
  [--check]` — generate `roadmap/ROADMAP.md` and `roadmap/milestones.md` from `roadmap.yaml`;
  `--check` exits `1` if the generated files are stale or hand-edited (quickstart.md S-6)
- [ ] T054 [P] `tools/bench/harness.py`: shared timing/memory/baseline-comparison helper that any
  day's `benchmarks.json` measurement can call into (plan.md Project Structure; Measurement entity
  needs a consistent `method` across weeks per data-model.md §6)
- [ ] T055 [P] `tools/hooks/pre-commit`: optional pre-commit hook that runs `roadmap check` in warn
  mode (never blocks) per plan.md's Post-Design Constitution Re-Check note on R-010
- [ ] T056 [P] Record at least one `applied-ai/_fixtures/` request/response pair and wire a sample
  offline-backed test in `tests/` proving an Applied AI day's test suite passes fully disconnected
  from the network (quickstart.md S-7, FR-034)
- [ ] T057 Run quickstart.md's S-1 through S-7 validation scenarios against the finished repository
  end to end and fix any discrepancy from the documented expected output
- [ ] T058 [P] Update root `README.md` with the final bootstrap + first-session instructions
  verified against quickstart.md's Bootstrap section

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Setup — BLOCKS all user stories (T021's full
  `roadmap.yaml` authoring is the long pole here)
- **User Stories (Phase 3–7)**: All depend on Foundational completion
  - US1 (Phase 3) has no dependency on US2–US5
  - US2 (Phase 4) depends on US1's `today`/`complete` (T028, T030) existing
  - US3 (Phase 5) depends on US1's `check` (T029) and US2's topics-due logic (T036)
  - US4 (Phase 6) depends on US1's `today` (T028) and US3's `coverage` (T043)
  - US5 (Phase 7) depends on US3's `coverage` (T043)
- **Polish (Phase 8)**: Depends on all desired user stories being complete

### Parallel Opportunities

- All `[P]`-marked Setup tasks (T002, T003, T005–T008)
- T009, T010, T011 (independent files) in Foundational
- Within each story's "Tests for User Story N" block, all `[P]` tasks target different test
  functions/files and can run in parallel
- Different user stories cannot truly run in parallel by different people until Foundational
  (through T022) is done, since T021's `roadmap.yaml` is a shared prerequisite for all CLI commands

---

## Parallel Example: Foundational Phase

```bash
# Launch independent schema/model files together:
Task: "Define dataclasses in tools/roadmap_cli/models.py"
Task: "Create roadmap.schema.json in tools/roadmap_cli/schema/"
Task: "Create progress.schema.json in tools/roadmap_cli/schema/"
```

## Parallel Example: User Story 1 tests

```bash
Task: "Contract test for roadmap today in tests/test_cli.py"
Task: "Contract test for roadmap check in tests/test_cli.py"
Task: "Contract test for roadmap complete in tests/test_cli.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1: Setup
2. Phase 2: Foundational — including authoring the full 70-day `roadmap.yaml` (T021), since US1's
   "pick any day number" independent test requires real data, not a 1-day fixture
3. Phase 3: User Story 1
4. **STOP and VALIDATE**: run quickstart.md's S-1 through S-4 — this alone delivers a growing body
   of committed artifacts (plan.md's MVP framing)

### Incremental Delivery

1. Setup + Foundational → roadmap data exists and validates clean
2. Add US1 → `today`/`check`/`complete` work, Day 1 built → MVP
3. Add US2 → spaced-repetition resurfacing and escalation
4. Add US3 → weekly review and coverage reporting
5. Add US4 → milestone readiness and the separate-repo boundary
6. Add US5 → role-targeted coverage detail
7. Polish → `render`, bench harness, pre-commit hook, offline proof, full quickstart pass

---

## Notes

- `[P]` tasks = different files, no dependencies
- T021 (authoring all 70 days in `roadmap.yaml`) is the single largest task in this plan by effort;
  it is Foundational rather than per-story because every user story's CLI command reads the same
  file
- Only Day 1's learning content (T031) is built by this feature; days 2–70's actual artifacts are
  produced during the programme itself, per plan.md's Summary
- Verify tests fail before implementing their corresponding command
- Commit after each task or logical group
- Stop at any checkpoint to validate a story independently
