# Feature Specification: AI Engineering Learning Roadmap

**Feature Branch**: `main` (no feature branch — git branch hook not installed in this project)

**Created**: 2026-11-14

**Status**: Amended 2026-11-15 under constitution v1.1.0 — see Clarifications session 2026-11-15

## Clarifications

### Session 2026-11-14

- Q: Should FastAPI (or an equivalent serving framework) be named explicitly as a required skill in the roadmap, since 'Applied AI Engineering' currently says 'LLM APIs' without naming the serving layer used to expose them? → A: Yes, require FastAPI explicitly as the named framework for wrapping models/agents as services.
- Q: Should the roadmap explicitly add a domain/day-set for Claude-specific tooling (Claude Code skills, Claude Agent SDK, MCP, multi-agent orchestration), given the constitution currently names six domains that don't mention these by name? → A: Yes, cover it as a named sub-topic inside the existing Applied AI Engineering domain (agentic patterns), not as a 7th domain.
- Q: Since MCP, Claude Agent SDK, and Claude Code skills are Anthropic-specific, how should their depth compare to the general agentic-patterns material (tool use, multi-step control flow) already required by FR-030? → A: Secondary — generic, interview-transferable agentic-pattern concepts stay primary; Claude-specific tooling is practiced as the implementation vehicle for those days rather than a separate deeper track.

### Session 2026-11-15 (post-audit amendment)

Arising from the strict repository audit of 2026-11-15, which found the stated baseline
contradicted by the learner's actual experience, AWS entirely absent, the module methodology ~29%
implemented, and four day entries building portfolio-project code in breach of Principle VII.

- Q: The spec's baseline (FR-028) assumed working Python with no substantive DSA and only conceptual ML/DL. What is the actual baseline? → A: Roughly two years of applied ML/DL, a completed master's thesis building an agent orchestrator with RAG and MCP for merge-request code review, and a six-month MLOps internship fine-tuning a local model toward Gemini 2.5 Pro parity. Introductory Applied AI material is therefore wasted time; the real gaps are DSA, system design, inference internals, cloud, and production engineering.
- Q: What is the real programme duration and weekly budget, given the master's completion date? → A: 19 weeks to end-March 2027 at ~40 focused hours per week — 133 day entries, 760 hours. Thesis and internship are already complete, so the budget does not compete with coursework.
- Q: Should the secondary target role switch from FDE to ML/MLOps Engineer, given FDE is a scarce title in Germany? → A: No — FDE stays secondary; ML/MLOps leads the remaining tier. FDE preparation is strong-generalist preparation and transfers to the European "AI Engineer (generalist)" roles that dominate the market, so DSA stays at moderate rather than minimal depth.
- Q: Who owns the thesis code, and can milestone 1 (a code-review triage agent) reuse it? → A: An industry partner owns it. It cannot be published, and no public close analogue may be built either. Milestone 1 as specified is withdrawn and replaced.
- Q: Which flagship portfolio project should be committed to? → A: Deferred until after programme week 4. Three candidate briefs are maintained until then: an agent evaluation and observability platform, a multi-backend inference gateway, and a production MCP server with governance.
- Q: Should Embedded ML Engineer remain a target role? → A: No — dropped. It requires C/C++ and hardware work that would dilute the two primary targets, and a single artifact would not make the learner competitive for it.
- Q: Should a seventh domain be added for cloud, given AWS student credits and a strict cost policy? → A: Yes — Cloud & Infrastructure, at 6–7 days, with budget alerts as the first exercise, mandatory per-day cost estimates, and same-day verified teardown. Added to the constitution at v1.1.0.
- Q: Which agent frameworks should be taught, of the six named? → A: LangGraph, LangChain and LlamaIndex. DSPy, Semantic Kernel and Haystack move to a documented Phase 2 backlog — DSPy on engineering merit is the strongest of the three dropped, but it appears in few job descriptions.

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

- **FR-001**: The roadmap MUST cover a continuous 19-week programme of 133 numbered day entries,
  starting Monday 2026-11-16 and ending Sunday 2027-03-28, and MUST state that start date, end
  date, and day count explicitly.
- **FR-002**: The roadmap MUST be organised into weeks, each with a stated theme, the domains it
  advances, and its expected outcome.
- **FR-003**: The roadmap MUST provide an entry for every study day in the programme.
- **FR-004**: Each day entry MUST specify, at minimum: a single objective, the concrete artifact to
  be committed, the test or measurement that verifies it, the `NOTES.md` topic to write, the
  expected effort in hours, any prerequisite day, and a reduced minimum-viable artifact for short
  sessions.
- **FR-005**: Each day entry MUST state an explicit, objectively evaluable completion gate.
- **FR-006**: The roadmap MUST identify, for each day, which of the seven in-scope domains it
  advances.
- **FR-007**: The roadmap MUST designate every day as either core (never cut) or optional
  (cut first when behind), so that scope reduction is a lookup rather than a judgement call.

**Domain coverage**

- **FR-008**: The roadmap MUST include days advancing all seven in-scope constitution domains:
  Python including OOP, internals and software-engineering principles; Data Structures & Algorithms;
  Git & Linux; System Design including networking, data modelling, distributed fundamentals and ML
  and inference architectures; ML & DL including applied mathematics and the MLOps lifecycle;
  Applied AI Engineering covering LLM internals, retrieval, agentic patterns, protocols, inference
  optimization, observability and AI test/validation; and Cloud & Infrastructure.
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
  repository and MUST NOT schedule project implementation work inside this repository. This
  prohibition binds individual day entries as well as milestone definitions (see FR-039).
- **FR-022**: The roadmap MUST provide a record format for promoted projects in this repository
  capturing the project name, the learnings it draws on, and a link.

**Progress and role targeting**

- **FR-023**: The roadmap MUST provide a progress record in which each day is marked complete,
  skipped, or carried over, with the date and a one-paragraph log entry.
- **FR-024**: The roadmap MUST map each of the five in-scope target role families to the domains and
  days that support it, so that coverage gaps per role are visible.
- **FR-025**: The roadmap MUST allocate programme days by role priority in the ratio 60% primary /
  25% secondary / 15% remaining, and MUST still cover every in-scope domain to a stated minimum
  depth. Days that serve more than one role tier count toward the highest tier they serve.
- **FR-026**: The roadmap MUST provide an interview-imminent re-prioritisation path per target role,
  each naming at least six topics ordered by drill priority, spanning at least three distinct
  domains, and drawn only from days already completed or completable within one week. Each path
  MUST state the expected drill time and MUST NOT consist solely of early-programme topics.

**Fit to the learner**

- **FR-027**: Day effort estimates MUST fit a budget of 6 focused hours on weekdays (Monday to
  Friday) and 5 focused hours on weekend days, totalling 40 hours per week and 760 hours across the
  programme. No single day entry MUST exceed its own day-type budget, and the day's main artifact
  effort plus the FR-037 daily DSA hour MUST together fit within that budget.
- **FR-028**: The roadmap MUST assume a starting baseline of **applied professional experience in
  ML/DL and applied AI engineering**: approximately two years of ML/DL work, a completed master's
  thesis building an agent orchestrator with retrieval and MCP, and an MLOps internship including
  fine-tuning a local model toward a frontier-model baseline. Accordingly it MUST NOT schedule
  introductory days on Python syntax, LLM API basics, basic tool calling, introductory chunking or
  introductory vector search. It MUST treat the learner's genuine gaps as the subject of the
  programme: Data Structures & Algorithms, System Design, inference and serving internals, Cloud &
  Infrastructure, and the production-engineering layer — observability, evaluation rigour under
  load, guardrails — around systems of the kind the learner can already build.
- **FR-029**: The roadmap MUST treat **AI / Agentic AI Engineer** as the primary target role and
  **Forward Deployed Engineer (FDE)** as the secondary target role, with the remaining tier ordered
  **ML/MLOps Engineer, Inference Engineer, AI Test Validation Engineer**. Embedded ML Engineer is
  **out of scope** as a target role; no day or milestone is required to serve it.
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
- **FR-032**: The roadmap MUST ensure that minimum-depth coverage of the three remaining roles is
  sufficient for the learner to hold a competent technical conversation about each — specifically
  at least one committed artifact exercising the MLOps lifecycle (pipeline, registry, drift or
  serving), one exercising inference latency and memory measurement, one exercising model size
  reduction, and one exercising systematic test and validation of a model or model-backed system.
- **FR-033**: The roadmap MUST front-load the Python and software-engineering depth that the stated
  baseline leaves open and that the primary role requires — typing, packaging, testing, async
  concurrency, profiling, OOP and the object model, memory internals, clean code, SOLID, and design
  patterns.

**Constraints**

- **FR-034**: Every day's artifact and its tests MUST be runnable from a clean checkout of this
  repository without paid infrastructure; any day requiring otherwise MUST specify a reduced local
  substitute. Cloud & Infrastructure days are the sole exception and MUST still commit a reviewable
  artifact — configuration, infrastructure definition, measurements, and a teardown record.
- **FR-035**: The roadmap MUST NOT schedule the commitment of secrets, API keys, proprietary
  datasets, or licensed course material. It MUST NOT schedule any artifact that reproduces, or is a
  close public analogue of, work owned by a third party under agreement.
- **FR-036**: The roadmap MUST NOT schedule work that violates any constitution principle; where the
  roadmap and the constitution conflict, the constitution governs.

**Amendments under constitution v1.1.0 (2026-11-15)**

- **FR-037**: The DSA material MUST run as a continuous daily track across every day of the
  programme, budgeted at approximately one hour per day, and MUST NOT be scheduled as a block of
  consecutive DSA-only days. DSA effort MUST be accounted separately from the day's main artifact
  effort so that both together fit the day-type budget in FR-027.
- **FR-038**: Every topic's `NOTES.md` MUST carry all eleven sections required by constitution
  Principle IV: learning objectives, prerequisites, conceptual explanation, why it matters,
  internal mechanisms, real-world applications, alternatives and trade-offs, failure modes and
  common mistakes, at least three interview questions with the learner's answers, assessment
  criteria, and revision notes.
- **FR-039**: No day entry MUST produce an artifact that implements a promotion milestone's project,
  including its scaffold, core, prototype, or evaluation harness. A day MAY teach a pattern that a
  project later uses; where a day's artifact and a project component would be the same code, the day
  MUST be re-scoped to the generic pattern.
- **FR-040**: Every Cloud & Infrastructure day entry MUST state an estimated cost and explicit
  teardown steps, MUST NOT be sequenced before the budget-alert and cost-monitoring day, and MUST
  require the teardown record as part of its completion gate.
- **FR-041**: The roadmap MUST be weighted for the **Germany and Europe** market as primary: applied
  project depth, system design, and production engineering MUST receive greater day allocation than
  algorithmic-screening volume, while DSA MUST remain at sufficient depth to serve FDE coding
  screens.
- **FR-042**: The roadmap MUST define the promotion milestones such that none is a close analogue of
  the learner's NDA-restricted thesis work (an agent that triages code review from merge requests),
  and MUST allow the flagship project choice to remain undecided until after programme week 4, with
  all candidate briefs maintained until then.

### Key Entities

- **Roadmap**: The whole programme. Has a duration, a start and end date, an ordered set of weeks, a
  set of promotion milestones, and a role-coverage mapping.
- **Week**: A named block of consecutive days with a theme, the domains it advances, its expected
  outcome, and exactly one review checkpoint.
- **Day Entry**: The atomic unit of work. Has a number, an objective, a target artifact, a
  verification step, a note topic, an effort estimate, a domain, a core/optional designation, a
  completion gate, optional prerequisites, and a minimum-viable fallback.
- **Domain**: One of the seven in-scope learning areas. Has a target depth and a mapping to the roles
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
- **SC-003**: All seven in-scope domains are advanced by at least one day, and no domain exceeds 30%
  of total programme days.
- **SC-004**: At the end of the programme the repository contains at least one committed, runnable
  artifact per completed day, each reproducible from a clean checkout.
- **SC-005**: Every DSA pattern and core ML concept introduced is scheduled for re-surfacing at least
  twice after its first completion.
- **SC-006**: In a simulated week with three missed days, applying the roadmap's recovery rules
  produces a re-planned following week with named cuts and no accumulated backlog.
- **SC-007**: At least three promotion milestones are defined, each naming its prerequisite days and
  supported roles, and none schedules implementation work inside this repository.
- **SC-008**: Each of the five in-scope target role families is traceable to the specific days that
  support it, with no in-scope role left unmapped.
- **SC-009**: The sum of effort estimates across all core (never-cut) day entries is at most 646
  hours — 85% of the 760-hour programme budget — leaving at least 15% slack for overruns, re-solves,
  and missed days.
- **SC-010**: An independent reader given only the roadmap and this repository can determine the
  learner's exact progress and the next action without consulting the learner.
- **SC-011**: Zero days outside the Cloud & Infrastructure domain require paid infrastructure or
  network-dependent resources to reach their completion gate, and every Cloud & Infrastructure day
  carries a cost estimate and a teardown record.
- **SC-012**: Day allocation across role tiers falls within 5 percentage points of the 60 / 25 / 15
  primary / secondary / remaining split, verifiable by counting day entries per tier.
- **SC-013**: Each of the three minimum-depth roles is supported by at least one completed artifact
  of the kind named in FR-032, so no in-scope target role is left with zero demonstrable evidence.
- **SC-014**: Every topic's `NOTES.md` carries all eleven sections required by FR-038 — verifiable
  by section-heading count across every topic directory, with zero partial templates.
- **SC-015**: Zero day entries produce an artifact under a promotion milestone's project scope,
  verifiable mechanically rather than by inspection.
- **SC-016**: Every day entry's main-artifact effort plus the daily DSA hour fits within its
  day-type budget, with zero days over.

## Assumptions

- **Audience**: The roadmap is written for a single self-directed learner working alone, not a cohort
  or a taught course.
- **Study rhythm**: The programme assumes near-daily study with occasional missed days treated as the
  norm rather than the exception; recovery rules are therefore mandatory rather than optional.
- **Duration**: Fixed at 19 calendar weeks — 133 day entries, Monday 2026-11-16 to Sunday
  2027-03-28 — derived from the 40-hour weekly budget and the learner's master's completion date of
  end-March 2027. The original "2–3 months" framing was superseded once that date was known.
- **Holiday period**: The programme spans late December. Weeks 6 and 7 are assumed to be the most
  likely to slip and are therefore the primary home for optional days and re-solve slots rather
  than for new core material.
- **Availability**: The learner's thesis and internship are complete and one academic credit
  remains, so the 40-hour weekly budget is treated as sustainable rather than competing with
  coursework. Job applications run in parallel and are out of scope for this repository.
- **Language**: Python is the implementation language for all days except where a concept cannot be
  demonstrated in Python, per the constitution.
- **Interview targeting**: "MANGOS" is interpreted as the large-tech hiring bar generally (Meta,
  Microsoft, Anthropic, Amazon, NVIDIA, Google, OpenAI); DSA weighting follows publicly observable
  interview-frequency patterns rather than any company-confidential material. With Germany and
  Europe as the primary market, DSA is treated as insurance against the minority of employers who
  screen algorithmically rather than as the programme's centre of gravity; the stated DSA budget is
  **not** assumed sufficient for a cold large-tech algorithmic loop.
- **Portfolio projects**: CV projects are built in separate repositories outside this directory and
  are out of scope for this feature; only their milestone definitions and pointer records live here.
- **Environment**: The learner works on a single Windows machine with no local GPU. Free hosted GPU
  (Colab or Kaggle) is assumed available for the few days that need one. An AWS student account with
  credits is available for the Cloud & Infrastructure domain, and a live LLM API budget of roughly
  $30–50 across the programme is assumed for the Applied AI days where fixtures teach materially
  less.
- **Existing knowledge**: The learner has roughly two years of applied ML/DL experience, a completed
  master's thesis building an agent orchestrator with retrieval and MCP, and an MLOps internship
  including fine-tuning a local model toward a frontier-model baseline. Introductory Python, LLM
  API, tool-calling and retrieval material is therefore out of scope. The genuine gaps — DSA, system
  design, inference and serving internals, cloud, and the production-engineering layer — are the
  subject of the programme.
- **Thesis IP**: The thesis code is owned by an industry partner and cannot be published or closely
  reproduced. No milestone or day may be a close analogue of a merge-request code-review triage
  agent.
- **Role weighting**: AI / Agentic AI Engineer is the primary target and FDE the secondary;
  ML/MLOps Engineer, Inference Engineer and AI Test Validation Engineer are covered to
  conversational depth with one demonstrable artifact each, not to interview depth. Embedded ML
  Engineer was dropped as a target: it requires C/C++ and hardware work that would dilute the two
  primary targets, and one artifact would not make the learner competitive for it.
- **Job outcome**: Securing a job depends on factors outside this repository (applications,
  interviews, market conditions). This feature's scope is interview readiness and portfolio
  readiness, not employment itself.
- **Governance**: The project constitution v1.1.0 governs this roadmap; its eight principles and
  daily quality gates are inputs to every day entry, not restated requirements.
