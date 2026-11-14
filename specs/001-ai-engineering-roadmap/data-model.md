# Phase 1 Data Model: AI Engineering Learning Roadmap

**Feature**: 001-ai-engineering-roadmap | **Date**: 2026-11-14

Nine entities, derived from the spec's Key Entities section. Field types use YAML conventions.
Validation rules reference the rule IDs defined in [contracts/roadmap-schema.md](./contracts/roadmap-schema.md).

---

## Entity relationships

```text
Roadmap (1)
├── weeks (10) ──────────── Week
│   ├── days (7 each) ───── DayEntry ──┬── domain ──────── Domain (6)
│   │                                   ├── topic ───────── Topic (~25)
│   │                                   ├── measurement ─── Measurement (0..1)
│   │                                   └── role_tier ───── RoleTarget (6)
│   └── review ──────────── ReviewCheckpoint (1 each)
│                             └── resolves ──────────────── Topic (due ones)
└── milestones (3) ───────── PromotionMilestone
                              └── prerequisite_days ─────── DayEntry

Progress (1, separate file)
└── entries (70) ─────────── DayProgress ─── day_id ─────── DayEntry
```

---

## 1. Roadmap

The whole programme. One per repository. Lives at `roadmap/roadmap.yaml`.

| Field | Type | Required | Notes |
|---|---|---|---|
| `version` | string | yes | Schema version, currently `1` |
| `start_date` | date | yes | `2026-11-16` |
| `end_date` | date | yes | `2027-01-24`; must equal `start_date` + `total_days` − 1 |
| `total_days` | int | yes | `70` |
| `weekday_hours` | number | yes | `4` |
| `weekend_hours` | number | yes | `6` |
| `primary_role` | role id | yes | `agentic-ai` |
| `secondary_role` | role id | yes | `fde` |
| `domains` | map of Domain | yes | Exactly the 6 constitution domains |
| `roles` | map of RoleTarget | yes | Exactly 6 |
| `topics` | map of Topic | yes | ~25 |
| `weeks` | list of Week | yes | Exactly 10 |
| `milestones` | list of PromotionMilestone | yes | At least 3 |
| `interview_imminent_plan` | map of role id -> list of topic id | yes | FR-026: the minimum drill subset per role when an interview lands before the programme ends |

**Validation**: V-01 (date arithmetic consistent), V-10 (domain and role maps complete), V-21
(`interview_imminent_plan` present, non-empty per role, references existing topic ids).

---

## 2. Week

A named block of 7 consecutive days with exactly one review checkpoint.

| Field | Type | Required | Notes |
|---|---|---|---|
| `number` | int | yes | 1..10, contiguous, no gaps |
| `theme` | string | yes | e.g. "Agent loops and tool use" |
| `domains` | list of domain id | yes | Domains this week advances |
| `outcome` | string | yes | What the learner can do by week's end |
| `days` | list of DayEntry | yes | Exactly 7 |
| `review` | ReviewCheckpoint | yes | Exactly 1 |

**Validation**: V-03 (7 days per week, 70 total, numbers contiguous across weeks).

---

## 3. DayEntry

The atomic unit of work. 70 of them. This is the entity the learner reads every morning.

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | int | yes | 1..70, globally unique and contiguous |
| `date` | date | yes | Derived; `start_date` + `id` − 1 |
| `day_type` | enum | yes | `weekday` \| `weekend`; derived from `date` |
| `objective` | string | yes | One sentence. The single thing today is for |
| `domain` | domain id | yes | Exactly one |
| `topic` | topic id | yes | Exactly one |
| `artifact` | path | yes | Repo-relative path the day must produce. **Never empty** (Principle I) |
| `verification` | string | yes | The test or measurement that proves it works |
| `notes_topic` | string | yes | What the `NOTES.md` entry must explain (Principle IV) |
| `effort_hours` | number | yes | Must not exceed the day_type budget (FR-027) |
| `tier` | enum | yes | `primary` \| `secondary` \| `remaining` |
| `priority` | enum | yes | `core` \| `optional` — `optional` is cut first when behind (FR-007) |
| `gate` | list of string | yes | ≥1 objectively evaluable pass/fail conditions |
| `minimum_viable` | string | yes | The reduced artifact for a short session (FR-004) |
| `prerequisites` | list of day id | no | Must all be lower than `id` (FR-011) |
| `from_scratch_of` | day id | no | Set on a library day; points at its scratch counterpart (Principle III) |
| `measurement` | Measurement | no | Required if the day makes a perf/accuracy/latency/memory claim |
| `language` | string | no | Defaults to `python` |
| `language_exception` | string | no | **Required** when `language != python` |
| `offline` | bool | no | Defaults to `true`; `false` means the day prefers live API access |
| `offline_fallback` | string | no | **Required** when `offline` is `false` (FR-034) |
| `serving` | string | no | **Required**, value `fastapi`, on any day wrapping an LLM call, agent, or model as a reachable service (FR-030a) |
| `generic_concept` | string | no | **Required** on any day whose vehicle is Claude Code skills, the Claude Agent SDK, or MCP; names the transferable agentic-pattern concept being practiced (tool use, multi-step control flow, multi-agent orchestration) so the day is not graded on Claude-specific trivia (FR-030b) |

**Validation**: V-02 (artifact non-empty), V-04 (effort within day_type budget), V-05 (scratch
precedes library), V-06 (measurement completeness), V-11 (prerequisites earlier), V-12
(language and offline exceptions justified), V-18 (`serving` is `fastapi` when set), V-19
(`generic_concept` set whenever the day's topic or tooling references Claude Code skills, Agent
SDK, or MCP).

---

## 4. Domain

One of the six constitution learning areas. Fixed set; cannot be extended without a constitution
amendment.

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | enum | yes | `python` \| `dsa` \| `git` \| `systems` \| `ml` \| `applied-ai` |
| `name` | string | yes | Display name |
| `directory` | path | yes | Repo-relative root for this domain's artifacts |
| `target_days` | int | yes | Planned day count; validator compares against actual |
| `min_depth` | string | yes | The floor this domain must reach regardless of role weighting |
| `supports_roles` | list of role id | yes | Which target roles this domain serves |

**Validation**: V-10 (all 6 present), SC-003 (no domain exceeds 40% of `total_days`).

---

## 5. Topic

A named concept or pattern within a domain — the unit that spaced repetition operates on.

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | slug | yes | e.g. `sliding-window`, `attention-from-scratch` |
| `name` | string | yes | Display name |
| `domain` | domain id | yes | Owning domain |
| `first_day` | day id | yes | Where it is introduced |
| `resurface_after` | list of int | yes | Intervals in **completed programme days**, strictly increasing, ≥2 entries (R-004, FR-015). Default `[7, 21]` |
| `references` | list of {title, url} | no | Titles and links only — never reproduced text (FR-035, R-007) |

**Validation**: V-07 (≥2 strictly increasing intervals).

---

## 6. Measurement

Attached to a DayEntry that makes a quantitative claim. Principle V's mechanism.

| Field | Type | Required | Notes |
|---|---|---|---|
| `metric` | enum | yes | `latency` \| `throughput` \| `memory` \| `accuracy` \| `cost` |
| `baseline` | string | yes | What the result is compared against. **Never empty** |
| `results_path` | path | yes | Where the committed results file lands, normally `<topic>/benchmarks.json` |
| `method` | string | yes | How it is measured, so week 2 and week 9 numbers are comparable |

**Validation**: V-06 — if a DayEntry has a `measurement`, all four fields must be non-empty, and
`roadmap check` fails the day if `results_path` does not exist.

---

## 7. ReviewCheckpoint

One per week. The mechanism behind Principle VI and FR-013/014.

| Field | Type | Required | Notes |
|---|---|---|---|
| `week` | int | yes | Matches the owning Week |
| `day` | day id | yes | Which day carries the review (normally the week's last day) |
| `resolves` | list of topic id | yes | ≥2 topics scheduled for from-blank-file re-solve (FR-014) |
| `procedure` | list of string | yes | The ordered review steps |
| `output_path` | path | yes | `progress/reviews/week-NN.md` |

**Validation**: V-07 (≥2 resolves), and every `dsa`/`ml` topic must appear in some checkpoint's
`resolves` at least twice across the programme — or in every checkpoint remaining after it, if
fewer than 2 review checkpoints occur after the topic's `first_day` (FR-015's scope is DSA
problem sets and core ML concepts, not every topic in every domain).

---

## 8. PromotionMilestone

A point at which learnings support an external portfolio project. Principle VII's boundary.

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | slug | yes | One of the 3 locked milestones: `code-review-triage-agent`, `inference-gateway`, `compression-validation-suite` |
| `name` | string | yes | The project's working name |
| `after_day` | day id | yes | Earliest day the milestone can be started |
| `prerequisite_days` | list of day id | yes | All must be `complete` before the milestone opens |
| `purpose` | string | yes | What the project is for |
| `demonstrates` | list of string | yes | Minimum capabilities it must show |
| `supports_roles` | list of role id | yes | Which target roles it speaks to |
| `external` | const `true` | yes | Hard-coded; this project is **not** built in this repository |
| `record_path` | path | yes | `promoted/README.md` — where the pointer record goes |

**Validation**: V-08 — a milestone must not declare any `artifact` path inside this repository.
V-20 — `purpose`, `demonstrates`, and `supports_roles` must each be non-empty (FR-020).

---

## 9. RoleTarget

One of the six role families, with its derived readiness.

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | enum | yes | `agentic-ai` \| `fde` \| `ml-engineer` \| `inference` \| `embedded-ml` \| `test-validation` |
| `name` | string | yes | Display name |
| `tier` | enum | yes | `primary` \| `secondary` \| `remaining` |
| `supporting_domains` | list of domain id | yes | Which domains serve this role |
| `evidence_required` | list of string | no | For `remaining`-tier roles, the artifact each must show (FR-032) |

**Validation**: exactly one `primary` and one `secondary`; tier day counts within ±5 points of
60/25/15 (SC-012).

---

## 10. DayProgress

Lives in `progress/progress.yaml`, separate from the roadmap. One entry per attempted day.

| Field | Type | Required | Notes |
|---|---|---|---|
| `day` | day id | yes | References a DayEntry |
| `status` | enum | yes | `pending` \| `complete` \| `skipped` \| `carried` |
| `date` | date | yes | When it was actually worked, which may differ from the planned date |
| `commit` | string | no | Commit SHA. **Required** when status is `complete` (Principle I) |
| `gate_passed` | bool | no | Result of `roadmap check`; required when `complete` |
| `journal_ref` | string | no | Anchor into `progress/journal.md` |
| `resolve_results` | list of {topic, passed} | no | Outcomes of any re-solves done that day |

### Day status state machine

```text
          ┌──────────────────────────────────────────┐
          │                                          │
          ▼                                          │
     ┌─────────┐  gate passes   ┌──────────┐         │
     │ pending │───────────────▶│ complete │         │
     └─────────┘                └──────────┘         │
       │     │                                       │
       │     │ out of time                           │
       │     └──────────────▶ ┌─────────┐            │
       │                      │ carried │────────────┘
       │                      └─────────┘  resumed next session
       │ deliberately not done
       ▼
     ┌─────────┐
     │ skipped │   terminal — recorded, never silently omitted (Principle II)
     └─────────┘
```

`complete` is terminal and requires both a commit SHA and `gate_passed: true`. `carried` returns to
`pending` on the next session. `skipped` is terminal but remains in the record — FR-017's recovery
rules operate on skipped days, and the validator rejects a progress file with gaps in the day
sequence (V-09).

---

## Derived values (never stored)

These are computed, not written, so they cannot drift:

| Value | Computed from | Serves |
|---|---|---|
| Current day | First entry in `progress.yaml` whose status is not `complete` or `skipped` | SC-001, FR-017 re-entry |
| Days remaining | `total_days` − count(complete) | SC-010 |
| Core effort total | Sum of `effort_hours` where `priority == core` | SC-009 (≤ 272 h) |
| Domain share | count(days per domain) ÷ `total_days` | SC-003 (≤ 40%) |
| Tier split | count(days per tier) ÷ `total_days` | SC-012 (60/25/15 ±5) |
| Topics due | Topics whose `first_day` + `resurface_after[n]` ≤ completed-day count | FR-015 |
| Role readiness | Completed days supporting a role ÷ days supporting that role | FR-024, SC-008 |
