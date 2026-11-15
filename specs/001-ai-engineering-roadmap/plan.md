# Implementation Plan: AI Engineering Learning Roadmap

**Branch**: `001-ai-engineering-roadmap` (feature directory; git branch is `main`) | **Date**: 2026-11-14 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-ai-engineering-roadmap/spec.md`

## Summary

Build the scaffolding that makes a 19-week, 133-day AI engineering learning programme executable and
verifiable: a structured roadmap, a progress record, and a small CLI that answers "what do I build
today?" in seconds and mechanically checks whether a day was actually completed.

The approach is a machine-readable `roadmap/roadmap.yaml` as single source of truth, from which a
human-readable `ROADMAP.md` is generated, paired with a `roadmap` CLI (`today`, `check`, `complete`,
`review`, `validate`, `coverage`, `render`). Five of the spec's thirteen success criteria are counting
criteria across 70 entries; making the roadmap data rather than prose turns them into one validator
run instead of a manual audit that drifts on first edit.

The learning content itself — six domain directories, each day's artifact, notes, tests, and
measurements — is produced day by day **during** the programme, not by this feature. This feature
delivers the roadmap, the tooling, the empty domain structure, and the first day's worked example.

## Technical Context

**Language/Version**: Python 3.12.3 (installed; reachable via the `py` launcher — plain `python` is
not on PATH, which `uv`'s managed `.venv` sidesteps)

**Primary Dependencies**: `uv` 0.13.8 (environment and lock), `pytest` (tests), `PyYAML` (roadmap and
progress parsing), `jsonschema` (contract validation), `typer` (CLI), `rich` (terminal rendering of
the day entry). Domain dependencies — NumPy, PyTorch, scikit-learn, an LLM SDK, `fastapi` +
`uvicorn` (FR-030a serving days), the Claude Agent SDK and an MCP server/client package
(FR-030b) — are declared as optional groups and installed only when the relevant domain's days
begin.

**Storage**: Plain files in the repository. `roadmap/roadmap.yaml` (source of truth),
`progress/progress.yaml` (status), `progress/journal.md` (prose log), per-topic `benchmarks.json`
(measurements). No database.

**Testing**: `pytest`. Tooling tests under root `tests/`; learning-artifact tests colocated in each
topic directory as `test_*.py` (R-009).

**Target Platform**: Windows 11 local development, with no platform-specific dependencies. Path
handling via `pathlib` so the repository also runs on Linux and macOS.

**Project Type**: CLI tool plus structured content repository. Single project, no client/server
split.

**Performance Goals**: `roadmap today` returns in under 1 second — it is run at the start of every
session and must never be the reason a session stalls. `roadmap validate` completes in under 5
seconds across all 70 entries so it can run in a pre-commit hook.

**Constraints**: Must run offline with no paid infrastructure (FR-034). No secrets, API keys,
proprietary datasets, or licensed course material committed (FR-035). Every artifact reproducible
from a clean checkout. No GPU assumed.

**Scale/Scope**: 133 day entries across 19 weeks and 7 domains, 114 topics, 19 weekly review
checkpoints, 3 promotion milestones, 6 role-coverage mappings. The CLI is roughly 7 commands over
~1,400 lines. The programme budget is 760 hours.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

Gates derived from constitution v1.1.0, principles I–VIII. Re-verified after the 133-day restructure (2026-11-15).

| # | Principle | Gate | Pre-Phase 0 | Post-Phase 1 |
|---|---|---|---|---|
| I | Learn By Building | Every day entry terminates in a committed, runnable artifact; no entry may have an empty `artifact` field | PASS — enforced by schema `required` and by `roadmap validate` | PASS — `contracts/roadmap-schema.md` makes `artifact` required; validator rule V-02 |
| II | Daily Deliverable | A per-day record exists with status and a prose log; skipped days are recorded explicitly, never omitted | PASS — `progress.yaml` + `journal.md` (R-003) | PASS — `skipped` is an explicit status in `contracts/progress-schema.md`; validator rule V-09 forbids gaps |
| III | From Scratch Before Framework | For any concept with both, the from-scratch day precedes the framework day | PASS — `from_scratch_of` (same topic) and `rebuilds_topic` (cross-topic) on day entries | PASS — V-05 covers same-topic pairs; **V-25** covers cross-topic pairs and is what actually enforces this: 5 days declare `rebuilds_topic` (LangGraph and LangChain rebuild `react-loop-scratch`, PyTorch rebuilds `neural-net-scratch`, KV caching rebuilds `transformers-attention-scratch`). V-05 alone evaluated 0 days after the restructure, which is why V-25 exists |
| IV | Explain It Back | Every day names a `notes_topic`; the day's check verifies `NOTES.md` carries all eleven required sections | PASS — required field | PASS — `roadmap check`'s `notes complete` item reports n/11 and names what is missing; a non-empty stub no longer passes |
| V | Measure, Don't Guess | Days claiming performance/accuracy/latency/memory declare a measurement and a baseline | PASS — `measurement` block with required `baseline` | PASS — validator rule V-06; `roadmap check` step 4 |
| VI | Spaced Repetition Over Coverage | Every topic schedules ≥2 re-surfacings at increasing intervals | PASS — `resurface_after` on topics (R-004) | PASS — validator rule V-07 |
| VII | Playground Here, Production Elsewhere | No milestone **and no day entry** schedules project implementation inside this repo; promoted projects recorded as pointers only | PASS — milestones carry no day entries | PASS — V-08 covers milestone definitions and **V-22** covers day entries. V-08 alone passed while four days were building projects, which is why V-22 exists |
| VIII | Progressive Assistance (NON-NEGOTIABLE) | Code is never ghostwritten; assistance escalates explain → hint → typed skeleton → debug → reference solution, and a ghostwritten artifact is reverted | PARTIAL — see below | **PARTIAL, and deliberately so.** Mechanised: `roadmap check`'s `implementation written` item fails a day whose artifact still contains a stub marker, so a day cannot be completed on the handed-over skeleton; and the skeleton-first workflow is the authored shape of every day's starting artifact. **Not mechanised: authorship itself.** No check can prove who typed a line, and pretending otherwise would be worse than naming the gap. Authorship is human-verified in the weekly review, whose procedure audits Principles I–VIII |

**Scope & Domain constraints**

| Constraint | Gate | Status |
|---|---|---|
| Python primary | Non-Python days must state a reason | PASS — `language_exception` field, required when `language != "python"` |
| Dependencies pinned, reproducible | Committed `uv.lock` | PASS (R-005) |
| No secrets or licensed material | DSA problems referenced by title and URL only; keys from env only | PASS (R-006, R-007) |
| No paid infrastructure | Every gate reachable on the offline fixture backend | PASS (R-006) — with the limitation recorded under Decision Required |
| FastAPI required for served artifacts (FR-030a) | Any day wrapping an LLM call, agent, or model as a service uses FastAPI; `roadmap-schema.md` tags these days `serving: fastapi` | PASS — enforced by schema field, not a new day count |
| Claude tooling secondary to generic agentic patterns (FR-030b) | Claude Code skills / Agent SDK / MCP days carry a `generic_concept` field naming the transferable pattern being practiced; validator rejects a day where this field is empty | PASS — no increase to the 24 Applied AI days in the allocation table below |

**Result**: All gates pass. One item is flagged for the learner's decision rather than as a
violation — see Decision Required below.

## Decision Required (not a blocker)

R-006 resolves the "no paid infrastructure" constraint by making an offline fixture backend the
default, so every Applied AI day is completable at zero cost. That satisfies the constitution
honestly, but it is worth stating plainly what it costs: roughly 8–10 of the 24 Applied AI days —
prompt iteration, agent failure modes, refusal and malformed-tool-call handling — teach materially
less against replayed fixtures than against a live model, because the thing being learned is how a
real model responds to a prompt the learner just invented.

A small live-API budget (on the order of $10–20 across ten weeks, given that these are short
prompts and the learner controls the loop) would remove that gap for the primary target role. The
plan does not assume it, nothing breaks without it, and no gate depends on it. Flagging it now so
the choice is deliberate rather than discovered in week 6.

## Project Structure

### Documentation (this feature)

```text
specs/001-ai-engineering-roadmap/
├── plan.md              # This file
├── spec.md              # Feature specification
├── research.md          # Phase 0 output — 10 resolved decisions
├── data-model.md        # Phase 1 output — 9 entities
├── quickstart.md        # Phase 1 output — validation guide
├── checklists/
│   └── requirements.md  # Spec quality checklist (16/16)
├── contracts/           # Phase 1 output
│   ├── roadmap-schema.md
│   ├── progress-schema.md
│   └── cli-contract.md
└── tasks.md             # Phase 2 output (/speckit-tasks — NOT created here)
```

### Source Code (repository root)

```text
D:\Learning\
├── pyproject.toml            # Single project, optional-dependency group per domain
├── uv.lock                   # Committed; pins every transitive version
├── README.md                 # Entry point: what this repo is, how to start a day
│
├── roadmap/
│   ├── roadmap.yaml          # SOURCE OF TRUTH — 133 days, 19 weeks, topics, milestones
│   ├── ROADMAP.md            # Generated from roadmap.yaml; never hand-edited
│   └── milestones.md         # Generated; the 3 promotion milestones in detail
│
├── progress/
│   ├── progress.yaml         # Machine-readable status per day + commit SHA
│   ├── journal.md            # Append-only prose log, one entry per day
│   └── reviews/              # One file per weekly review checkpoint
│       └── week-01.md
│
├── tools/
│   ├── roadmap_cli/          # today, check, complete, review, validate, coverage, render
│   │   ├── __init__.py
│   │   ├── cli.py
│   │   ├── models.py         # Dataclasses mirroring data-model.md
│   │   ├── loader.py         # YAML load + schema validation
│   │   ├── validate.py       # Rules V-01..V-12
│   │   ├── render.py         # roadmap.yaml -> ROADMAP.md
│   │   └── coverage.py       # Role-tier and domain reporting
│   ├── bench/                # Shared timing / memory / baseline-comparison helper
│   │   ├── __init__.py
│   │   └── harness.py
│   └── hooks/
│       └── pre-commit        # Optional, warns on an incomplete day
│
├── python/                   # Domain: Python depth (8 days)
├── dsa/                      # Domain: DSA by pattern (16 days)
├── git/                      # Domain: Git (2 days)
├── systems/                  # Domain: System design (6 days)
├── ml/                       # Domain: ML & DL (14 days)
├── applied-ai/               # Domain: Applied AI Engineering (24 days)
│   ├── _fixtures/            # Recorded LLM request/response pairs (offline default)
│   └── _mcp/                 # Shared MCP server/client stub used by the agentic-pattern days
│
├── promoted/
│   └── README.md             # Pointer records for CV projects built in OTHER repos
│
└── tests/                    # Tooling tests only; learning tests live beside their topic
    ├── test_validate.py
    ├── test_cli.py
    └── test_render.py
```

Each domain directory follows the same internal shape, created as its days arrive:

```text
<domain>/
├── NOTES.md                  # Domain-level index of topics
└── <topic-slug>/
    ├── NOTES.md              # Principle IV: the explain-it-back note
    ├── <artifact>.py         # Principle I: the runnable artifact
    ├── test_<artifact>.py    # Colocated test (R-009)
    └── benchmarks.json       # Principle V: present when the day claims a measurement
```

**Structure Decision**: Single project, flat domain directories at the repository root. Chosen over
a `src/` layout because the domain directories *are* the deliverable — the learner opens
`dsa/sliding-window/` directly, and burying that under `src/` adds a level of indirection that
serves packaging concerns this repository does not have. The only packaged code is `tools/`, which
is installed in editable mode so `roadmap` is on the path. Tests are split deliberately: tooling
tests centralised under `tests/`, learning tests colocated with their topic, per R-009.

### Day allocation

Realised distribution after the step-5 restructure (verified by `roadmap coverage`):

| Domain | Days | % of 133 | Cap (SC-003: ≤30%) |
|---|---|---|---|
| Applied AI Engineering | 38 | 29% | OK |
| System Design | 27 | 20% | OK |
| ML & DL (incl. MLOps and inference) | 24 | 18% | OK |
| Data Structures & Algorithms | 20 | 15% | OK (plus 1 h/day on all 133 days) |
| Python & software engineering | 12 | 9% | OK |
| Cloud & Infrastructure | 9 | 7% | OK |
| Git & Linux | 3 | 2% | OK |
| **Total** | **133** | **100%** | |

Role-tier split, satisfying FR-025 and SC-012 (target 60 / 25 / 15, tolerance ±5 points). Per
FR-025 a day serving several tiers counts toward the highest, so system design and Python depth
count as primary — an agentic-AI engineer needs both:

| Tier | Role | Days | % |
|---|---|---|---|
| Primary | AI / Agentic AI Engineer | 80 | 60% |
| Secondary | Forward Deployed Engineer | 31 | 23% |
| Remaining | ML/MLOps, Inference, AI Test Validation | 22 | 17% |

DSA is a continuous daily track rather than blocked days (FR-037): `dsa_hours: 1.0` on all 133
days, plus 20 dedicated pattern days interleaved so no run exceeds 2 consecutive.

## Phase 1 Design Artifacts

| Artifact | Contents |
|---|---|
| [data-model.md](./data-model.md) | 9 entities, their fields, relationships, validation rules, and the day-status state machine |
| [contracts/roadmap-schema.md](./contracts/roadmap-schema.md) | YAML schema for `roadmap.yaml` + validator rules V-01..V-24 |
| [contracts/progress-schema.md](./contracts/progress-schema.md) | YAML schema for `progress.yaml` and the journal entry format |
| [contracts/cli-contract.md](./contracts/cli-contract.md) | The 7 `roadmap` commands: arguments, output, exit codes |
| [quickstart.md](./quickstart.md) | Bootstrap, validation scenarios, and the end-to-end "complete a day" walkthrough |

## Complexity Tracking

> Filled because the Constitution Check's simplicity expectations deserve an explicit justification
> for the two places this plan is more than the minimum.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|---|---|---|
| A CLI and validator for what is "just a study plan" | SC-002, SC-003, SC-009, SC-012 and SC-013 are counting criteria over 70 entries; the constitution's day-completion gate is a five-item check run ~70 times. Both are mechanical work that humans do unreliably and abandon under time pressure — which is exactly when the programme most needs them. | A hand-maintained Markdown plan was rejected because the counting criteria become unverifiable after the first edit, and the completion gate degrades to self-assessment — the very failure mode Principles II and V exist to prevent. |
| A generated `ROADMAP.md` alongside the YAML source | SC-001 (start in under 2 minutes) and SC-010 (an outside reader can determine progress) both need readable prose; the counting criteria need structured data. One file cannot serve both without one of them degrading. | Keeping only the YAML was rejected because daily use would mean reading YAML, which works against SC-001. Keeping only Markdown reintroduces the counting problem. Generation keeps a single source of truth and costs one command. |

Three things were deliberately **not** built, to keep this proportionate: no database (plain files),
no web UI (the CLI is enough for one user), and no real spaced-repetition algorithm (R-004 — ~25
topics over a fixed 19-week horizon does not justify SM-2 or FSRS).

## Post-Design Constitution Re-Check

Re-evaluated after Phase 1. All seven principle gates still pass, now backed by named validator
rules rather than intent — see the Post-Phase 1 column in the Constitution Check table. The design
added no new dependency on paid infrastructure, no secret material, and no implementation work
inside this repository for the promotion milestones.

One design-stage observation worth recording: the `roadmap check` command (R-010) warns rather than
blocks. This is a deliberate softening of the constitution's day-completion gate, on the grounds
that a blocking hook pushes toward `--no-verify` or toward not committing exploratory work, which
Principle VII explicitly wants preserved. The gate remains enforced at the weekly review, where
`roadmap review` reports every day whose check did not pass.
