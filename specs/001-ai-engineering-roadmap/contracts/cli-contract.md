# Contract: the `roadmap` CLI

**Feature**: 001-ai-engineering-roadmap | **Date**: 2026-11-14

Nine commands. Installed via `uv sync` in editable mode, invoked as `uv run roadmap <command>` or
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

  Day 12 of 133 · Thu 2026-11-27 · weekday · 5.0 h + 1.0 h DSA · core · tier: primary
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
| `--days-until-interview N` | FR-026: print the `interview_imminent_plan` drill subset for the remaining N days instead of the normal day card |

Exit `0` always, unless the roadmap fails to load. When all 133 days are done it prints the
programme summary and the promotion milestone status.

---

## `roadmap check`

Runs the current day's gate. Mechanises the constitution's day-completion gate so it is not a
self-assessment. Six items, in order: the artifact exists; its tests pass; `NOTES.md` carries all
eleven sections required by Principle IV; the implementation is written rather than still the
handed-over skeleton (Principle VIII); any declared measurement is committed; and a commit exists.
For a cloud day, the teardown record is also required.

```text
$ roadmap check

  Day 12 · applied-ai/tool-calling

  [PASS] artifact exists            applied-ai/tool-calling/loop.py
  [PASS] tests pass                 3 passed in 0.41s
  [FAIL] notes complete             7/11 sections — missing: Interview questions, ...
  [FAIL] implementation written     still a skeleton — NotImplementedError present
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

Runs rules V-01 to V-24 against `roadmap.yaml`, and P-01 to P-07 plus J-01 to J-03 against the
progress files.

```text
$ roadmap validate

  roadmap.yaml ................ 133 days · 19 weeks · 114 topics · 3 milestones
  [ERROR] V-02  day 34: `minimum_viable` is empty
  [WARN]  V-14  core effort 655.0 h exceeds the 646.0 h cap (85% of the 760.0 h budget) by 9.0 h
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
  wrote roadmap/ROADMAP.md (133 days, 19 weeks)
  wrote roadmap/milestones.md (3 milestones)
```

| Arg | Effect |
|---|---|
| `--check` | Verify the generated files are up to date without writing. Exit `1` if stale |

`--check` exists so the pre-commit hook can catch a hand-edited or stale `ROADMAP.md`, which is the
one failure mode that would silently desynchronise the source of truth from what the learner reads
each morning.

---

---

## `roadmap scan`

FR-035's mechanism. Scans tracked text files for three classes of content that must never
be committed, and is the one check wired into the pre-commit hook as **blocking** — a
secret or a third-party-owned analogue cannot be un-committed once history is public.

```text
$ roadmap scan
  scanned 101 text file(s)
    WARN promoted/README.md: NDA-adjacent wording: code-review-triage

  0 blocking, 1 warning(s)
```

| Class | Severity | Detection |
|---|---|---|
| Secrets | **BLOCK** | Key shapes (Anthropic, OpenAI, AWS, GitHub, Google, Hugging Face, Slack, private-key blocks, bearer literals) plus long hardcoded assignments to `api_key`/`secret`/`token`/`password`. Environment lookups and placeholders are exempt |
| Licensed material | WARN | Two or more distinct problem-statement markers in one `.md`/`.txt` file (`Example 1:`, `Constraints:`, `Input:`/`Output:`, "Given an array … return"). R-007 permits title and URL only |
| Third-party-owned work | WARN | Wording matching the NDA-restricted thesis domain (FR-042). Governance paths (`specs/`, `.specify/`, `promoted/briefs/`, `progress/`) are allowlisted so they can state the restriction |

| Arg | Effect |
|---|---|
| `--staged` | Scan only files staged for commit; what the hook uses |
| `--json` | Structured output |

Exit `0` when no **BLOCK** finding, `1` otherwise. Warnings never fail the command: a scan
that cries wolf gets bypassed, and these two classes are heuristic by nature.

The detection lists in `tools/roadmap_cli/policy.py` are meant to be edited as the
programme goes on.

A file may opt out entirely by containing `roadmap-policy: ignore-file` in its first 40
lines, with a reason. The marker must live in the file itself rather than in configuration,
so an exemption is reviewable in the same diff that relies on it. The canonical case is a
scanner's own test fixtures, which necessarily contain secret-shaped strings.

---

## `roadmap audit`

SC-004 and SC-014's mechanism. `roadmap check` verifies one day; this verifies every
completed day, which is what the success criteria actually claim.

```text
$ roadmap audit
  Audit across 1 completed day(s)

  Notes completeness (SC-014)
    [INCOMPLETE] day 1 project-tooling: 4/11 sections

  Artifact presence (SC-004)
    [OK] day 1 python/project-tooling/env_report.py

  Content policy (FR-035)
    no findings

  1 day(s) with incomplete notes, 0 missing artifact(s), 0 blocking policy finding(s)
```

Review days are excluded from the notes check: their prose lives in the review file itself.

| Arg | Effect |
|---|---|
| `--json` | Structured output, suitable for CI |

Exit `0` only when every completed day has complete notes and a present artifact, and no
blocking policy finding exists. Intended for the weekly review and for CI.

## Error handling

| Condition | Exit | Message |
|---|---|---|
| `roadmap.yaml` missing | 2 | Names the expected path and suggests `roadmap init` |
| Unknown schema `version` | 2 | Refuses to guess; names the supported version |
| `progress.yaml` missing | 0 | Treated as a fresh start; `today` returns day 1 |
| Dirty working tree on `complete` | 2 | Lists the uncommitted paths |
| Day id out of range | 2 | Names the valid range |
