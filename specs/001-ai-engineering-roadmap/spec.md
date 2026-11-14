# Feature Specification: AI Engineering Learning Roadmap

**Feature Branch**: `main` (no feature branch — git branch hook not installed in this project)

**Created**: 2026-11-14

**Status**: Ready for planning — all clarifications resolved 2026-11-14

## Clarifications

### Session 2026-11-14

- Q: Should FastAPI (or an equivalent serving framework) be named explicitly as a required skill in the roadmap, since 'Applied AI Engineering' currently says 'LLM APIs' without naming the serving layer used to expose them? → A: Yes, require FastAPI explicitly as the named framework for wrapping models/agents as services.
- Q: Should the roadmap explicitly add a domain/day-set for Claude-specific tooling (Claude Code skills, Claude Agent SDK, MCP, multi-agent orchestration), given the constitution currently names six domains that don't mention these by name? → A: Yes, cover it as a named sub-topic inside the existing Applied AI Engineering domain (agentic patterns), not as a 7th domain.
- Q: Since MCP, Claude Agent SDK, and Claude Code skills are Anthropic-specific, how should their depth compare to the general agentic-patterns material (tool use, multi-step control flow) already required by FR-030? → A: Secondary — generic, interview-transferable agentic-pattern concepts stay primary; Claude-specific tooling is practiced as the implementation vehicle for those days rather than a separate deeper track.

**Input**: User description: "A 2-3 month structured AI engineering learning roadmap for this playground repository, with per-day deliverables. The roadmap must sequence the six in-scope domains from the constitution (Python, DSA with large-tech interview weighting, Git, System Design including ML/inference architectures, ML & DL fundamentals and internals, and Applied AI Engineering covering LLM APIs, retrieval, agentic patterns, inference optimization and AI test/validation). Each day must specify a concrete committed artifact, a measurement or test where applicable, and a NOTES.md topic, per constitution Principles I-VI. The roadmap must include weekly review checkpoints with spaced-repetition re-solve slots, and must identify milestones where learnings are ready to be promoted outward into separate production-deployable CV projects (Principle VII) without those projects being built inside this repo. Target outcome: readiness for AI engineering interviews (FDE, AI/Agentic AI engineer, ML engineer, Embedded ML, Inference engineer, AI test validation)."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Know and ship today's deliverable (Priority: P1)

The learner sits down for a study session, opens one place in the repository, and within two
minutes knows exactly what to build today: the objective, the artifact to produce, the test or
measurement that proves it works, and the note to write. They build it, verify it, log it, and
commit. They never spend session time deciding what to study.

**Why this priority**: This is the engine of the whole program. Without a ready-made daily
objective, sessions are lost to planning and the daily-deliverable principle collapses. Delivered
alone, it already produces a growing body of committed artifacts — a viable MVP.

**Independent Test**: Pick any day number in the roadmap and hand it to the learner cold. They can
begin building within two minutes without asking a question, and at the end they can state
unambiguously whether the day passed or failed its completion gate.

**Acceptance Scenarios**:

1. **Given** the roadmap exists and the learner has completed day 12, **When** they open the
   roadmap at the start of a session, **Then** day 13's objective, required artifact, verification
   step, and note topic are visible in one place without cross-referencing other documents.
2. **Given** a day entry is open, **When** the learner finishes building, **Then** the entry states
   an explicit pass/fail completion gate they can evaluate without judgement calls.
3. **Given** a day's topic depends on an earlier day's artifact, **When** the learner reads the
   entry, **Then** the prerequisite day is named.
4. **Given** a session is cut short, **When** the learner can only spend part of the planned time,
   **Then** the entry identifies a reduced "minimum viable" artifact that still satisfies the
   daily-deliverable principle.

---

### User Story 2 - Retain what was learned (Priority: P2)

The learner revisits earlier material on a schedule rather than only moving forward. Previously
solved problems resurface for a from-blank-file re-solve, and fragile topics are flagged for extra
passes. Retention, not coverage, drives the schedule.

**Why this priority**: Interview performance depends on retrieval speed, and a forward-only roadmap
guarantees that week 1 material is gone by week 8. This is the difference between having touched
the syllabus and being able to perform.

**Independent Test**: Run the roadmap's review slots in isolation against a set of already-completed
topics and confirm each topic resurfaces at least twice at increasing intervals, with a recorded
pass/fail outcome per re-solve.

**Acceptance Scenarios**:

1. **Given** the learner completed a set of problems in week 2, **When** they reach the week 4 and
   week 7 review slots, **Then** a defined subset of those problems is scheduled for re-solve from
   a blank file.
2. **Given** a re-solve fails, **When** the learner records the failure, **Then** the roadmap directs
   that topic back into an upcoming review slot rather than letting it drop.
3. **Given** time is short in a session, **When** both new material and a pending re-solve are
   scheduled, **Then** the roadmap states that revision takes priority.

---

### User Story 3 - Weekly review and honest re-planning (Priority: P2)

Once a week the learner stops producing and inspects: what shipped, what slipped, which
constitution principles were violated, and what gets cut from next week. Scope is reduced
deliberately instead of silently accumulating as a backlog.

**Why this priority**: A 2–3 month plan at daily granularity will drift within the first fortnight.
Without a built-in correction mechanism the plan is abandoned rather than adjusted.

**Independent Test**: Simulate a week in which three of seven days were missed, run the weekly
review procedure, and confirm it produces a concrete re-planned next week with named cuts rather
than a growing backlog.

**Acceptance Scenarios**:

1. **Given** a week has ended, **When** the learner runs the review checkpoint, **Then** it yields a
   record of days completed, days skipped, re-solve outcomes, and principle violations observed.
2. **Given** the learner is behind schedule, **When** they re-plan, **Then** the roadmap provides an
   explicit rule for what to cut first and what is never cut.
3. **Given** the learner is ahead of schedule, **When** they re-plan, **Then** the roadmap names
   optional stretch material rather than leaving the time unstructured.

---

### User Story 4 - Know when a topic is ready to become a CV project (Priority: P3)

At defined points the learner can see that a cluster of learnings is now sufficient to support a
production-deployable portfolio project, what that project should demonstrate, and which target
roles it speaks to. The project is then built in its own separate repository, and the playground
records only its name, source learnings, and link.

**Why this priority**: The job outcome depends on portfolio artifacts, but building them too early
produces shallow work and building them inside the playground violates the separation principle.
This is valuable but depends on earlier learning being in place first.

**Independent Test**: Reach a promotion milestone with its prerequisite days marked complete and
confirm the milestone states the project's scope, what it must demonstrate, its target roles, and
the one-line record to add back to the playground — with no project code created in this repository.

**Acceptance Scenarios**:

1. **Given** the prerequisite days for a milestone are complete, **When** the learner reads the
   milestone, **Then** it specifies the project's purpose, the minimum demonstrable capability, and
   the roles it supports.
2. **Given** a milestone is reached, **When** the learner begins the project, **Then** the roadmap
   directs them to create it in a separate repository and to add only a pointer record here.
3. **Given** prerequisite days are incomplete, **When** the learner reads the milestone, **Then** the
   unmet prerequisites are identified.

---

### User Story 5 - Map progress to target roles (Priority: P3)

The learner can see which of the target role families each completed domain supports, and which
roles remain under-served, so that remaining time is spent closing the gap that matters for the
roles they are actually applying to.

**Why this priority**: The six named role families weight the domains very differently. Without a
visible mapping, effort spreads evenly and no single role profile becomes strong.

**Independent Test**: With an arbitrary subset of days marked complete, the mapping identifies which
target roles are adequately covered and which are not.

**Acceptance Scenarios**:

1. **Given** a set of completed days, **When** the learner consults the role mapping, **Then** each
   target role shows the proportion of its supporting material completed.
2. **Given** a primary target role is chosen, **When** the learner follows the roadmap, **Then** the
   domains weighted toward that role appear earlier and in greater depth than the others.

---

### Edge Cases

- **Missed days**: What happens when the learner misses one day, three consecutive days, or a full
  week? The roadmap must define whether days shift, compress, or drop, and must never require a
  silent backlog.
- **Topic overruns**: What happens when a day's objective genuinely needs two or three sessions?
  The roadmap must allow a day to span sessions without corrupting downstream day numbering.
- **Uneven time availability**: How does the plan handle a weekday with one hour versus a weekend
  with six? Day entries must be sized by expected effort, not assumed to be interchangeable.
- **A real interview lands mid-program**: What is the emergency re-prioritisation path when an
  interview is scheduled three weeks in, before the plan completes?
- **A re-solve keeps failing**: What happens when the same topic fails re-solve twice? The roadmap
  must escalate rather than loop indefinitely.
- **Material requires paid or heavy infrastructure**: What happens when a topic (large-model
  training, GPU inference, cloud deployment) cannot run on the learner's machine? Each such day
  must degrade to a small local sample or simulation.
- **Prerequisite knowledge is absent**: What happens when a day assumes a concept the learner never
  learned? Day entries must name prerequisites so the gap is visible before the session starts.
- **Motivation collapse**: What happens after a multi-day gap? The roadmap must provide a defined
  re-entry point rather than requiring the learner to restart or guess.
- **Scope cannot fit the available time**: If the full six-domain program exceeds the learner's real
  capacity, the roadmap must state which material is core and which is optional, rather than
  producing a plan that is certain to be abandoned.

## Requirements *(mandatory)*

### Functional Requirements

**Roadmap structure**

- **FR-001**: The roadmap MUST cover a continuous 10-week programme of 70 numbered day entries,
  starting Monday 2026-11-16 and ending Sunday 2027-01-24, and MUST state that start date, end
  date, and day count explicitly.
- **FR-002**: The roadmap MUST be organised into weeks, each with a stated theme, the domains it
  advances, and its expected outcome.
- **FR-003**: The roadmap MUST provide an entry for every study day in the programme.
- **FR-004**: Each day entry MUST specify, at minimum: a single objective, the concrete artifact to
  be committed, the test or measurement that verifies it, the `NOTES.md` topic to write, the
  expected effort in hours, any prerequisite day, and a reduced minimum-viable artifact for short
  sessions.
- **FR-005**: Each day entry MUST state an explicit, objectively evaluable completion gate.
- **FR-006**: The roadmap MUST identify, for each day, which of the six in-scope domains it advances.
- **FR-007**: The roadmap MUST designate every day as either core (never cut) or optional
  (cut first when behind), so that scope reduction is a lookup rather than a judgement call.

**Domain coverage**

- **FR-008**: The roadmap MUST include days advancing all six in-scope constitution domains: Python;
  Data Structures & Algorithms; Git; System Design including ML and inference architectures; ML & DL
  fundamentals and internals; and Applied AI Engineering covering LLM APIs, retrieval, agentic
  patterns, inference optimization, and AI test/validation.
- **FR-009**: The DSA material MUST be organised by interview-frequency-weighted pattern rather than
  by data-structure taxonomy, and MUST state which pattern each problem set exercises.
- **FR-010**: For every foundational topic, the roadmap MUST schedule the from-scratch
  implementation before any framework or library treatment of the same idea, and MUST schedule the
  library comparison afterward.
- **FR-011**: The roadmap MUST sequence domains so that no day depends on material scheduled later.
- **FR-012**: Each day whose claims concern performance, accuracy, latency, or memory MUST require a
  committed, reproducible measurement, and MUST name the baseline being compared against.

**Review and retention**

- **FR-013**: The roadmap MUST include one review checkpoint per calendar week with a defined
  procedure and a recorded output.
- **FR-014**: Each review checkpoint MUST schedule at least two from-blank-file re-solves of
  previously completed problems, naming which ones.
- **FR-015**: Every DSA problem set and core ML concept MUST be scheduled for re-surfacing at least
  twice at increasing intervals after its first completion.
- **FR-016**: The roadmap MUST define an escalation path for a topic that fails re-solve twice.
- **FR-017**: The roadmap MUST define rules for recovering from missed days, consecutive missed
  days, and a fully missed week, including a named re-entry point after any gap.
- **FR-018**: The roadmap MUST state the priority rule that revision of fragile material outranks
  starting new material when session time is short.

**Promotion to CV projects**

- **FR-019**: The roadmap MUST define at least three promotion milestones at which accumulated
  learnings support a production-deployable portfolio project.
- **FR-020**: Each promotion milestone MUST state its prerequisite days, the project's purpose, the
  minimum capability the project must demonstrate, and the target roles it supports.
- **FR-021**: Each promotion milestone MUST direct that the project be created in a separate
  repository and MUST NOT schedule project implementation work inside this repository.
- **FR-022**: The roadmap MUST provide a record format for promoted projects in this repository
  capturing the project name, the learnings it draws on, and a link.

**Progress and role targeting**

- **FR-023**: The roadmap MUST provide a progress record in which each day is marked complete,
  skipped, or carried over, with the date and a one-paragraph log entry.
- **FR-024**: The roadmap MUST map each of the six target role families to the domains and days that
  support it, so that coverage gaps per role are visible.
- **FR-025**: The roadmap MUST allocate programme days by role priority in the ratio 60% primary /
  25% secondary / 15% remaining, and MUST still cover every in-scope domain to a stated minimum
  depth. Days that serve more than one role tier count toward the highest tier they serve.
- **FR-026**: The roadmap MUST provide an interview-imminent re-prioritisation path identifying the
  minimum subset of material to drill when an interview is scheduled before the programme ends.

**Fit to the learner**

- **FR-027**: Day effort estimates MUST fit a budget of 4 focused hours on weekdays (Monday to
  Friday) and 6 focused hours on weekend days, totalling 32 hours per week and 320 hours across the
  programme. No single day entry MUST exceed its own day-type budget, and weekday entries MUST NOT
  assume weekend-length sessions.
- **FR-028**: The roadmap MUST assume a starting baseline of working Python ability with no
  substantive DSA practice and only conceptual ML/DL exposure. It MUST NOT schedule days teaching
  Python syntax, basic control flow, or basic data types. It MUST begin DSA at pattern level from
  week 1 and MUST begin ML/DL at mechanism level — implemented from scratch — rather than at
  conceptual overview level.
- **FR-029**: The roadmap MUST treat **AI / Agentic AI Engineer** as the primary target role and
  **Forward Deployed Engineer (FDE)** as the secondary target role, with ML Engineer, Inference
  Engineer, Embedded ML Engineer, and AI Test Validation Engineer covered at minimum depth in that
  order of preference.
- **FR-030**: Because the primary role is AI / Agentic AI Engineer, the roadmap MUST give greatest
  depth to Applied AI Engineering — LLM API usage and cost/latency control, retrieval and its
  evaluation, agentic patterns including tool use and multi-step control flow, and systematic
  evaluation of non-deterministic systems.
- **FR-030a**: The roadmap MUST require FastAPI as the named serving framework for exposing any
  model, LLM-API wrapper, or agent as a runnable service, so that day artifacts under FR-030 are
  reachable over HTTP rather than left as scripts.
- **FR-030b**: The roadmap MUST cover Claude Code skills, the Claude Agent SDK, and MCP
  (Model Context Protocol) as named implementation vehicles for the agentic-patterns days required
  by FR-030, rather than as a separate domain. Generic, interview-transferable agentic concepts
  (tool use, multi-step control flow, multi-agent orchestration) remain the primary learning
  objective of those days; Claude-specific tooling is the means of practicing them, not an
  additional depth track, and MUST NOT increase the Applied AI Engineering day count beyond what
  FR-003/SC-003 already allow.
- **FR-031**: Because the secondary role is FDE, the roadmap MUST give second-greatest depth to
  breadth-of-delivery material: system design, integration and deployment patterns, debugging
  unfamiliar systems, and interview-grade DSA fluency.
- **FR-032**: The roadmap MUST ensure that minimum-depth coverage of the four remaining roles is
  sufficient for the learner to hold a competent technical conversation about each — specifically
  at least one committed artifact exercising classical ML training and evaluation, one exercising
  inference latency and memory measurement, one exercising model size reduction, and one exercising
  systematic test and validation of a model or model-backed system.
- **FR-033**: The roadmap MUST front-load the Python depth that the stated baseline leaves open and
  that the primary role requires — typing, packaging, testing, async concurrency, and profiling —
  rather than assuming it from general Python comfort.

**Constraints**

- **FR-034**: Every day's artifact MUST be runnable from a clean checkout of this repository without
  paid infrastructure; any day requiring otherwise MUST specify a reduced local substitute.
- **FR-035**: The roadmap MUST NOT schedule the commitment of secrets, API keys, proprietary
  datasets, or licensed course material.
- **FR-036**: The roadmap MUST NOT schedule work that violates any constitution principle; where the
  roadmap and the constitution conflict, the constitution governs.

### Key Entities

- **Roadmap**: The whole programme. Has a duration, a start and end date, an ordered set of weeks, a
  set of promotion milestones, and a role-coverage mapping.
- **Week**: A named block of consecutive days with a theme, the domains it advances, its expected
  outcome, and exactly one review checkpoint.
- **Day Entry**: The atomic unit of work. Has a number, an objective, a target artifact, a
  verification step, a note topic, an effort estimate, a domain, a core/optional designation, a
  completion gate, optional prerequisites, and a minimum-viable fallback.
- **Domain**: One of the six in-scope learning areas. Has a target depth and a mapping to the roles
  it supports.
- **Topic**: A named concept or pattern within a domain. Has a first-encounter day and a set of
  scheduled re-surfacing dates.
- **Review Checkpoint**: A weekly inspection. Has a procedure, a set of scheduled re-solves, and a
  recorded output covering completions, slips, violations, and next week's cuts.
- **Promotion Milestone**: A point at which learnings support an external portfolio project. Has
  prerequisite days, a project purpose, a minimum demonstrable capability, and supported roles.
- **Progress Log**: The running record. One entry per day with status, date, what was built, what
  broke, and the non-obvious concept.
- **Role Target**: One of the six role families. Has a set of supporting domains with weights and a
  derived readiness state.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The learner can identify and begin the current day's work in under 2 minutes from
  opening the roadmap, without asking a clarifying question.
- **SC-002**: Every day in the programme has a stated artifact and a stated completion gate — 100%
  coverage, zero entries reading "study" or "read about" with no deliverable.
- **SC-003**: All six in-scope domains are advanced by at least one day, and no domain exceeds 40%
  of total programme days.
- **SC-004**: At the end of the programme the repository contains at least one committed, runnable
  artifact per completed day, each reproducible from a clean checkout.
- **SC-005**: Every DSA pattern and core ML concept introduced is scheduled for re-surfacing at least
  twice after its first completion.
- **SC-006**: In a simulated week with three missed days, applying the roadmap's recovery rules
  produces a re-planned following week with named cuts and no accumulated backlog.
- **SC-007**: At least three promotion milestones are defined, each naming its prerequisite days and
  supported roles, and none schedules implementation work inside this repository.
- **SC-008**: Each of the six target role families is traceable to the specific days that support it,
  with no role left unmapped.
- **SC-009**: The sum of effort estimates across all core (never-cut) day entries is at most 272
  hours — 85% of the 320-hour programme budget — leaving at least 15% slack for overruns, re-solves,
  and missed days.
- **SC-010**: An independent reader given only the roadmap and this repository can determine the
  learner's exact progress and the next action without consulting the learner.
- **SC-011**: Zero days require paid infrastructure or network-dependent resources to reach their
  completion gate.
- **SC-012**: Day allocation across role tiers falls within 5 percentage points of the 60 / 25 / 15
  primary / secondary / remaining split, verifiable by counting day entries per tier.
- **SC-013**: Each of the four minimum-depth roles is supported by at least one completed artifact
  of the kind named in FR-032, so no target role is left with zero demonstrable evidence.

## Assumptions

- **Audience**: The roadmap is written for a single self-directed learner working alone, not a cohort
  or a taught course.
- **Study rhythm**: The programme assumes near-daily study with occasional missed days treated as the
  norm rather than the exception; recovery rules are therefore mandatory rather than optional.
- **Duration**: "2–3 months" is fixed at 10 calendar weeks — 70 day entries, Monday 2026-11-16 to
  Sunday 2027-01-24 — derived from the 32-hour weekly budget.
- **Holiday period**: The programme spans late December. Weeks 6 and 7 are assumed to be the most
  likely to slip and are therefore the primary home for optional days and re-solve slots rather
  than for new core material.
- **Language**: Python is the implementation language for all days except where a concept cannot be
  demonstrated in Python, per the constitution.
- **Interview targeting**: "MANGOS" is interpreted as the large-tech hiring bar generally (Meta,
  Microsoft, Anthropic, Amazon, NVIDIA, Google, OpenAI); DSA weighting follows publicly observable
  interview-frequency patterns rather than any company-confidential material.
- **Portfolio projects**: CV projects are built in separate repositories outside this directory and
  are out of scope for this feature; only their milestone definitions and pointer records live here.
- **Environment**: The learner works on a single Windows machine with no guaranteed GPU and no paid
  cloud budget; any GPU or cloud topic degrades to a local sample.
- **Existing knowledge**: The learner writes Python comfortably but has not practised DSA
  substantively and knows ML/DL only conceptually. Python syntax instruction is therefore out of
  scope, while Python engineering depth (typing, packaging, testing, async, profiling) is in scope.
- **Role weighting**: AI / Agentic AI Engineer is the primary target and FDE the secondary; the
  remaining four roles are covered to conversational depth with one demonstrable artifact each,
  not to interview depth.
- **Job outcome**: Securing a job depends on factors outside this repository (applications,
  interviews, market conditions). This feature's scope is interview readiness and portfolio
  readiness, not employment itself.
- **Governance**: The project constitution v1.0.0 governs this roadmap; its seven principles and
  daily quality gates are inputs to every day entry, not restated requirements.
