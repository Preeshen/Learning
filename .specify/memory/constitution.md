<!--
SYNC IMPACT REPORT (temporary scratch material — remove before committing the amended file)

Version change: 1.0.0 → 1.1.0
Bump rationale: MINOR. One principle added (VIII), two principles materially expanded
(IV, VII), one domain added, one constraint set added. No principle removed or redefined
in a way that invalidates prior work, so this is not a MAJOR bump.

Modified principles:
- IV. Explain It Back → expanded from four free-form note headings to an eleven-section
  module template (objectives, prerequisites, concept, why, mechanisms, applications,
  alternatives, mistakes, interview questions, assessment, revision)
- VII. Playground Here, Production Elsewhere → tightened to bind individual day entries,
  not only promotion milestones

Added principles:
- VIII. Progressive Assistance (NON-NEGOTIABLE)

Added sections / content:
- Scope & Learning Domains: seventh domain "Cloud & Infrastructure"
- Scope & Learning Domains: programme parameters (19 weeks, 133 days, 760 h, roles, market)
- Scope & Learning Domains: "Cloud cost discipline" constraint block
- Learning Workflow & Quality Gates: module-template and teardown items in the day gate

Removed sections: none.

Deferred items / follow-up TODOs:
- Principle VII's tightening makes day entries 60, 61, 66 and 67 of the current
  roadmap non-compliant: they produce portfolio-project code inside this repository.
  Validator rule V-08 must be extended to day entries, and those four days re-pointed.
- Principle IV's expansion makes every existing topic `NOTES.md` incomplete (they carry
  four of eleven sections). The template and the thirteen existing topic directories
  must be updated.
- The seventh domain has no day entries yet; the Cloud & Infrastructure track is
  authored in `specs/002-curriculum-expansion`.
- Prior report's deferred items are resolved: the repository is initialised, and the
  roadmap exists at `roadmap/roadmap.yaml`.
-->

# AI Engineering Learning Playground Constitution

## Core Principles

### I. Learn By Building (NON-NEGOTIABLE)

Every concept studied MUST terminate in committed, runnable code in this repository.
Reading a paper, watching a lecture, or taking notes is preparation, never the
deliverable. A topic is "learned" only when an artifact exists that executes and that
the author can re-run from a clean checkout.

Rationale: Recognition memory from passive consumption collapses under interview and
on-the-job pressure. Hiring signal for AI engineering roles is demonstrated artifacts,
not syllabus coverage.

### II. Daily Deliverable

Each study day MUST produce at least one commit containing new or improved code, plus a
one-paragraph log entry recording: what was built, what broke, and the single concept
that was non-obvious. Zero-progress days MUST be logged explicitly as skipped rather
than silently omitted.

Rationale: A dated, honest commit history is both the accountability mechanism and the
evidence of consistency that reviewers and interviewers inspect.

### III. From Scratch Before Framework

For every foundational topic, a from-scratch implementation MUST precede any library or
framework use of the same idea. Examples: write backpropagation in NumPy before
`torch.autograd`; implement a hash map, heap, and graph traversal before reaching for
`collections` or `networkx`; hand-roll a retrieval loop before adopting an agent
framework. Once the from-scratch version passes its tests, the idiomatic library version
MUST be written alongside it for comparison.

Rationale: Framework-only knowledge fails under debugging, performance work, and
systems-design interviews. The pairing makes the abstraction's cost visible.

### IV. Explain It Back

Every topic directory MUST contain a `NOTES.md`, written in the author's own words after
the code works, containing all eleven of the following sections:

1. **Learning objectives** — what the author can do after this topic that they could not before.
2. **Prerequisites** — the concepts and prior topics this one assumes.
3. **Conceptual explanation** — the idea stated plainly, without code.
4. **Why it matters** — the engineering problem that makes this worth knowing.
5. **Internal mechanisms** — how it actually works underneath, not how to call it.
6. **Real-world applications** — where this appears in production systems.
7. **Alternatives and trade-offs** — what else solves this, and what each choice costs.
8. **Failure modes and common mistakes** — how it breaks, and the errors made while learning it.
9. **Interview questions** — at least three questions on this topic, with the author's answers.
10. **Assessment criteria** — how the author would judge whether someone understands this.
11. **Revision notes** — the compressed form to re-read before an interview.

Copied text MUST be quoted and attributed; unattributed copying is a violation.

Rationale: Written explanation is the cheapest available test of genuine understanding.
Free-form notes proved too easy to satisfy with four sentences; the fixed template forces
the specific recall — mechanisms, trade-offs, failure modes — that interviews probe and
that passive familiarity cannot fake.

### V. Measure, Don't Guess

Any claim about performance, accuracy, latency, or memory MUST be accompanied by a
reproducible measurement committed next to the code — a benchmark script, timing
harness, or evaluation run with its inputs recorded. DSA solutions MUST state asserted
time and space complexity and MUST be validated against test cases, including edge
cases. ML/DL work MUST report the metric, the dataset split, and the baseline it is
compared against.

Rationale: Inference, embedded-ML, and AI-validation roles are measurement roles.
Unmeasured claims are the single most common disqualifier in technical screens.

### VI. Spaced Repetition Over Coverage

Breadth MUST NOT outrun retention. DSA patterns and core ML concepts MUST be revisited
on a spaced schedule, and a previously solved problem re-solved from a blank file counts
as a valid daily deliverable. When time is scarce, revision of fragile material takes
priority over starting new material.

Rationale: Interview performance is a function of retrieval speed under pressure, not of
topics once touched.

### VII. Playground Here, Production Elsewhere

This repository is a learning playground: experiments, dead ends, and deliberately naive
implementations are welcome and MUST be kept rather than deleted. CV-facing,
production-deployable projects MUST live in their own separate repositories and MUST NOT
be developed inside this one.

This binds **individual day entries as well as promotion milestones**. No day entry may
produce an artifact that implements a portfolio project — including its scaffold, its
core, a prototype of it, or its evaluation harness. A day may teach a pattern that a
project later uses; it may not build the project. Where a day's artifact and a project's
component would be the same code, the day MUST be re-scoped to the generic pattern.

Code may be promoted outward from here, never pulled inward. Each promoted project MUST
be recorded in this repository with its name, the learnings it draws on, and a link.
Project briefs, technical prerequisites, architecture references and readiness checklists
MAY live here; project source code MUST NOT.

Rationale: Mixing exploratory and production code destroys both — the playground becomes
too precious to experiment in, and the portfolio becomes too messy to show. The milestone-
level rule proved insufficient: day entries named after milestones were building the
projects while automated checks passed.

### VIII. Progressive Assistance (NON-NEGOTIABLE)

Code MUST NOT be ghostwritten for the author. Assistance MUST escalate in this order, and
MUST NOT skip ahead:

1. Explain the concept.
2. Give hints toward the approach.
3. Provide a typed skeleton — signatures, asserted complexity, and the mechanism stated in
   the docstring, with the body left as `NotImplementedError`.
4. Help debug the author's own attempt.
5. Provide a complete reference solution only after a genuine attempt, or on the author's
   explicit request for one.

A committed artifact the author did not write themselves is not a learning artifact and
MUST be reverted, regardless of whether it passes its tests.

Rationale: This rule was already enforced in practice before it was written down — commit
`243659d` reverted thirteen days of solutions as "ghostwritten, not learned". A rule that
exists only as a commit message will not survive a week of time pressure. The whole value
of this repository is the author's ability to produce this code unaided; an artifact that
demonstrates otherwise is worse than an empty directory, because it hides the gap.

## Scope & Learning Domains

**Programme parameters**: 19 weeks and 133 day entries, budgeted at 760 focused hours
(6 h per weekday, 5 h per weekend day), ending March 2027. Primary target role is
**AI / Agentic AI Engineer**; secondary is **Forward Deployed Engineer**; ML/MLOps
Engineer leads the remaining tier, followed by Inference Engineer and AI Test Validation
Engineer. Primary target market is **Germany and Europe**, which weights applied project
depth and system design above algorithmic screening volume.

The following domains are in scope for this repository, and all MUST be represented by
committed artifacts before the program is considered complete:

- **Python**: language core, typing, packaging, testing, async, profiling, OOP, object
  model and memory internals, and software engineering principles including clean code,
  SOLID, and design patterns.
- **Data Structures & Algorithms**: patterns weighted toward large-tech interview
  frequency (Meta, Microsoft, Anthropic, Amazon, NVIDIA, Google, OpenAI). This domain
  MUST run as a continuous daily track across the whole programme, not as a block of
  consecutive days, because retrieval speed depends on distributed practice.
- **Git & Linux**: branching, rebase, bisect, conflict resolution, history hygiene, and
  the shell, filesystem, process and networking basics required to operate a deployed
  service.
- **System Design**: networking and HTTP, REST API design, SQL and NoSQL data modelling
  and indexing, caching, queues and event-driven architecture, microservices, distributed
  fundamentals (CAP, replication, partitioning, load balancing, fault tolerance),
  authentication and authorisation, observability, and ML- and inference-specific
  architectures (serving, batching, feature stores).
- **ML & DL**: applied mathematics essentials, classical ML, feature engineering, neural
  network internals, training dynamics, transformers and attention, evaluation
  methodology, and the MLOps lifecycle — pipelines, registries, drift, and serving.
- **Applied AI Engineering**: LLM internals (tokenisation, embeddings, decoding,
  fine-tuning and parameter-efficient adaptation), retrieval and its evaluation, agentic
  patterns, agent and interoperability protocols, inference optimization and quantization,
  production serving, observability and tracing, guardrails and adversarial testing, and
  AI test/validation practice.
- **Cloud & Infrastructure**: identity and least-privilege access, object storage,
  serverless compute and API gateways, managed NoSQL, queues and pub/sub, container
  registry and orchestration, managed model-hosting services, and cloud observability and
  cost monitoring.

Constraints:

- Primary language is **Python**. Another language MAY be used only when the concept
  cannot be demonstrated in Python (e.g. kernel-level or embedded work), and the reason
  MUST be stated in that topic's `NOTES.md`.
- Dependencies MUST be pinned per topic and the environment MUST be reproducible from
  the repository alone.
- No secrets, API keys, proprietary datasets, or licensed course material may be
  committed. Work covered by a third-party agreement MUST NOT be reproduced here, and no
  artifact may be a close public analogue of work owned by another party.
- Committed artifacts and their tests MUST run from a clean checkout on the author's own
  machine without paid infrastructure. Anything otherwise requiring paid resources MUST
  degrade to a small local sample. Cloud & Infrastructure exercises are the sole
  exception, governed by the cloud cost discipline below; each such day MUST still commit
  an artifact — configuration, infrastructure definition, measurements, and a teardown
  record — that is reviewable without access to the cloud account.

Cloud cost discipline (applies to every Cloud & Infrastructure day and any paid resource):

- Budget alerts and cost monitoring MUST exist and be verified **before** any cloud
  resource is provisioned. This is the first cloud exercise, not a later one.
- Every cloud exercise MUST carry an estimated cost before it begins and explicit
  teardown steps, and the teardown MUST be executed and verified complete on the same day.
- Current published pricing MUST be checked when the exercise is authored. No service may
  be assumed free, and free-tier eligibility MUST be confirmed rather than presumed.
- No paid resource may be provisioned without the author's explicit per-exercise approval.

## Learning Workflow & Quality Gates

Daily loop:

1. Pick the day's objective from the active roadmap.
2. Write the failing test, assertion, or measurement first where the topic admits one.
3. Implement from scratch (Principle III), then the library comparison if applicable.
4. Record the measurement (Principle V).
5. Write or extend `NOTES.md` against the eleven-section template (Principle IV).
6. Commit with a message naming the topic and the day's objective.

A day's work MUST NOT be marked complete unless all of the following hold:

- The code runs from a clean checkout of the repository.
- Tests or assertions for the day's artifact pass, and failures are recorded rather
  than deleted.
- The implementation was written by the author, not generated for them (Principle VIII).
- `NOTES.md` for the topic reflects what was actually built and carries all eleven
  required sections.
- The commit exists with a descriptive message.
- Any performance or accuracy claim has a committed measurement behind it.
- For a cloud day, teardown has been executed and the teardown record is committed.

Weekly review (MUST happen once per calendar week):

- Re-solve at least two previously completed DSA problems from a blank file.
- Audit the week's commits against this constitution and record violations.
- Reconcile cloud spend against the budget if any cloud exercise ran.
- Re-plan the coming week, explicitly cutting scope rather than accumulating a backlog.

## Governance

This constitution supersedes ad-hoc study habits and any conflicting advice embedded in
tutorials, courses, or generated plans. When a roadmap, specification, task list, or
mentor suggestion conflicts with a principle here, this document wins and the conflict
MUST be recorded in the weekly review.

Amendment procedure:

1. Propose the change in writing, naming the principle affected and the problem observed.
2. Apply the amendment to this file with an updated Sync Impact Report.
3. Commit the amendment separately from learning work, using a `docs:` commit.

Versioning policy (semantic):

- **MAJOR**: a principle is removed or redefined in a way that invalidates prior work.
- **MINOR**: a principle or section is added, or guidance is materially expanded.
- **PATCH**: clarification, wording, or typo fixes with no change in obligation.

Compliance review:

- Every weekly review MUST check the week's commits against Principles I-VIII.
- Expedience is not a justification for violation; a principle that proves genuinely
  unworkable MUST be amended rather than quietly ignored.
- Roadmap and task artifacts generated by Spec Kit commands in this repository MUST be
  checked against this constitution before execution begins.
- Where a principle can be mechanically enforced, it SHOULD be — a validator rule or a
  gate check is preferred to a self-assessment, because self-assessment is what fails
  under time pressure.

**Version**: 1.1.0 | **Ratified**: 2026-11-14 | **Last Amended**: 2026-11-15
