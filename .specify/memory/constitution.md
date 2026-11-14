<!--
SYNC IMPACT REPORT (temporary scratch material — remove before committing the amended file)

Version change: [unversioned template] → 1.0.0
Bump rationale: Initial ratification. All placeholder tokens replaced with concrete
governance for this project; no prior version existed, so this is a MAJOR baseline.

Modified principles (template slot → ratified principle):
- [PRINCIPLE_1_NAME] → I. Learn By Building (NON-NEGOTIABLE)
- [PRINCIPLE_2_NAME] → II. Daily Deliverable
- [PRINCIPLE_3_NAME] → III. From Scratch Before Framework
- [PRINCIPLE_4_NAME] → IV. Explain It Back
- [PRINCIPLE_5_NAME] → V. Measure, Don't Guess
- (added) → VI. Spaced Repetition Over Coverage
- (added) → VII. Playground Here, Production Elsewhere

Added sections:
- Scope & Learning Domains (was [SECTION_2_NAME])
- Learning Workflow & Quality Gates (was [SECTION_3_NAME])
- Governance (filled from [GOVERNANCE_RULES])

Removed sections: none.

Deferred items / follow-up TODOs:
- The 2-3 month roadmap with daily deliverables is NOT part of this constitution.
  It must be produced via `/speckit-specify` as the first feature of this repo.
- This directory is not yet a git repository; Principle VII and the workflow gates
  assume `git init` has been run. Initialize before the first learning day.
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

Every topic directory MUST contain a `NOTES.md` written in the author's own words that
states the problem the technique solves, its mechanism, its failure modes, and its
trade-offs. Copied text MUST be quoted and attributed; unattributed copying is a
violation. Notes MUST be written after the code works, not before.

Rationale: Written explanation is the cheapest available test of genuine understanding
and converts directly into interview answers and CV talking points.

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
be developed inside this one. Code may be promoted outward from here, never pulled
inward. Each promoted project MUST be recorded in this repository with its name, the
learnings it draws on, and a link.

Rationale: Mixing exploratory and production code destroys both — the playground becomes
too precious to experiment in, and the portfolio becomes too messy to show.

## Scope & Learning Domains

The following domains are in scope for this repository, and all MUST be represented by
committed artifacts before the program is considered complete:

- **Python**: language core, typing, packaging, testing, async, profiling.
- **Data Structures & Algorithms**: patterns weighted toward large-tech interview
  frequency (Meta, Microsoft, Anthropic, Amazon, NVIDIA, Google, OpenAI).
- **Git**: branching, rebase, bisect, conflict resolution, history hygiene.
- **System Design**: distributed fundamentals plus ML- and inference-specific
  architectures (serving, batching, caching, queues, feature stores).
- **ML & DL**: classical ML, neural network internals, training dynamics,
  transformers and attention, evaluation methodology.
- **Applied AI Engineering**: LLM APIs, retrieval, agentic patterns, inference
  optimization and quantization, and AI test/validation practice.

Constraints:

- Primary language is **Python**. Another language MAY be used only when the concept
  cannot be demonstrated in Python (e.g. kernel-level or embedded work), and the reason
  MUST be stated in that topic's `NOTES.md`.
- Dependencies MUST be pinned per topic and the environment MUST be reproducible from
  the repository alone.
- No secrets, API keys, proprietary datasets, or licensed course material may be
  committed.
- The repository MUST remain runnable on the author's own machine without paid
  infrastructure; anything requiring paid resources MUST degrade to a small local sample.

## Learning Workflow & Quality Gates

Daily loop:

1. Pick the day's objective from the active roadmap.
2. Write the failing test, assertion, or measurement first where the topic admits one.
3. Implement from scratch (Principle III), then the library comparison if applicable.
4. Record the measurement (Principle V).
5. Write or extend `NOTES.md` (Principle IV).
6. Commit with a message naming the topic and the day's objective.

A day's work MUST NOT be marked complete unless all of the following hold:

- The code runs from a clean checkout of the repository.
- Tests or assertions for the day's artifact pass, and failures are recorded rather
  than deleted.
- `NOTES.md` for the topic reflects what was actually built.
- The commit exists with a descriptive message.
- Any performance or accuracy claim has a committed measurement behind it.

Weekly review (MUST happen once per calendar week):

- Re-solve at least two previously completed DSA problems from a blank file.
- Audit the week's commits against this constitution and record violations.
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

- Every weekly review MUST check the week's commits against Principles I-VII.
- Expedience is not a justification for violation; a principle that proves genuinely
  unworkable MUST be amended rather than quietly ignored.
- Roadmap and task artifacts generated by Spec Kit commands in this repository MUST be
  checked against this constitution before execution begins.

**Version**: 1.0.0 | **Ratified**: 2026-11-14 | **Last Amended**: 2026-11-14
