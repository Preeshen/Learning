# Quickstart: AI Engineering Learning Roadmap

**Feature**: 001-ai-engineering-roadmap | **Date**: 2026-11-14

How to bootstrap the repository and prove the feature works end to end. This is a validation and
run guide — implementation belongs in `tasks.md`.

## Prerequisites

Already present on this machine (verified 2026-11-14):

| Tool | Version | Note |
|---|---|---|
| Python | 3.12.3 | Reachable via the `py` launcher. Plain `python` is **not** on PATH |
| uv | 0.13.8 | Creates and manages `.venv`, so the PATH gap does not matter |
| git | 2.47.0 | Repository already initialised, remote `origin` set |

No GPU, no cloud account, and no API key are required. Every scenario below runs offline.

## Bootstrap

```powershell
cd D:\Learning
uv sync                      # creates .venv, installs tooling, installs `roadmap` editable
uv run roadmap --version     # confirms the CLI is wired up
```

If `uv sync` is the first command ever run here, it also writes `uv.lock`. Commit it — a lockfile
that is not committed is not a lockfile.

## Validation scenarios

Each scenario proves a specific spec requirement. Run them in order; each is independent once
bootstrap is done.

### S-1 — The roadmap is structurally sound

*Proves: FR-001 to FR-012, SC-002, SC-003, and the validator rules in
[contracts/roadmap-schema.md](./contracts/roadmap-schema.md).*

```powershell
uv run roadmap validate --strict
```

**Expect**: exit code `0`, and a summary line reading `133 days · 19 weeks · 114 topics ·
3 milestones`. Any error names the offending day and the rule id.

This single command is the mechanical form of five of the spec's success criteria. If it passes,
every day has an artifact and a gate, no domain exceeds 40% of the programme, core effort fits the
646-hour core cap, the role split is within tolerance, and every minimum-depth role has its evidence
day.

### S-2 — Today's work is findable in under two minutes

*Proves: SC-001, FR-004, FR-017's re-entry behaviour.*

```powershell
uv run roadmap today
```

**Expect**: the day card from [contracts/cli-contract.md](./contracts/cli-contract.md) — objective,
artifact path, verification, notes topic, gate checklist, and the short-session fallback — printed
in under a second.

**Then test the gap-recovery property**, which is the part most likely to be got wrong:

```powershell
uv run roadmap today --json | ConvertFrom-Json | Select-Object day
# mark a day skipped, then ask again
uv run roadmap complete --skip --built "-" --broke "-" --learned "Travelling"
uv run roadmap today --json | ConvertFrom-Json | Select-Object day
```

**Expect**: the second call returns the *next* day, not a date-derived one. Nothing renumbers.
This is what makes a missed week harmless.

### S-3 — A day cannot be marked complete dishonestly

*Proves: Principle I and II made mechanical; P-02 and P-03 in
[contracts/progress-schema.md](./contracts/progress-schema.md).*

```powershell
uv run roadmap check            # against an unfinished day
uv run roadmap complete --built "x" --broke "y" --learned "z"
```

**Expect**: `check` lists which of the five gate items failed; `complete` **refuses** with exit `1`
and does not write to `progress.yaml`. With `--force` it records the day but writes
`gate_passed: false` rather than hiding the failure.

### S-4 — Complete a real day end to end

*Proves: the whole daily loop — the feature's primary user story.*

```powershell
uv run roadmap today                    # read the objective
# ... build the artifact, write the test, write NOTES.md ...
uv run pytest python/project-tooling/   # the day's own verification
git add -A; git commit -m "python: day 1 - project tooling and env report"
uv run roadmap check                    # all five green
uv run roadmap complete --built "Env report script with a committed lockfile" `
                        --broke "uv sync picked a stale cache; --refresh fixed it" `
                        --learned "A lockfile not committed is not a lockfile"
uv run roadmap today                    # now shows day 2
```

**Expect**: `progress.yaml` gains a `complete` entry carrying the real commit SHA;
`journal.md` gains a dated section with the three prose fields; `roadmap today` advances.

### S-5 — The weekly review is generated from facts, not memory

*Proves: FR-013, FR-014, FR-023, Principle VI.*

```powershell
uv run roadmap review
uv run roadmap coverage
```

**Expect**: `progress/reviews/week-01.md` written with completion counts, effort against budget,
failed gates, and topics due for re-solve already filled in. The judgement sections — re-solve
results, constitution audit, next week's cuts — are left blank for the learner.

`coverage` prints the per-role readiness table, so a role with zero evidence is visible rather than
assumed.

### S-6 — The generated roadmap cannot silently drift

*Proves: R-001's single-source-of-truth property.*

```powershell
uv run roadmap render --check
```

**Expect**: exit `0` when `ROADMAP.md` matches `roadmap.yaml`. Hand-edit `ROADMAP.md`, re-run, and
expect exit `1`. This is the guard against the one failure mode that would quietly desynchronise
what the learner reads each morning from the actual source of truth.

### S-7 — Everything works offline

*Proves: FR-034, and R-006's fixture backend.*

Disconnect from the network, then:

```powershell
uv run roadmap validate --strict
uv run roadmap today
uv run pytest applied-ai/
```

**Expect**: all pass. Applied AI tests run against recorded fixtures in `applied-ai/_fixtures/`.
No command reaches the network, and no API key is read.

## Acceptance

The feature is working when S-1 through S-7 all pass and the repository contains:

- `roadmap/roadmap.yaml` with 70 validated day entries
- `roadmap/ROADMAP.md` generated and in sync
- `progress/progress.yaml` and `progress/journal.md` with at least day 1 recorded
- A working `roadmap` CLI with all seven commands
- Six domain directories present, each with a `NOTES.md` index
- `promoted/README.md` ready to receive pointer records
- `uv.lock` committed

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `python: not found` | Plain `python` is not on PATH here | Use `uv run ...`, which uses `.venv` directly |
| `roadmap: command not found` | Editable install not done | `uv sync` |
| `validate` reports V-01 date errors | `start_date` edited without re-deriving day dates | Re-run `roadmap render` after any date change |
| `complete` exits 2 on a clean day | Working tree dirty — untracked files count | `git status`, commit or stash first |
| `render --check` fails unexpectedly | `ROADMAP.md` was hand-edited | Never edit it; re-run `roadmap render` |
