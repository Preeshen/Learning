# Roadmap (generated — do not hand-edit; see roadmap.yaml)

133 days · 19 weeks · 2026-11-16 to 2027-03-28

## Week 1 — Python engineering depth

Domains: python, dsa · Outcome: Typed, tested, packaged, profiled Python with a committed lockfile.

### Day 1 — 2026-11-16 (weekday, 5.0h, core)

- **Domain/Topic**: python / project-tooling
- **Objective**: Stand up the repo toolchain and complete the worked example day.
- **Artifact**: `python/project-tooling/env_report.py`
- **Verification**: pytest python/project-tooling/ passes; roadmap validate exits 0
- **Notes topic**: Why a committed lockfile is the difference between reproducible and 'works here'
- **Minimum viable**: Toolchain installed and `roadmap today` runs; defer the notes.

### Day 2 — 2026-11-17 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / arrays-hashing
- **Objective**: Solve the arrays, hashing and prefix sums pattern from scratch with a shared test harness.
- **Artifact**: `dsa/arrays-hashing/solutions.py`
- **Verification**: pytest dsa/arrays-hashing/ passes; complexity asserted per solution
- **Notes topic**: What the arrays, hashing and prefix sums pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 3 — 2026-11-18 (weekday, 5.0h, core)

- **Domain/Topic**: python / python-typing-static-analysis
- **Objective**: Add precise type hints to a deliberately under-typed module and make mypy --strict pass.
- **Artifact**: `python/python-typing-static-analysis/typed_pipeline.py`
- **Verification**: mypy --strict passes; pytest python/python-typing-static-analysis/ passes
- **Notes topic**: What --strict catches that ordinary annotations do not
- **Minimum viable**: Reduced scope: the core case only, tested.

### Day 4 — 2026-11-19 (weekday, 5.0h, core)

- **Domain/Topic**: python / python-oop-object-model
- **Objective**: Implement a descriptor, a context manager and __slots__, and measure the memory difference.
- **Artifact**: `python/python-oop-object-model/model.py`
- **Verification**: pytest passes; benchmarks.json records __slots__ memory delta vs plain class
- **Notes topic**: What a descriptor is actually doing when you write obj.attr
- **Minimum viable**: Reduced scope: the core case only, tested.

### Day 5 — 2026-11-20 (weekday, 5.0h, core)

- **Domain/Topic**: python / python-async-concurrency
- **Objective**: Implement the same IO-bound fan-out three ways: threads, asyncio, and sequential.
- **Artifact**: `python/python-async-concurrency/fanout.py`
- **Verification**: pytest passes; benchmarks.json compares all three against sequential
- **Notes topic**: Why asyncio wins on IO and loses on CPU, in terms of the GIL
- **Minimum viable**: Reduced scope: the core case only, tested.

### Day 6 — 2026-11-21 (weekend, 4.0h, core)

- **Domain/Topic**: python / python-profiling
- **Objective**: Profile a deliberately slow function, find the hot path, fix it, and prove the speedup.
- **Artifact**: `python/python-profiling/hotpath.py`
- **Verification**: pytest passes; benchmarks.json shows before/after against the unoptimised baseline
- **Notes topic**: Why wall-clock timing misleads and what cProfile shows instead
- **Minimum viable**: Reduced scope: the core case only, tested.

### Day 7 — 2026-11-22 (weekend, 4.0h, core)

- **Domain/Topic**: python / project-tooling
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-01.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 7): resolves arrays-hashing, arrays-hashing

## Week 2 — Clean code, SOLID and design patterns

Domains: python, dsa · Outcome: Refactoring vocabulary and the patterns that show up in system-design interviews.

### Day 8 — 2026-11-23 (weekday, 5.0h, core)

- **Domain/Topic**: python / solid-principles
- **Objective**: Refactor a deliberately god-classed module into single-responsibility units.
- **Artifact**: `python/solid-principles/refactored.py`
- **Verification**: pytest passes before and after; behaviour unchanged
- **Notes topic**: Which SOLID letters actually change designs and which are restatements
- **Minimum viable**: Reduced scope: the core case only, tested.

### Day 9 — 2026-11-24 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / two-pointers
- **Objective**: Solve the two pointers pattern from scratch with a shared test harness.
- **Artifact**: `dsa/two-pointers/solutions.py`
- **Verification**: pytest dsa/two-pointers/ passes; complexity asserted per solution
- **Notes topic**: What the two pointers pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 10 — 2026-11-25 (weekday, 5.0h, core)

- **Domain/Topic**: python / design-patterns-creational
- **Objective**: Implement factory, builder and adapter where each genuinely earns its place.
- **Artifact**: `python/design-patterns-creational/patterns.py`
- **Verification**: pytest passes for each pattern's contract
- **Notes topic**: When a factory is indirection that pays and when it is ceremony
- **Minimum viable**: Reduced scope: the core case only, tested.

### Day 11 — 2026-11-26 (weekday, 5.0h, optional)

- **Domain/Topic**: python / error-handling-design
- **Objective**: Design an exception hierarchy and a result type, and show where each is the better fit.
- **Artifact**: `python/error-handling-design/errors.py`
- **Verification**: pytest covers both the raising and the result-returning paths
- **Notes topic**: When exceptions are control flow and when they are a leaked implementation detail
- **Minimum viable**: Reduced scope: the core case only, tested.

### Day 12 — 2026-11-27 (weekday, 5.0h, core)

- **Domain/Topic**: python / dependency-injection-testability
- **Objective**: Make an untestable module testable by inverting its dependencies; no mocking library.
- **Artifact**: `python/dependency-injection-testability/service.py`
- **Verification**: pytest passes with a hand-written fake, no mock patching
- **Notes topic**: Why patching is a smell and injection is the fix
- **Minimum viable**: Reduced scope: the core case only, tested.

### Day 13 — 2026-11-28 (weekend, 4.0h, optional)

- **Domain/Topic**: python / code-review-practice
- **Objective**: Take an unfamiliar open-source module, map it, and write a reviewer's summary of its design.
- **Artifact**: `python/code-review-practice/REVIEW.md`
- **Verification**: The review names the module's entry points, invariants and one real weakness
- **Notes topic**: How to orient in unfamiliar code fast — the FDE core skill
- **Minimum viable**: Reduced scope: the core case only, tested.

### Day 14 — 2026-11-29 (weekend, 4.0h, core)

- **Domain/Topic**: python / solid-principles
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-02.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 14): resolves two-pointers, arrays-hashing

## Week 3 — LLM internals from scratch

Domains: applied-ai, dsa · Outcome: Tokenisation, embeddings and decoding understood at mechanism level, not API level.

### Day 15 — 2026-11-30 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / tokenisation-bpe
- **Objective**: Implement byte-pair encoding from scratch and compare its token counts to a real tokenizer.
- **Artifact**: `applied-ai/tokenisation-bpe/bpe.py`
- **Verification**: pytest passes; benchmarks.json compares token counts against a reference tokenizer
- **Notes topic**: Why token count is not word count, and what that does to cost
- **Minimum viable**: BPE merges implemented and tested; defer the comparison.

### Day 16 — 2026-12-01 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / sliding-window
- **Objective**: Solve the sliding window pattern from scratch with a shared test harness.
- **Artifact**: `dsa/sliding-window/solutions.py`
- **Verification**: pytest dsa/sliding-window/ passes; complexity asserted per solution
- **Notes topic**: What the sliding window pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 17 — 2026-12-02 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / decoding-strategies
- **Objective**: Implement greedy, top-k, top-p and temperature sampling over a fixed logit distribution.
- **Artifact**: `applied-ai/decoding-strategies/decode.py`
- **Verification**: pytest passes; output distributions differ measurably per strategy
- **Notes topic**: What temperature actually multiplies, and why top-p beats top-k
- **Minimum viable**: Greedy and temperature done; defer top-p.

### Day 18 — 2026-12-03 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / structured-output-parsing
- **Objective**: Build a parse-validate-repair loop for malformed model JSON against a schema.
- **Artifact**: `applied-ai/structured-output-parsing/parse.py`
- **Verification**: pytest covers 5 malformed-output cases including truncation
- **Notes topic**: Why repairing a malformed parse is not the same as retrying a failed call
- **Minimum viable**: Happy path plus one malformed case.

### Day 19 — 2026-12-04 (weekday, 5.0h, optional)

- **Domain/Topic**: applied-ai / finetuning-lora
- **Objective**: Implement a LoRA adapter forward pass from scratch and count its trainable parameters.
- **Artifact**: `applied-ai/finetuning-lora/lora.py`
- **Verification**: pytest passes; benchmarks.json reports trainable-parameter ratio vs full fine-tuning
- **Notes topic**: Why low-rank adaptation works at all, in terms of the update matrix rank
- **Minimum viable**: Adapter forward pass implemented and tested.

### Day 20 — 2026-12-05 (weekend, 4.0h, core)

- **Domain/Topic**: applied-ai / prompt-engineering-eval-harness
- **Objective**: Build a harness that scores prompt variants on a fixed labelled set rather than on impression.
- **Artifact**: `applied-ai/prompt-engineering-eval-harness/harness.py`
- **Verification**: pytest passes; harness reports per-variant accuracy against a committed labelled set
- **Notes topic**: Why a prompt change without an eval set is a guess
- **Minimum viable**: Harness scores two variants on 10 items.

### Day 21 — 2026-12-06 (weekend, 4.0h, core)

- **Domain/Topic**: applied-ai / tokenisation-bpe
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-03.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 21): resolves arrays-hashing, sliding-window

## Week 4 — Agentic control flow depth

Domains: applied-ai, dsa · Outcome: Agent loops, memory, reflection and human-in-the-loop built from scratch.

### Day 22 — 2026-12-07 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / react-loop-scratch
- **Objective**: Implement a ReAct reason-act-observe loop in stdlib Python with no agent framework.
- **Artifact**: `applied-ai/react-loop-scratch/react.py`
- **Verification**: pytest covers a 3-step task and a loop-limit termination case
- **Notes topic**: What ReAct actually prescribes versus what frameworks add on top
- **Minimum viable**: Single-step loop with one tool.

### Day 23 — 2026-12-08 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / binary-search
- **Objective**: Solve the binary search pattern from scratch with a shared test harness.
- **Artifact**: `dsa/binary-search/solutions.py`
- **Verification**: pytest dsa/binary-search/ passes; complexity asserted per solution
- **Notes topic**: What the binary search pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 24 — 2026-12-09 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / agent-memory-state
- **Objective**: Implement window, summary and retrieval-backed memory behind one interface.
- **Artifact**: `applied-ai/agent-memory-state/memory.py`
- **Verification**: pytest passes for all three strategies; context overflow is handled
- **Notes topic**: Why conversation memory is a compression problem, not a storage problem
- **Minimum viable**: Window memory only.

### Day 25 — 2026-12-10 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / agent-reflection-critique
- **Objective**: Add a critic pass over the agent output and measure whether it actually helps.
- **Artifact**: `applied-ai/agent-reflection-critique/reflect.py`
- **Verification**: pytest passes; benchmarks.json reports pass-rate with and without the critic
- **Notes topic**: When reflection improves output and when it just burns tokens
- **Minimum viable**: Critic pass wired in; defer measurement.

### Day 26 — 2026-12-11 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / agent-human-in-the-loop
- **Objective**: Implement propose-then-commit with an approval boundary and an action budget.
- **Artifact**: `applied-ai/agent-human-in-the-loop/approval.py`
- **Verification**: pytest proves no side-effecting tool runs before approval and the budget halts the loop
- **Notes topic**: Why an action budget is a safety mechanism, not only a cost mechanism
- **Minimum viable**: Approval boundary enforced for one tool.

### Day 27 — 2026-12-12 (weekend, 4.0h, core)

- **Domain/Topic**: applied-ai / agent-error-handling
- **Objective**: Handle malformed tool arguments, tool exceptions and non-termination distinctly.
- **Artifact**: `applied-ai/agent-error-handling/resilient.py`
- **Verification**: pytest covers all three failure classes separately
- **Notes topic**: Why a malformed call is a prompt bug and a tool exception is not
- **Minimum viable**: Malformed-argument path handled.

### Day 28 — 2026-12-13 (weekend, 4.0h, core)

- **Domain/Topic**: applied-ai / react-loop-scratch
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-04.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 28): resolves two-pointers, binary-search

## Week 5 — Evaluation and observability

Domains: applied-ai, systems, dsa · Outcome: Non-deterministic systems measured, traced and regression-gated.

### Day 29 — 2026-12-14 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / eval-nondeterministic-systems
- **Objective**: Build an eval harness reporting confidence intervals over repeated runs, not single scores.
- **Artifact**: `applied-ai/eval-nondeterministic-systems/evaluate.py`
- **Verification**: pytest passes; harness reports mean and CI over at least 5 runs per item
- **Notes topic**: Why a single eval run tells you almost nothing
- **Minimum viable**: Harness runs an item 5 times and reports the mean.

### Day 30 — 2026-12-15 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / sorting-algorithms
- **Objective**: Solve the sorting pattern from scratch with a shared test harness.
- **Artifact**: `dsa/sorting-algorithms/solutions.py`
- **Verification**: pytest dsa/sorting-algorithms/ passes; complexity asserted per solution
- **Notes topic**: What the sorting pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 31 — 2026-12-16 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / agent-trajectory-eval
- **Objective**: Score whole agent trajectories against labelled traces, not just final answers.
- **Artifact**: `applied-ai/agent-trajectory-eval/trajectory.py`
- **Verification**: pytest passes; a right answer reached via wrong steps scores lower
- **Notes topic**: Why final-answer accuracy hides the failures that matter in production
- **Minimum viable**: Trajectory scored on step overlap alone.

### Day 32 — 2026-12-17 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / llm-regression-gates
- **Objective**: Build a release gate that fails when eval scores drop beyond a threshold.
- **Artifact**: `applied-ai/llm-regression-gates/gate.py`
- **Verification**: pytest proves the gate fails on a seeded regression and passes on noise
- **Notes topic**: How to separate a real regression from run-to-run variance
- **Minimum viable**: Gate fires on a hardcoded threshold.

### Day 33 — 2026-12-18 (weekday, 5.0h, core)

- **Domain/Topic**: systems / observability-tracing
- **Objective**: Instrument this week's agent with spans and attributes, then inspect the trace tree.
- **Artifact**: `systems/observability-tracing/tracing.py`
- **Verification**: pytest passes; a committed trace shows nested spans with timings
- **Notes topic**: What a span is, and why log lines cannot reconstruct a causal tree
- **Minimum viable**: Spans emitted for one nested call.

### Day 34 — 2026-12-19 (weekend, 4.0h, core)

- **Domain/Topic**: systems / observability-metrics-slos
- **Objective**: Compute TTFT and p50/p95/p99 plus error rate over a simulated request stream.
- **Artifact**: `systems/observability-metrics-slos/metrics.py`
- **Verification**: pytest passes; benchmarks.json reports the percentile table
- **Notes topic**: Why p99 rather than the mean, and what an SLO commits you to
- **Minimum viable**: p50 and p95 computed.

### Day 35 — 2026-12-20 (weekend, 4.0h, core)

- **Domain/Topic**: applied-ai / eval-nondeterministic-systems
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan. Milestone readiness check: Agent evaluation and observability platform.
- **Artifact**: `progress/reviews/week-05.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 35): resolves sliding-window, sorting-algorithms

## Week 6 — Retrieval depth

Domains: applied-ai, dsa · Outcome: Hybrid retrieval, reranking and query rewriting, each measured against a baseline.

### Day 36 — 2026-12-21 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / retrieval-vector-search
- **Objective**: Implement brute-force and an approximate index, then measure the recall/latency trade-off.
- **Artifact**: `applied-ai/retrieval-vector-search/index.py`
- **Verification**: pytest passes; benchmarks.json plots recall against latency vs brute force
- **Notes topic**: What ANN gives up to go fast, and when that trade is wrong
- **Minimum viable**: Brute-force search with tests.

### Day 37 — 2026-12-22 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / linked-lists
- **Objective**: Solve the linked lists pattern from scratch with a shared test harness.
- **Artifact**: `dsa/linked-lists/solutions.py`
- **Verification**: pytest dsa/linked-lists/ passes; complexity asserted per solution
- **Notes topic**: What the linked lists pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 38 — 2026-12-23 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / retrieval-hybrid-bm25
- **Objective**: Implement BM25, fuse it with dense retrieval, and measure whether fusion actually wins.
- **Artifact**: `applied-ai/retrieval-hybrid-bm25/hybrid.py`
- **Verification**: pytest passes; benchmarks.json compares BM25, dense and fused
- **Notes topic**: Why lexical retrieval still beats embeddings on some queries
- **Minimum viable**: BM25 implemented and tested.

### Day 39 — 2026-12-24 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / retrieval-reranking
- **Objective**: Add a reranking stage over the top-k candidates and measure the precision gain and its cost.
- **Artifact**: `applied-ai/retrieval-reranking/rerank.py`
- **Verification**: pytest passes; benchmarks.json reports precision and added latency vs no reranker
- **Notes topic**: Why retrieve-then-rerank beats retrieving more documents
- **Minimum viable**: Reranker applied to top-10; defer measurement.

### Day 40 — 2026-12-25 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / retrieval-query-rewriting
- **Objective**: Implement query rewriting and multi-query expansion, measuring recall change.
- **Artifact**: `applied-ai/retrieval-query-rewriting/rewrite.py`
- **Verification**: pytest passes; benchmarks.json reports recall before and after rewriting
- **Notes topic**: Why the user query is rarely the best retrieval query
- **Minimum viable**: Single rewrite strategy implemented.

### Day 41 — 2026-12-26 (weekend, 4.0h, optional)

- **Domain/Topic**: applied-ai / retrieval-agentic-rag
- **Objective**: Let the agent decide whether and what to retrieve, then measure against always-retrieve.
- **Artifact**: `applied-ai/retrieval-agentic-rag/agentic.py`
- **Verification**: pytest passes; benchmarks.json compares against the always-retrieve baseline
- **Notes topic**: When skipping retrieval is the right call, and how the agent should know
- **Minimum viable**: Agent chooses retrieve or not on one decision rule.

### Day 42 — 2026-12-27 (weekend, 4.0h, core)

- **Domain/Topic**: applied-ai / retrieval-vector-search
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-06.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 42): resolves binary-search, linked-lists

## Week 7 — Production frameworks

Domains: applied-ai, dsa · Outcome: LangGraph, LangChain and LlamaIndex, each compared against the scratch build.

### Day 43 — 2026-12-28 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / langgraph-state-graphs
- **Objective**: Rebuild the week-4 ReAct agent as a LangGraph state machine and diff the two designs.
- **Artifact**: `applied-ai/langgraph-state-graphs/graph.py`
- **Verification**: pytest passes; the graph handles the same 3-step task as the scratch loop
- **Notes topic**: What a state graph makes explicit that an imperative loop hides
- **Minimum viable**: Two-node graph running end to end.

### Day 44 — 2026-12-29 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / stacks-queues-monotonic
- **Objective**: Solve the stacks, queues and monotonic stacks pattern from scratch with a shared test harness.
- **Artifact**: `dsa/stacks-queues-monotonic/solutions.py`
- **Verification**: pytest dsa/stacks-queues-monotonic/ passes; complexity asserted per solution
- **Notes topic**: What the stacks, queues and monotonic stacks pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 45 — 2026-12-30 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / langgraph-checkpointing
- **Objective**: Add checkpointing so an interrupted run resumes from its last node.
- **Artifact**: `applied-ai/langgraph-checkpointing/resume.py`
- **Verification**: pytest kills a run mid-graph and proves it resumes without repeating work
- **Notes topic**: Why durable execution matters more than retry logic for long agent runs
- **Minimum viable**: Checkpoint written and reloaded.

### Day 46 — 2026-12-31 (weekday, 5.0h, optional)

- **Domain/Topic**: applied-ai / langchain-abstractions
- **Objective**: Implement one chain with LangChain and the same behaviour without it; compare both.
- **Artifact**: `applied-ai/langchain-abstractions/chain.py`
- **Verification**: pytest passes for both implementations with identical outputs
- **Notes topic**: Which LangChain abstractions pay for themselves and which you would avoid in production
- **Minimum viable**: LangChain version only; note the comparison as pending.

### Day 47 — 2027-01-01 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / framework-selection-tradeoffs
- **Objective**: Write a decision record choosing a framework for a stated scenario, with evidence.
- **Artifact**: `applied-ai/framework-selection-tradeoffs/DECISION.md`
- **Verification**: The record names criteria, evidence from this week, and what would change the decision
- **Notes topic**: How to defend a framework choice in an interview without sounding dogmatic
- **Minimum viable**: Criteria table plus a provisional choice.

### Day 48 — 2027-01-02 (weekend, 4.0h, core)

- **Domain/Topic**: applied-ai / serving-agents-fastapi
- **Objective**: Wrap the agent behind FastAPI with streaming, timeouts and structured errors.
- **Artifact**: `applied-ai/serving-agents-fastapi/app.py`
- **Verification**: pytest passes against the ASGI test client, including a timeout case
- **Notes topic**: Why streaming changes your error-handling design
- **Minimum viable**: Non-streaming endpoint with tests.

### Day 49 — 2027-01-03 (weekend, 4.0h, core)

- **Domain/Topic**: applied-ai / langgraph-state-graphs
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-07.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 49): resolves sorting-algorithms, stacks-queues-monotonic

## Week 8 — Protocols and security

Domains: applied-ai, dsa · Outcome: MCP in depth, A2A, and the adversarial surface of tool-using systems.

### Day 50 — 2027-01-04 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / mcp-server-client
- **Objective**: Implement an MCP server over stdio and a client that discovers and calls its tools.
- **Artifact**: `applied-ai/mcp-server-client/server.py`
- **Verification**: pytest passes; the client lists tools and completes a round trip
- **Notes topic**: What MCP standardises that a bespoke tool interface does not
- **Minimum viable**: Server exposes one tool and the client calls it.

### Day 51 — 2027-01-05 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / trees-traversals
- **Objective**: Solve the trees and traversals pattern from scratch with a shared test harness.
- **Artifact**: `dsa/trees-traversals/solutions.py`
- **Verification**: pytest dsa/trees-traversals/ passes; complexity asserted per solution
- **Notes topic**: What the trees and traversals pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 52 — 2027-01-06 (weekday, 5.0h, optional)

- **Domain/Topic**: applied-ai / mcp-resources-prompts
- **Objective**: Extend the server with resources and prompt templates, not just tools.
- **Artifact**: `applied-ai/mcp-resources-prompts/resources.py`
- **Verification**: pytest covers resource listing, reading and a parameterised prompt
- **Notes topic**: Why resources and prompts are separate primitives from tools
- **Minimum viable**: Resource listing and reading only.

### Day 53 — 2027-01-07 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / mcp-security-auth
- **Objective**: Add scoped permissions, a path jail and an audit log to the MCP server.
- **Artifact**: `applied-ai/mcp-security-auth/secure.py`
- **Verification**: pytest proves a tool cannot escape its path jail and every call is audited
- **Notes topic**: Why tool scoping is the real security boundary in an agent system
- **Minimum viable**: Path jail enforced and tested.

### Day 54 — 2027-01-08 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / prompt-injection-defence
- **Objective**: Build an injection test suite against the week-7 agent and then defend against it.
- **Artifact**: `applied-ai/prompt-injection-defence/injection.py`
- **Verification**: pytest includes 6 injection attempts; the defended agent resists all of them
- **Notes topic**: Why prompt injection is an architecture problem, not a prompt problem
- **Minimum viable**: Three injection cases and one defence.

### Day 55 — 2027-01-09 (weekend, 4.0h, core)

- **Domain/Topic**: applied-ai / guardrails-data-leakage
- **Objective**: Implement input and output guardrails including PII scrubbing, and measure false positives.
- **Artifact**: `applied-ai/guardrails-data-leakage/guardrails.py`
- **Verification**: pytest passes; benchmarks.json reports catch rate and false-positive rate
- **Notes topic**: Why a guardrail that blocks too much is also a failure
- **Minimum viable**: Output scrubbing for one PII class.

### Day 56 — 2027-01-10 (weekend, 4.0h, core)

- **Domain/Topic**: applied-ai / mcp-server-client
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-08.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 56): resolves linked-lists, trees-traversals

## Week 9 — Networking, HTTP and API design

Domains: systems, dsa · Outcome: The request path understood end to end, and APIs designed rather than accreted.

### Day 57 — 2027-01-11 (weekday, 5.0h, core)

- **Domain/Topic**: systems / networking-tcp-http
- **Objective**: Implement a minimal HTTP server on raw sockets and trace a request through it.
- **Artifact**: `systems/networking-tcp-http/server.py`
- **Verification**: pytest passes; the server handles keep-alive and a malformed request
- **Notes topic**: What happens between DNS and your handler function
- **Minimum viable**: Single-request server, no keep-alive.

### Day 58 — 2027-01-12 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / trees-bst
- **Objective**: Solve the binary search trees pattern from scratch with a shared test harness.
- **Artifact**: `dsa/trees-bst/solutions.py`
- **Verification**: pytest dsa/trees-bst/ passes; complexity asserted per solution
- **Notes topic**: What the binary search trees pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 59 — 2027-01-13 (weekday, 5.0h, core)

- **Domain/Topic**: systems / rest-api-design
- **Objective**: Design and implement a resource API with pagination, filtering and consistent errors.
- **Artifact**: `systems/rest-api-design/api.py`
- **Verification**: pytest covers pagination boundaries, bad input and the error envelope
- **Notes topic**: Why cursor pagination beats offset at scale
- **Minimum viable**: CRUD plus offset pagination.

### Day 60 — 2027-01-14 (weekday, 5.0h, core)

- **Domain/Topic**: systems / api-versioning-contracts
- **Objective**: Evolve an API without breaking a client, and prove it with contract tests.
- **Artifact**: `systems/api-versioning-contracts/versioned.py`
- **Verification**: pytest runs the old client against the new API and passes
- **Notes topic**: Which changes are backward compatible and which only look it
- **Minimum viable**: One additive change with a contract test.

### Day 61 — 2027-01-15 (weekday, 5.0h, core)

- **Domain/Topic**: systems / auth-authz
- **Objective**: Implement token auth plus role-based authorisation, and test the bypass attempts.
- **Artifact**: `systems/auth-authz/auth.py`
- **Verification**: pytest covers expired tokens, wrong roles and a privilege-escalation attempt
- **Notes topic**: Why authentication and authorisation fail in different places
- **Minimum viable**: Token validation and one role check.

### Day 62 — 2027-01-16 (weekend, 4.0h, core)

- **Domain/Topic**: systems / rate-limiting-backpressure
- **Objective**: Implement token-bucket and sliding-window limiters and measure behaviour under overload.
- **Artifact**: `systems/rate-limiting-backpressure/limiter.py`
- **Verification**: pytest passes; benchmarks.json shows accepted vs rejected under a burst
- **Notes topic**: Why shedding load early beats queueing it
- **Minimum viable**: Token bucket with tests.

### Day 63 — 2027-01-17 (weekend, 4.0h, core)

- **Domain/Topic**: systems / networking-tcp-http
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-09.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 63): resolves stacks-queues-monotonic, trees-bst

## Week 10 — Data systems

Domains: systems, dsa · Outcome: Relational and non-relational modelling, indexing and caching, with measured queries.

### Day 64 — 2027-01-18 (weekday, 5.0h, optional)

- **Domain/Topic**: systems / sql-modelling-joins
- **Objective**: Model a non-trivial domain in SQLite, then write the queries the model makes awkward.
- **Artifact**: `systems/sql-modelling-joins/schema.sql`
- **Verification**: pytest runs the schema and its queries; results asserted
- **Notes topic**: Why normalisation is a trade against read cost
- **Minimum viable**: Schema plus two queries.

### Day 65 — 2027-01-19 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / heaps-top-k
- **Objective**: Solve the heaps and top-k pattern from scratch with a shared test harness.
- **Artifact**: `dsa/heaps-top-k/solutions.py`
- **Verification**: pytest dsa/heaps-top-k/ passes; complexity asserted per solution
- **Notes topic**: What the heaps and top-k pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 66 — 2027-01-20 (weekday, 5.0h, core)

- **Domain/Topic**: systems / sql-indexing-query-plans
- **Objective**: Add indexes to slow queries and read the query plan to prove why they helped.
- **Artifact**: `systems/sql-indexing-query-plans/indexes.py`
- **Verification**: pytest passes; benchmarks.json shows query time before and after with plans
- **Notes topic**: How to read a query plan, and why an index can make writes worse
- **Minimum viable**: One index with a before/after timing.

### Day 67 — 2027-01-21 (weekday, 5.0h, optional)

- **Domain/Topic**: systems / nosql-access-patterns
- **Objective**: Model the same domain for key-value and document access, and show what each makes hard.
- **Artifact**: `systems/nosql-access-patterns/model.py`
- **Verification**: pytest covers the access patterns each model supports and one it does not
- **Notes topic**: Why you design NoSQL schemas backwards from the queries
- **Minimum viable**: One access pattern modelled.

### Day 68 — 2027-01-22 (weekday, 5.0h, core)

- **Domain/Topic**: systems / caching-strategies-redis
- **Objective**: Implement cache-aside, write-through and TTL eviction; measure hit rate and staleness.
- **Artifact**: `systems/caching-strategies-redis/cache.py`
- **Verification**: pytest passes; benchmarks.json reports hit rate per strategy
- **Notes topic**: Why cache invalidation is the hard part, stated precisely
- **Minimum viable**: Cache-aside with a hit-rate count.

### Day 69 — 2027-01-23 (weekend, 4.0h, core)

- **Domain/Topic**: systems / vector-store-vs-rdbms
- **Objective**: Compare a dedicated vector index against pgvector-style SQL storage for the same corpus.
- **Artifact**: `systems/vector-store-vs-rdbms/compare.py`
- **Verification**: pytest passes; benchmarks.json compares recall and latency for both
- **Notes topic**: When a vector database earns its operational cost over a SQL extension
- **Minimum viable**: One backend measured.

### Day 70 — 2027-01-24 (weekend, 4.0h, core)

- **Domain/Topic**: systems / sql-modelling-joins
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-10.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 70): resolves trees-traversals, heaps-top-k

## Week 11 — Queues, events and services

Domains: systems, dsa · Outcome: Asynchronous architecture and the failure modes that come with it.

### Day 71 — 2027-01-25 (weekday, 5.0h, core)

- **Domain/Topic**: systems / queues-workers-dlq
- **Objective**: Build a work queue with retries, exponential backoff and a dead-letter path.
- **Artifact**: `systems/queues-workers-dlq/queue.py`
- **Verification**: pytest covers retry exhaustion landing in the DLQ and a poison message
- **Notes topic**: Why a dead-letter queue is a design requirement, not an operational afterthought
- **Minimum viable**: Queue with retries, no DLQ yet.

### Day 72 — 2027-01-26 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / graphs-bfs-dfs
- **Objective**: Solve the graphs, bfs and dfs pattern from scratch with a shared test harness.
- **Artifact**: `dsa/graphs-bfs-dfs/solutions.py`
- **Verification**: pytest dsa/graphs-bfs-dfs/ passes; complexity asserted per solution
- **Notes topic**: What the graphs, bfs and dfs pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 73 — 2027-01-27 (weekday, 5.0h, core)

- **Domain/Topic**: systems / event-driven-architecture
- **Objective**: Implement a publish-subscribe fan-out with at-least-once delivery and idempotent consumers.
- **Artifact**: `systems/event-driven-architecture/events.py`
- **Verification**: pytest proves a duplicate delivery does not double-apply
- **Notes topic**: Why at-least-once forces idempotency on every consumer
- **Minimum viable**: Fan-out to two consumers.

### Day 74 — 2027-01-28 (weekday, 5.0h, optional)

- **Domain/Topic**: systems / kafka-log-semantics
- **Objective**: Implement partitioned append-only log semantics with consumer offsets and replay.
- **Artifact**: `systems/kafka-log-semantics/log.py`
- **Verification**: pytest covers ordering within a partition, offset commit and replay from an offset
- **Notes topic**: Why ordering is per-partition and what that costs you
- **Minimum viable**: Single-partition log with offsets.

### Day 75 — 2027-01-29 (weekday, 5.0h, optional)

- **Domain/Topic**: systems / microservices-boundaries
- **Objective**: Split a monolith by boundary, then show the distributed transaction the split created.
- **Artifact**: `systems/microservices-boundaries/BOUNDARIES.md`
- **Verification**: The document names each service, its data, and the consistency problem introduced
- **Notes topic**: Why the hard part of microservices is the data, not the services
- **Minimum viable**: Boundary map plus one identified problem.

### Day 76 — 2027-01-30 (weekend, 4.0h, core)

- **Domain/Topic**: systems / idempotency-exactly-once
- **Objective**: Implement idempotency keys so a retried request cannot double-charge.
- **Artifact**: `systems/idempotency-exactly-once/idempotent.py`
- **Verification**: pytest proves the same key applied twice has one effect
- **Notes topic**: Why exactly-once delivery is a fiction and idempotency is the real answer
- **Minimum viable**: Key storage and dedupe check.

### Day 77 — 2027-01-31 (weekend, 4.0h, core)

- **Domain/Topic**: systems / queues-workers-dlq
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-11.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 77): resolves trees-bst, graphs-bfs-dfs

## Week 12 — Distributed systems fundamentals

Domains: systems, dsa · Outcome: Replication, partitioning, consensus trade-offs and designing for failure.

### Day 78 — 2027-02-01 (weekday, 5.0h, core)

- **Domain/Topic**: systems / cap-consistency-models
- **Objective**: Simulate a partition and demonstrate the behaviour difference between CP and AP choices.
- **Artifact**: `systems/cap-consistency-models/partition.py`
- **Verification**: pytest covers both configurations under the same simulated partition
- **Notes topic**: Why CAP is about what you give up during a partition, not in general
- **Minimum viable**: One configuration simulated.

### Day 79 — 2027-02-02 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / graphs-topological-sort
- **Objective**: Solve the topological sorting pattern from scratch with a shared test harness.
- **Artifact**: `dsa/graphs-topological-sort/solutions.py`
- **Verification**: pytest dsa/graphs-topological-sort/ passes; complexity asserted per solution
- **Notes topic**: What the topological sorting pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 80 — 2027-02-03 (weekday, 5.0h, optional)

- **Domain/Topic**: systems / replication-partitioning
- **Objective**: Implement consistent hashing and show the rebalance cost when a node joins.
- **Artifact**: `systems/replication-partitioning/hashing.py`
- **Verification**: pytest passes; benchmarks.json reports keys moved on node join vs modulo hashing
- **Notes topic**: Why consistent hashing exists, measured in keys moved
- **Minimum viable**: Consistent hashing ring with tests.

### Day 81 — 2027-02-04 (weekday, 5.0h, core)

- **Domain/Topic**: systems / fault-tolerance-patterns
- **Objective**: Implement a circuit breaker and a bulkhead, and prove they contain a failing dependency.
- **Artifact**: `systems/fault-tolerance-patterns/resilience.py`
- **Verification**: pytest proves the breaker opens, and that a slow dependency cannot exhaust all workers
- **Notes topic**: Why timeouts without bulkheads still take the system down
- **Minimum viable**: Circuit breaker with open and half-open states.

### Day 82 — 2027-02-05 (weekday, 5.0h, core)

- **Domain/Topic**: systems / systems-inference-serving-design
- **Objective**: Write the high-level and low-level design for a multi-tenant inference service.
- **Artifact**: `systems/systems-inference-serving-design/DESIGN.md`
- **Verification**: The design states capacity maths, failure modes and the batching trade-off explicitly
- **Notes topic**: How to run an ML system-design interview end to end
- **Minimum viable**: High-level design plus capacity estimate.

### Day 83 — 2027-02-06 (weekend, 4.0h, optional)

- **Domain/Topic**: systems / systems-feature-stores
- **Objective**: Build a tiny feature store and demonstrate the skew it exists to prevent.
- **Artifact**: `systems/systems-feature-stores/store.py`
- **Verification**: pytest proves offline and online reads agree for the same entity and timestamp
- **Notes topic**: What training-serving skew is and why point-in-time correctness is the fix
- **Minimum viable**: Online read path only.

### Day 84 — 2027-02-07 (weekend, 4.0h, core)

- **Domain/Topic**: systems / cap-consistency-models
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-12.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 84): resolves heaps-top-k, graphs-topological-sort

## Week 13 — Cloud foundations

Domains: cloud, dsa · Outcome: Identity, storage, serverless compute and managed NoSQL, with spend controlled from day one.

### Day 85 — 2027-02-08 (weekday, 5.0h, core)

- **Domain/Topic**: cloud / cloud-iam-budgets
- **Objective**: Create a least-privilege user with MFA and budget alarms at three thresholds, before anything else.
- **Artifact**: `cloud/cloud-iam-budgets/setup.md`
- **Verification**: The record shows the alarm thresholds and a screenshot-free CLI verification of each
- **Notes topic**: Why budget alarms are the first cloud exercise and not a later one
- **Minimum viable**: Least-privilege user plus one budget alarm.

### Day 86 — 2027-02-09 (weekday, 5.0h, optional)

- **Domain/Topic**: dsa / graphs-shortest-paths
- **Objective**: Solve the shortest paths pattern from scratch with a shared test harness.
- **Artifact**: `dsa/graphs-shortest-paths/solutions.py`
- **Verification**: pytest dsa/graphs-shortest-paths/ passes; complexity asserted per solution
- **Notes topic**: What the shortest paths pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 87 — 2027-02-10 (weekday, 5.0h, core)

- **Domain/Topic**: cloud / cloud-object-storage
- **Objective**: Store the RAG corpus in S3 with versioning and a lifecycle rule, then read it from code.
- **Artifact**: `cloud/cloud-object-storage/storage.py`
- **Verification**: pytest passes against a local stub; the committed record shows the live round trip
- **Notes topic**: Why object storage is not a filesystem, and what that changes in your code
- **Minimum viable**: Upload and download one object.

### Day 88 — 2027-02-11 (weekday, 5.0h, core)

- **Domain/Topic**: cloud / cloud-serverless-functions
- **Objective**: Deploy the week-7 FastAPI handler as a function behind an HTTP endpoint and measure cold start.
- **Artifact**: `cloud/cloud-serverless-functions/handler.py`
- **Verification**: pytest passes locally; benchmarks.json records cold vs warm invocation latency
- **Notes topic**: What a cold start actually costs and which workloads it disqualifies
- **Minimum viable**: Function deployed and invoked once.

### Day 89 — 2027-02-12 (weekday, 5.0h, core)

- **Domain/Topic**: cloud / cloud-managed-nosql
- **Objective**: Store agent conversation state in DynamoDB with a single-table design.
- **Artifact**: `cloud/cloud-managed-nosql/state.py`
- **Verification**: pytest passes against a local stub; the record shows the live read and write
- **Notes topic**: Why single-table design follows from the access patterns you listed first
- **Minimum viable**: One write and one read.

### Day 90 — 2027-02-13 (weekend, 4.0h, optional)

- **Domain/Topic**: cloud / cloud-containers-registry
- **Objective**: Containerise the agent service, push it to a registry and run it as a managed task.
- **Artifact**: `cloud/cloud-containers-registry/Dockerfile`
- **Verification**: The image builds and runs locally; the record shows the managed task serving one request
- **Notes topic**: Why the registry and the scheduler are separate concerns
- **Minimum viable**: Image builds and runs locally; defer the deploy.

### Day 91 — 2027-02-14 (weekend, 4.0h, core)

- **Domain/Topic**: cloud / cloud-iam-budgets
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-13.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 91): resolves graphs-bfs-dfs, graphs-shortest-paths

## Week 14 — Managed AI services, Git and Linux

Domains: cloud, git, dsa · Outcome: A managed model provider compared against direct APIs, plus the operational basics.

### Day 92 — 2027-02-15 (weekday, 5.0h, optional)

- **Domain/Topic**: cloud / cloud-managed-model-hosting
- **Objective**: Call a managed hosted model and compare latency and cost against the direct provider API.
- **Artifact**: `cloud/cloud-managed-model-hosting/compare.py`
- **Verification**: pytest passes against fixtures; benchmarks.json compares both paths
- **Notes topic**: What a managed model endpoint buys over calling the provider directly
- **Minimum viable**: One call through each path.

### Day 93 — 2027-02-16 (weekday, 5.0h, optional)

- **Domain/Topic**: dsa / union-find
- **Objective**: Solve the union-find pattern from scratch with a shared test harness.
- **Artifact**: `dsa/union-find/solutions.py`
- **Verification**: pytest dsa/union-find/ passes; complexity asserted per solution
- **Notes topic**: What the union-find pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 94 — 2027-02-17 (weekday, 5.0h, core)

- **Domain/Topic**: cloud / cloud-observability-costs
- **Objective**: Instrument the deployed service with logs, metrics and a cost tag, then reconcile the spend.
- **Artifact**: `cloud/cloud-observability-costs/RECONCILIATION.md`
- **Verification**: The record reconciles tagged spend against the week's estimates, naming any variance
- **Notes topic**: Why per-tenant cost attribution has to be designed in, not derived later
- **Minimum viable**: Tags applied and one metric queried.

### Day 95 — 2027-02-18 (weekday, 5.0h, core)

- **Domain/Topic**: git / linux-shell-filesystem
- **Objective**: Script a log-triage pipeline with grep, awk, sed, find and xargs over a committed sample.
- **Artifact**: `git/linux-shell-filesystem/triage.sh`
- **Verification**: The script runs on the committed sample and its output is asserted by a test
- **Notes topic**: Which shell tool to reach for, and why pipelines beat scripts for triage
- **Minimum viable**: Three-stage pipeline working.

### Day 96 — 2027-02-19 (weekday, 5.0h, optional)

- **Domain/Topic**: git / git-advanced-workflows
- **Objective**: Use bisect to find a seeded regression, then reflog to recover a deliberately lost commit.
- **Artifact**: `git/git-advanced-workflows/RECOVERY.md`
- **Verification**: The record shows the bisect transcript and the recovered commit SHA
- **Notes topic**: Why reflog means almost nothing in git is truly lost
- **Minimum viable**: Bisect completed.

### Day 97 — 2027-02-20 (weekend, 4.0h, optional)

- **Domain/Topic**: git / git-rebase-conflict-resolution
- **Objective**: Resolve a deliberately conflicting interactive rebase, squashing and reordering commits.
- **Artifact**: `git/git-rebase-conflict-resolution/NOTES.md`
- **Verification**: The resulting history is linear with the intended commits and messages
- **Notes topic**: When to rebase and when rewriting shared history is wrong
- **Minimum viable**: Conflict resolved on one commit.

### Day 98 — 2027-02-21 (weekend, 4.0h, core)

- **Domain/Topic**: cloud / cloud-managed-model-hosting
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan. Milestone readiness check: Multi-backend inference gateway.
- **Artifact**: `progress/reviews/week-14.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 98): resolves graphs-topological-sort, union-find

## Week 15 — Applied mathematics and classical ML

Domains: ml, dsa · Outcome: The maths that transformer and optimiser behaviour actually depends on.

### Day 99 — 2027-02-22 (weekday, 5.0h, core)

- **Domain/Topic**: ml / math-calculus-autodiff
- **Objective**: Build a scalar reverse-mode autodiff engine and differentiate a small expression graph.
- **Artifact**: `ml/math-calculus-autodiff/autodiff.py`
- **Verification**: pytest asserts gradients match analytic derivatives
- **Notes topic**: What the chain rule becomes when you implement it as a graph
- **Minimum viable**: Forward and backward for add and multiply.

### Day 100 — 2027-02-23 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / recursion-backtracking
- **Objective**: Solve the recursion and backtracking pattern from scratch with a shared test harness.
- **Artifact**: `dsa/recursion-backtracking/solutions.py`
- **Verification**: pytest dsa/recursion-backtracking/ passes; complexity asserted per solution
- **Notes topic**: What the recursion and backtracking pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 101 — 2027-02-24 (weekday, 5.0h, core)

- **Domain/Topic**: ml / math-probability-statistics
- **Objective**: Implement confidence intervals and a significance test, then apply them to week-5 eval data.
- **Artifact**: `ml/math-probability-statistics/stats.py`
- **Verification**: pytest asserts known-answer cases; applied to the committed eval results
- **Notes topic**: Why an eval difference without a confidence interval is not a result
- **Minimum viable**: Confidence interval implemented and tested.

### Day 102 — 2027-02-25 (weekday, 5.0h, core)

- **Domain/Topic**: ml / classical-ml-comparison
- **Objective**: Train logistic regression, a tree and a gradient-boosted model; compare against a trivial baseline.
- **Artifact**: `ml/classical-ml-comparison/compare.py`
- **Verification**: pytest passes; benchmarks.json reports metrics, split and the majority-class baseline
- **Notes topic**: Why a model that cannot beat the majority class is not a model
- **Minimum viable**: One model trained with a reported metric.

### Day 103 — 2027-02-26 (weekday, 5.0h, optional)

- **Domain/Topic**: ml / feature-engineering
- **Objective**: Build a feature pipeline, then demonstrate target leakage and the split that prevents it.
- **Artifact**: `ml/feature-engineering/features.py`
- **Verification**: pytest proves the leaky pipeline scores higher offline and the correct one does not leak
- **Notes topic**: Why a suspiciously good offline score is usually leakage
- **Minimum viable**: Pipeline built; leakage demonstration deferred.

### Day 104 — 2027-02-27 (weekend, 4.0h, core)

- **Domain/Topic**: ml / ml-evaluation-methodology
- **Objective**: Implement precision/recall/F1/ROC-AUC from scratch and show where accuracy misleads.
- **Artifact**: `ml/ml-evaluation-methodology/metrics.py`
- **Verification**: pytest asserts against sklearn; an imbalanced case is committed where accuracy misleads
- **Notes topic**: Which metric to pick, derived from the cost of each error type
- **Minimum viable**: Precision, recall and F1 implemented.

### Day 105 — 2027-02-28 (weekend, 4.0h, core)

- **Domain/Topic**: ml / math-calculus-autodiff
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-15.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 105): resolves graphs-shortest-paths, math-calculus-autodiff, recursion-backtracking, math-probability-statistics, classical-ml-comparison, feature-engineering, ml-evaluation-methodology

## Week 16 — Neural network and transformer internals

Domains: ml, dsa · Outcome: Backpropagation, training dynamics and attention, all implemented from scratch.

### Day 106 — 2027-03-01 (weekday, 5.0h, core)

- **Domain/Topic**: ml / gradient-descent-scratch
- **Objective**: Implement batch, stochastic and mini-batch gradient descent and compare convergence.
- **Artifact**: `ml/gradient-descent-scratch/gradient_descent.py`
- **Verification**: pytest passes; benchmarks.json compares steps-to-converge across the three
- **Notes topic**: Why batch size changes the path and not just the speed
- **Minimum viable**: Batch gradient descent converging on a convex problem.

### Day 107 — 2027-03-02 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / greedy-intervals
- **Objective**: Solve the greedy and intervals pattern from scratch with a shared test harness.
- **Artifact**: `dsa/greedy-intervals/solutions.py`
- **Verification**: pytest dsa/greedy-intervals/ passes; complexity asserted per solution
- **Notes topic**: What the greedy and intervals pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 108 — 2027-03-03 (weekday, 5.0h, core)

- **Domain/Topic**: ml / neural-net-scratch
- **Objective**: Implement a two-layer network with manual backpropagation; verify with gradient checking.
- **Artifact**: `ml/neural-net-scratch/network.py`
- **Verification**: pytest passes gradient checking against numerical gradients
- **Notes topic**: What backpropagation computes, written out for one concrete layer
- **Minimum viable**: Forward pass plus one layer of backward.

### Day 109 — 2027-03-04 (weekday, 5.0h, core)

- **Domain/Topic**: ml / training-dynamics
- **Objective**: Deliberately induce a vanishing gradient and a dead-ReLU network, then diagnose each.
- **Artifact**: `ml/training-dynamics/dynamics.py`
- **Verification**: pytest asserts the diagnostic detects each seeded pathology
- **Notes topic**: How to read a loss curve and name the failure, rather than lowering the learning rate
- **Minimum viable**: One pathology induced and detected.

### Day 110 — 2027-03-05 (weekday, 5.0h, core)

- **Domain/Topic**: ml / transformers-attention-scratch
- **Objective**: Implement scaled dot-product and multi-head attention; verify against a reference.
- **Artifact**: `ml/transformers-attention-scratch/attention.py`
- **Verification**: pytest asserts output agreement with a PyTorch reference to tolerance
- **Notes topic**: Why the scaling factor is there, and what multi-head actually buys
- **Minimum viable**: Single-head attention verified.

### Day 111 — 2027-03-06 (weekend, 4.0h, optional)

- **Domain/Topic**: ml / pytorch-gpu-training
- **Objective**: Port the scratch network to PyTorch and measure the speedup against the NumPy version.
- **Artifact**: `ml/pytorch-gpu-training/train.py`
- **Verification**: pytest passes on CPU; benchmarks.json compares against the from-scratch implementation
- **Notes topic**: What the framework does for you, priced in wall-clock and in lost visibility
- **Minimum viable**: PyTorch version trains to the same loss.

### Day 112 — 2027-03-07 (weekend, 4.0h, core)

- **Domain/Topic**: ml / gradient-descent-scratch
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan. Milestone readiness check: Production MCP server with governance.
- **Artifact**: `progress/reviews/week-16.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 112): resolves union-find, gradient-descent-scratch, greedy-intervals, neural-net-scratch, training-dynamics, transformers-attention-scratch, pytorch-gpu-training

## Week 17 — MLOps lifecycle

Domains: ml, dsa · Outcome: Pipelines, registries, drift and serving — the secondary-role evidence.

### Day 113 — 2027-03-08 (weekday, 5.0h, core)

- **Domain/Topic**: ml / mlops-pipelines
- **Objective**: Build a parameterised pipeline that reproduces a run exactly from a committed config and seed.
- **Artifact**: `ml/mlops-pipelines/pipeline.py`
- **Verification**: pytest proves two runs from the same config produce identical metrics
- **Notes topic**: Why a reproducible run needs more pinned than the random seed
- **Minimum viable**: Pipeline runs end to end from config.

### Day 114 — 2027-03-09 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / dp-1d
- **Objective**: Solve the dynamic programming: 1-d pattern from scratch with a shared test harness.
- **Artifact**: `dsa/dp-1d/solutions.py`
- **Verification**: pytest dsa/dp-1d/ passes; complexity asserted per solution
- **Notes topic**: What the dynamic programming: 1-d pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 115 — 2027-03-10 (weekday, 5.0h, core)

- **Domain/Topic**: ml / mlops-model-registry
- **Objective**: Implement model versioning with stage promotion and a rollback path.
- **Artifact**: `ml/mlops-model-registry/registry.py`
- **Verification**: pytest covers promote, serve-current and rollback-to-previous
- **Notes topic**: Why a model needs a deployment lifecycle and not just a file path
- **Minimum viable**: Versioning plus promotion.

### Day 116 — 2027-03-11 (weekday, 5.0h, core)

- **Domain/Topic**: ml / mlops-drift-monitoring
- **Objective**: Implement data and prediction drift detection, then trigger on a seeded distribution shift.
- **Artifact**: `ml/mlops-drift-monitoring/drift.py`
- **Verification**: pytest proves the detector fires on the seeded shift and not on resampling noise
- **Notes topic**: Which drift matters, and why prediction drift is the earlier signal
- **Minimum viable**: One drift statistic implemented.

### Day 117 — 2027-03-12 (weekday, 5.0h, core)

- **Domain/Topic**: ml / mlops-model-serving
- **Objective**: Serve the trained model behind an API and prove the serving path matches training.
- **Artifact**: `ml/mlops-model-serving/serve.py`
- **Verification**: pytest asserts identical predictions from the training code and the served endpoint
- **Notes topic**: Where training-serving skew creeps in, concretely
- **Minimum viable**: Endpoint serves predictions.

### Day 118 — 2027-03-13 (weekend, 4.0h, optional)

- **Domain/Topic**: ml / mlops-testing-validation
- **Objective**: Build a behavioural test suite: invariance, directional expectation and edge cases.
- **Artifact**: `ml/mlops-testing-validation/validate.py`
- **Verification**: pytest runs all three test classes; at least one real model weakness is documented
- **Notes topic**: Why accuracy is not a test suite
- **Minimum viable**: Invariance tests only.

### Day 119 — 2027-03-14 (weekend, 4.0h, core)

- **Domain/Topic**: ml / mlops-pipelines
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-17.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 119): resolves math-calculus-autodiff, recursion-backtracking, math-probability-statistics, classical-ml-comparison, feature-engineering, ml-evaluation-methodology, mlops-pipelines, dp-1d, mlops-model-registry, mlops-drift-monitoring, mlops-model-serving, mlops-testing-validation

## Week 18 — Inference and production engineering

Domains: ml, dsa · Outcome: Serving internals, KV caching, batching and compression, all measured.

### Day 120 — 2027-03-15 (weekday, 5.0h, core)

- **Domain/Topic**: ml / inference-latency-profiling
- **Objective**: Measure TTFT, inter-token latency and throughput for a local model under load.
- **Artifact**: `ml/inference-latency-profiling/profile.py`
- **Verification**: pytest passes; benchmarks.json reports the full latency breakdown
- **Notes topic**: Why TTFT and total latency are optimised by different changes
- **Minimum viable**: TTFT measured for a single request.

### Day 121 — 2027-03-16 (weekday, 5.0h, core)

- **Domain/Topic**: dsa / dp-2d
- **Objective**: Solve the dynamic programming: 2-d pattern from scratch with a shared test harness.
- **Artifact**: `dsa/dp-2d/solutions.py`
- **Verification**: pytest dsa/dp-2d/ passes; complexity asserted per solution
- **Notes topic**: What the dynamic programming: 2-d pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 122 — 2027-03-17 (weekday, 5.0h, core)

- **Domain/Topic**: ml / inference-kv-cache
- **Objective**: Implement a KV cache for autoregressive decoding and measure the speedup it produces.
- **Artifact**: `ml/inference-kv-cache/kv_cache.py`
- **Verification**: pytest asserts identical outputs with and without the cache; speedup recorded
- **Notes topic**: Why KV caching turns quadratic decoding into linear, and what it costs in memory
- **Minimum viable**: Cache implemented for one attention layer.

### Day 123 — 2027-03-18 (weekday, 5.0h, core)

- **Domain/Topic**: ml / inference-batching
- **Objective**: Implement static and continuous batching and measure throughput against tail latency.
- **Artifact**: `ml/inference-batching/batching.py`
- **Verification**: pytest passes; benchmarks.json shows the throughput/p99 trade for both
- **Notes topic**: Why continuous batching beats static batching on mixed-length requests
- **Minimum viable**: Static batching with a throughput number.

### Day 124 — 2027-03-19 (weekday, 5.0h, core)

- **Domain/Topic**: ml / inference-quantization
- **Objective**: Quantize a small model to int8 and report the accuracy, latency and memory trade.
- **Artifact**: `ml/inference-quantization/quantize.py`
- **Verification**: pytest passes; benchmarks.json reports all three axes against the fp32 baseline
- **Notes topic**: Where quantization loses accuracy, and which layers are worth keeping in high precision
- **Minimum viable**: int8 weights quantized with a size measurement.

### Day 125 — 2027-03-20 (weekend, 4.0h, core)

- **Domain/Topic**: ml / inference-cost-latency-budgeting
- **Objective**: Build a cost model for a request path and find the cheapest configuration meeting an SLO.
- **Artifact**: `ml/inference-cost-latency-budgeting/budget.py`
- **Verification**: pytest passes; benchmarks.json reports cost per 1k requests per configuration
- **Notes topic**: How to argue for a model choice in money rather than in preference
- **Minimum viable**: Cost model covering one configuration.

### Day 126 — 2027-03-21 (weekend, 4.0h, core)

- **Domain/Topic**: ml / inference-latency-profiling
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-18.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 126): resolves gradient-descent-scratch, greedy-intervals, neural-net-scratch, training-dynamics, transformers-attention-scratch, pytorch-gpu-training, inference-latency-profiling, dp-2d, inference-kv-cache, inference-batching, inference-quantization, inference-cost-latency-budgeting

## Week 19 — Portfolio readiness and consolidation

Domains: applied-ai, systems, dsa · Outcome: Project briefs finalised, weak topics re-solved, and the interview drill paths built.

### Day 127 — 2027-03-22 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / project-brief-flagship
- **Objective**: Finalise the flagship brief: scope, architecture, eval plan and the readiness checklist.
- **Artifact**: `promoted/briefs/flagship.md`
- **Verification**: The brief states what it demonstrates, its eval metric, and its deployment target
- **Notes topic**: How to scope a portfolio project so it is finishable and still substantial
- **Minimum viable**: Scope and architecture sections drafted.

### Day 128 — 2027-03-23 (weekday, 5.0h, optional)

- **Domain/Topic**: dsa / tries
- **Objective**: Solve the tries pattern from scratch with a shared test harness.
- **Artifact**: `dsa/tries/solutions.py`
- **Verification**: pytest dsa/tries/ passes; complexity asserted per solution
- **Notes topic**: What the tries pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 129 — 2027-03-24 (weekday, 5.0h, core)

- **Domain/Topic**: applied-ai / interview-drill-agentic
- **Objective**: Build the drill path for the primary role: topics, questions and a timed mock.
- **Artifact**: `applied-ai/interview-drill-agentic/DRILL.md`
- **Verification**: The drill covers at least 6 topics across 3 domains with answers written out
- **Notes topic**: Which agentic questions recur, and the answer you would actually give out loud
- **Minimum viable**: Topic list plus three answers.

### Day 130 — 2027-03-25 (weekday, 5.0h, core)

- **Domain/Topic**: systems / interview-drill-systems
- **Objective**: Run two timed system-design questions end to end and write up both, including what went badly.
- **Artifact**: `systems/interview-drill-systems/DRILL.md`
- **Verification**: Both write-ups include capacity maths, failure modes and a self-critique
- **Notes topic**: How to structure 45 minutes of system design without running out of time
- **Minimum viable**: One question completed.

### Day 131 — 2027-03-26 (weekday, 5.0h, optional)

- **Domain/Topic**: dsa / bit-manipulation
- **Objective**: Solve the bit manipulation pattern from scratch with a shared test harness.
- **Artifact**: `dsa/bit-manipulation/solutions.py`
- **Verification**: pytest dsa/bit-manipulation/ passes; complexity asserted per solution
- **Notes topic**: What the bit manipulation pattern recognises, and its complexity
- **Minimum viable**: Two problems solved and tested; defer the rest to a review slot.

### Day 132 — 2027-03-27 (weekend, 4.0h, core)

- **Domain/Topic**: applied-ai / consolidation-weak-topics
- **Objective**: Re-solve every topic that failed a re-solve during the programme, from a blank file.
- **Artifact**: `applied-ai/consolidation-weak-topics/RESOLVES.md`
- **Verification**: Every previously failed topic is re-solved and the outcome recorded
- **Notes topic**: What the failure pattern across your re-solves says about how you learn
- **Minimum viable**: The two weakest topics re-solved.

### Day 133 — 2027-03-28 (weekend, 4.0h, core)

- **Domain/Topic**: applied-ai / project-brief-flagship
- **Objective**: Weekly review: re-solve the scheduled topics from a blank file, audit the week against the constitution, reconcile any cloud spend, and re-plan.
- **Artifact**: `progress/reviews/week-19.md`
- **Verification**: roadmap review writes the generated section; the judgement sections are filled in
- **Notes topic**: What this week's re-solve failures say about which material is fragile
- **Minimum viable**: Run `roadmap review` and complete the re-solves; defer the prose audit.

**Review** (day 133): resolves mlops-pipelines, dp-1d, mlops-model-registry, mlops-drift-monitoring, mlops-model-serving, mlops-testing-validation, inference-latency-profiling, dp-2d, inference-kv-cache, inference-batching, inference-quantization, inference-cost-latency-budgeting, tries, bit-manipulation

