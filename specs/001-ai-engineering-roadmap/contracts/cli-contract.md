# Contract: the `roadmap` CLI

**Feature**: 001-ai-engineering-roadmap | **Date**: 2026-11-14

Seven commands. Installed via `uv sync` in editable mode, invoked as `uv run roadmap <command>` or
plain `roadmap <command>` inside the activated environment.

Global conventions:

- Exit `0` on success, `1` on a rule failure, `2` on a usage or load error.
- `--json` on every read command emits machine-readable output for scripting and tests.
- All paths printed are repository-relative.
- No command writes to `roadmap/roadmap.yaml`. Only `render` writes `ROADMAP.md`; only `complete`
  and `review` write under `progress/`.

---

## `roadmap today`

The command the learner runs at the start of every session. Must answer "what do I build today?"
within SC-001's two-minute budget — target runtime under 1 second.

```text
$ roadmap today

  Day 12 of 70 · Tue 2026-11-27 · weekday · 4.0 h · core · tier: primary
  Domain: applied-ai · Topic: tool-calling

  OBJECTIVE
    Build a tool-calling loop that survives malformed arguments.

  ARTIFACT        applied-ai/tool-calling/loop.py
  VERIFICATION    pytest applied-ai/tool-calling/ — including 3 malformed-call cases
  NOTES           Why retrying a malformed tool call is not the same as retrying a failed one

  GATE
    [ ] pytest applied-ai/tool-calling/ passes
    [ ] applied-ai/tool-calling/NOTES.md modified
    [ ] benchmarks.json records retry counts against the no-retry baseline

  IF SHORT ON TIME
    Happy-path loop with one tool; defer malformed-argument handling to day 13.

  PREREQUISITES   day 9 (complete), day 11 (complete)
  DUE FOR RESOLVE arrays-hashing, binary-search
```

| Arg | Effect |
|---|---|
| *(none)* | The derived current day — lowest day not `complete` or `skipped` |
| `<day>` | Show a specific day instead |
| `--json` | Structured output |
| `--next N` | Show the next N days, for planning a weekend |

Exit `0` always, unless the roadmap fails to load. When all 70 days are done it prints the
programme summary and the promotion milestone status.

---

## `roadmap check`

Runs the current day's gate. Mechanises the constitution's five-item day-completion gate so it is
not a self-assessment.

```text
$ roadmap check

  Day 12 · applied-ai/tool-calling

  [PASS] artifact exists            applied-ai/tool-calling/loop.py
  [PASS] tests pass                 3 passed in 0.41s
  [FAIL] notes modified             applied-ai/tool-calling/NOTES.md unchanged since day 11
  [FAIL] measurement committed      benchmarks.json not found
  [PASS] working tree has a commit  a91c3f0

  2 of 5 checks failed — day not complete.
```

| Arg | Effect |
|---|---|
| `<day>` | Check a specific day |
| `--json` | Structured output |

Exit `0` when all checks pass, `1` otherwise. Used by the optional pre-commit hook in warn mode
(R-010) and by `roadmap review` to build the failed-gate report.

---

## `roadmap complete`

Records a day as done. Refuses to record an incomplete day, which is what keeps `progress.yaml`
honest.

```text
$ roadmap complete --built "Tool-calling loop with malformed-argument retry" \
                   --broke "Retry loop re-sent the same bad args; needed to reset the message" \
                   --learned "A malformed call is a prompt bug, not a transient failure"
```

Behaviour:

1. Runs `roadmap check`. If any check fails, refuses unless `--force` is given, and `--force`
   records `gate_passed: false` rather than hiding it.
2. Resolves the current commit SHA. Errors if the tree is dirty or has no commit for this day.
3. Appends an entry to `progress.yaml` and a section to `journal.md`.

| Arg | Required | Effect |
|---|---|---|
| `--built` / `--broke` / `--learned` | yes | The three journal fields (Principle II) |
| `--skip` | — | Record `skipped` instead, with a reason. Never silently omit a day |
| `--carry` | — | Record `carried` — started, out of time |
| `--resolve <topic>:<pass\|fail>` | — | Record a re-solve result, repeatable |
| `--force` | — | Record despite a failed gate, honestly flagged |

Exit `0` on record, `1` on refusal, `2` on a dirty tree.

---

## `roadmap review`

Generates the weekly checkpoint file, then stops — the judgement sections are the learner's to
write.

```text
$ roadmap review          # current week
$ roadmap review 3        # a specific week
```

Writes `progress/reviews/week-NN.md` pre-filled with the Generated section defined in
[progress-schema.md](./progress-schema.md): completion counts, effort used against budget, failed
gates, topics due for re-solve, and per-role readiness. Refuses to overwrite an existing review
without `--regenerate`.

Exit `0` on write, `1` if the week has no recorded days.

---

## `roadmap validate`

Runs rules V-01 to V-17 against `roadmap.yaml`, and P-01 to P-07 plus J-01 to J-03 against the
progress files.

```text
$ roadmap validate

  roadmap.yaml ................ 70 days · 10 weeks · 25 topics · 3 milestones
  [ERROR] V-02  day 34: `minimum_viable` is empty
  [WARN]  V-14  core effort 281.0 h exceeds the 272.0 h budget by 9.0 h
  [WARN]  V-15  tier split 64 / 23 / 13 — primary exceeds target by 4 points (within ±5)

  1 error, 2 warnings
```

| Arg | Effect |
|---|---|
| `--strict` | Promote warnings to errors. Used by the weekly review and CI |
| `--json` | Structured output |

Exit `0` when no errors (and, under `--strict`, no warnings), `1` otherwise. Must complete in under
5 seconds so it can run in a pre-commit hook.

---

## `roadmap coverage`

The FR-024 / SC-008 role-coverage report — which target roles the completed work actually supports.

```text
$ roadmap coverage

  Role                        Tier        Days   Done   Readiness
  AI / Agentic AI Engineer    primary       42     11       26%
  Forward Deployed Engineer   secondary     18      6       33%
  ML Engineer                 remaining      4      0        0%   evidence: 0/1
  Inference Engineer          remaining      3      0        0%   evidence: 0/1
  Embedded ML Engineer        remaining      2      0        0%   evidence: 0/1
  AI Test Validation          remaining      1      0        0%   evidence: 0/1

  Domain share: applied-ai 34% · dsa 23% · ml 20% · python 11% · systems 9% · git 3%
```

| Arg | Effect |
|---|---|
| `--role <id>` | Detail for one role, listing the specific days |
| `--json` | Structured output |

Exit `0` always.

---

## `roadmap render`

Regenerates `roadmap/ROADMAP.md` and `roadmap/milestones.md` from `roadmap.yaml`. The only command
that writes the generated views.

```text
$ roadmap render
  wrote roadmap/ROADMAP.md (70 days, 10 weeks)
  wrote roadmap/milestones.md (3 milestones)
```

| Arg | Effect |
|---|---|
| `--check` | Verify the generated files are up to date without writing. Exit `1` if stale |

`--check` exists so the pre-commit hook can catch a hand-edited or stale `ROADMAP.md`, which is the
one failure mode that would silently desynchronise the source of truth from what the learner reads
each morning.

---

## Error handling

| Condition | Exit | Message |
|---|---|---|
| `roadmap.yaml` missing | 2 | Names the expected path and suggests `roadmap init` |
| Unknown schema `version` | 2 | Refuses to guess; names the supported version |
| `progress.yaml` missing | 0 | Treated as a fresh start; `today` returns day 1 |
| Dirty working tree on `complete` | 2 | Lists the uncommitted paths |
| Day id out of range | 2 | Names the valid range |
