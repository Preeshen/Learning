# Roadmap (generated — do not hand-edit; see roadmap.yaml)

70 days · 10 weeks · 2026-11-16 to 2027-01-24

## Week 1 — Python depth and DSA patterns I

Domains: python, dsa, git, applied-ai · Outcome: Typed, tested, packaged Python; arrays/hashing and two-pointer patterns solved cold; first tool-calling loop built.

### Day 1 — 2026-11-16 (weekday, 4h, core)

- **Domain/Topic**: python / project-tooling
- **Objective**: Stand up the repo toolchain and complete the worked example day.
- **Artifact**: `python/project-tooling/env_report.py`
- **Verification**: pytest python/project-tooling/ passes; roadmap validate exits 0
- **Notes topic**: Why a committed lockfile is the difference between reproducible and 'works here'
- **Minimum viable**: Toolchain installed and `roadmap today` runs; defer the notes.

### Day 2 — 2026-11-17 (weekday, 4h, core)

- **Domain/Topic**: dsa / arrays-hashing
- **Objective**: Solve the arrays/hashing pattern from scratch across 4 problems with a shared test harness.
- **Artifact**: `dsa/arrays-hashing/solutions.py`
- **Verification**: pytest dsa/arrays-hashing/ passes; complexity asserted per solution
- **Notes topic**: Why a hash map turns an O(n^2) lookup into O(n)
- **Minimum viable**: 2 of 4 problems solved and tested; defer the other 2 to the review slot.
- **Prerequisites**: 1

### Day 3 — 2026-11-18 (weekday, 4h, core)

- **Domain/Topic**: dsa / two-pointers
- **Objective**: Solve the two-pointers pattern from scratch across 4 problems.
- **Artifact**: `dsa/two-pointers/solutions.py`
- **Verification**: pytest dsa/two-pointers/ passes; complexity asserted per solution
- **Notes topic**: Why two pointers replaces an O(n^2) pair search with a single O(n) pass
- **Minimum viable**: 2 of 4 problems solved and tested; defer the other 2 to the review slot.
- **Prerequisites**: 2

### Day 4 — 2026-11-19 (weekday, 4h, optional)

- **Domain/Topic**: git / git-fundamentals
- **Objective**: Practice rebase, bisect, and conflict resolution against a scripted repo history.
- **Artifact**: `git/git-fundamentals/drill.sh`
- **Verification**: drill.sh exits 0 after resolving the seeded conflicts
- **Notes topic**: Why rebase rewrites history and merge doesn't, and when each is the right tool
- **Minimum viable**: Rebase drill only; defer bisect and conflict drills.

### Day 5 — 2026-11-20 (weekday, 4h, core)

- **Domain/Topic**: dsa / sliding-window
- **Objective**: Solve the sliding-window pattern from scratch across 3 problems.
- **Artifact**: `dsa/sliding-window/solutions.py`
- **Verification**: pytest dsa/sliding-window/ passes; complexity asserted per solution
- **Notes topic**: Why a shrinking/growing window avoids re-scanning the whole string each time
- **Minimum viable**: 2 of 3 problems solved; defer the third.
- **Prerequisites**: 3

### Day 6 — 2026-11-21 (weekend, 6h, core)

- **Domain/Topic**: applied-ai / tool-calling
- **Objective**: Build a tool-calling loop from scratch, then wrap it behind a FastAPI endpoint.
- **Artifact**: `applied-ai/tool-calling/loop.py`
- **Verification**: pytest applied-ai/tool-calling/ passes, including 3 malformed-call cases
- **Notes topic**: Why retrying a malformed tool call is not the same as retrying a failed one
- **Minimum viable**: Happy-path loop with one tool, no FastAPI wrapper; defer serving and malformed-argument handling.
- **Prerequisites**: 1

### Day 7 — 2026-11-22 (weekend, 6h, core)

- **Domain/Topic**: dsa / arrays-hashing
- **Objective**: Weekly review: re-solve two DSA topics from a blank file, audit the week against the constitution, re-plan.
- **Artifact**: `progress/reviews/week-01.md`
- **Verification**: roadmap review writes the Generated section; both re-solves recorded pass/fail
- **Notes topic**: What the re-solve revealed about which parts of day 2 and day 3 were not actually retained
- **Minimum viable**: Re-solve one topic instead of two; log the skip honestly.
- **Prerequisites**: 2, 3

**Review** (day 7): resolves arrays-hashing, two-pointers

## Week 2 — DSA patterns II and first ML mechanism

Domains: dsa, ml, applied-ai · Outcome: Binary search, stacks, linked lists, and trees-I solved cold; gradient descent implemented from scratch; LLM cost/latency budgeting instrumented.

### Day 8 — 2026-11-23 (weekday, 4h, core)

- **Domain/Topic**: dsa / binary-search
- **Objective**: Solve the binary-search pattern from scratch, including search-on-answer and rotated-array variants.
- **Artifact**: `dsa/binary-search/solutions.py`
- **Verification**: pytest dsa/binary-search/ passes; complexity asserted per solution
- **Notes topic**: Why 'search on answer' reframes an optimization problem as a monotonic predicate you can binary search over
- **Minimum viable**: Classic binary search plus one variant; defer search-on-answer to the review slot.

### Day 9 — 2026-11-24 (weekday, 4h, core)

- **Domain/Topic**: dsa / stacks-monotonic
- **Objective**: Solve the stacks / monotonic-stack pattern from scratch across 3 problems.
- **Artifact**: `dsa/stacks-monotonic/solutions.py`
- **Verification**: pytest dsa/stacks-monotonic/ passes; complexity asserted per solution
- **Notes topic**: Why a monotonic stack answers 'next greater element' style questions in one O(n) pass instead of O(n^2)
- **Minimum viable**: Valid-parentheses plus one monotonic-stack problem; defer the third.

### Day 10 — 2026-11-25 (weekday, 4h, core)

- **Domain/Topic**: ml / gradient-descent-scratch
- **Objective**: Implement gradient descent and linear regression from scratch in NumPy, then compare against scikit-learn.
- **Artifact**: `ml/gradient-descent-scratch/gradient_descent.py`
- **Verification**: pytest ml/gradient-descent-scratch/ passes; benchmarks.json reports convergence vs scikit-learn's closed-form fit
- **Notes topic**: Why gradient descent needs a learning rate and closed-form least-squares doesn't, and what that costs at scale
- **Minimum viable**: From-scratch gradient descent only; defer the scikit-learn comparison to day 11's slack.
- **Prerequisites**: 1

### Day 11 — 2026-11-26 (weekday, 4h, core)

- **Domain/Topic**: dsa / linked-lists
- **Objective**: Solve the linked-list pattern from scratch: reversal, fast-slow pointers, cycle detection, merge-k.
- **Artifact**: `dsa/linked-lists/solutions.py`
- **Verification**: pytest dsa/linked-lists/ passes; complexity asserted per solution
- **Notes topic**: Why fast-slow pointers detect a cycle in O(n) time and O(1) space without a visited set
- **Minimum viable**: Reversal and cycle detection only; defer merge-k to the review slot.

### Day 12 — 2026-11-27 (weekday, 4h, core)

- **Domain/Topic**: applied-ai / cost-latency-budgeting
- **Objective**: Instrument token usage and latency for the day-6 tool-calling loop; establish a cost/latency budget and measure against it.
- **Artifact**: `applied-ai/cost-latency-budgeting/budget_tracker.py`
- **Verification**: pytest applied-ai/cost-latency-budgeting/ passes; benchmarks.json reports token cost and p50/p95 latency against the day-6 baseline
- **Notes topic**: Why token count alone is a cost signal but not a latency signal, and vice versa
- **Minimum viable**: Token-cost tracking only; defer p50/p95 latency measurement to day 13's slack.
- **Prerequisites**: 6

### Day 13 — 2026-11-28 (weekend, 6h, core)

- **Domain/Topic**: dsa / trees-traversals
- **Objective**: Solve tree traversals and BST-property problems from scratch across 4 problems.
- **Artifact**: `dsa/trees-traversals/solutions.py`
- **Verification**: pytest dsa/trees-traversals/ passes; complexity asserted per solution
- **Notes topic**: Why an in-order traversal of a valid BST is always sorted, and how that property turns validation into a one-pass check
- **Minimum viable**: Preorder/inorder/postorder plus BST validation; defer the remaining problem to the review slot.

### Day 14 — 2026-11-29 (weekend, 6h, core)

- **Domain/Topic**: dsa / sliding-window
- **Objective**: Weekly review: re-solve two DSA topics from a blank file, audit the week against the constitution, re-plan.
- **Artifact**: `progress/reviews/week-02.md`
- **Verification**: roadmap review writes the Generated section; both re-solves recorded pass/fail
- **Notes topic**: What the re-solve revealed about which parts of binary search and stacks were not actually retained
- **Minimum viable**: Re-solve one topic instead of two; log the skip honestly.
- **Prerequisites**: 8, 9

**Review** (day 14): resolves sliding-window, two-pointers

## Week 3 — Python engineering depth and DSA patterns III

Domains: python, dsa, applied-ai · Outcome: Typed, statically-checked, packaged, async-aware Python; trees-II and heaps solved cold; first LLM API call made from scratch.

### Day 15 — 2026-11-30 (weekday, 4h, core)

- **Domain/Topic**: python / python-typing-static-analysis
- **Objective**: Add static typing throughout the repo's tooling and run a type checker against it.
- **Artifact**: `python/typing-static-analysis/typed_examples.py`
- **Verification**: pytest python/typing-static-analysis/ passes; mypy python/typing-static-analysis/ reports zero errors
- **Notes topic**: What a type checker catches that a test suite doesn't, and what it can't catch
- **Minimum viable**: Type the existing tool's public functions only; defer the generics exercise.

### Day 16 — 2026-12-01 (weekday, 4h, core)

- **Domain/Topic**: python / python-packaging-testing-depth
- **Objective**: Package a small module properly (pyproject entry point, editable install) and write its test suite with fixtures and parametrization.
- **Artifact**: `python/packaging-testing-depth/pkg_demo.py`
- **Verification**: pytest python/packaging-testing-depth/ passes using pytest fixtures and parametrize
- **Notes topic**: Why a parametrized test is not the same as four copy-pasted tests
- **Minimum viable**: Write the fixtures and one parametrized test; defer the packaging exercise.
- **Prerequisites**: 1

### Day 17 — 2026-12-02 (weekday, 4h, core)

- **Domain/Topic**: dsa / trees-construct-serialize
- **Objective**: Solve tree-construction, serialization, and lowest-common-ancestor problems from scratch.
- **Artifact**: `dsa/trees-construct-serialize/solutions.py`
- **Verification**: pytest dsa/trees-construct-serialize/ passes; complexity asserted per solution
- **Notes topic**: Why LCA's split-point argument works for a general binary tree, not just a BST
- **Minimum viable**: LCA and one construction problem; defer serialization.
- **Prerequisites**: 13

### Day 18 — 2026-12-03 (weekday, 4h, core)

- **Domain/Topic**: python / python-async-concurrency
- **Objective**: Write an async job runner using asyncio: concurrent I/O-bound tasks with a bounded concurrency limit.
- **Artifact**: `python/async-concurrency/job_runner.py`
- **Verification**: pytest python/async-concurrency/ passes; benchmarks.json shows concurrent runtime vs sequential baseline
- **Notes topic**: Why async concurrency helps I/O-bound work and does nothing for CPU-bound work
- **Minimum viable**: Sequential baseline plus one concurrent variant; defer the bounded-concurrency semaphore.

### Day 19 — 2026-12-04 (weekday, 4h, core)

- **Domain/Topic**: dsa / heaps-priority-queues
- **Objective**: Solve heap/priority-queue problems from scratch: k-th largest, merge-k-lists revisited via a custom comparator, task scheduling.
- **Artifact**: `dsa/heaps-priority-queues/solutions.py`
- **Verification**: pytest dsa/heaps-priority-queues/ passes; complexity asserted per solution
- **Notes topic**: Why a heap gives O(log n) insert/extract-min instead of O(n) for repeatedly finding the smallest/largest element
- **Minimum viable**: K-th-largest only; defer task scheduling.

### Day 20 — 2026-12-05 (weekend, 6h, core)

- **Domain/Topic**: applied-ai / llm-api-basics
- **Objective**: Make a real LLM API call from scratch (no SDK wrapper beyond HTTP), parse a structured-output response, and handle a malformed-response retry.
- **Artifact**: `applied-ai/llm-api-basics/client.py`
- **Verification**: pytest applied-ai/llm-api-basics/ passes against recorded fixtures
- **Notes topic**: What a 'structured output' guarantee actually guarantees, and what still has to be validated client-side
- **Minimum viable**: Happy-path structured-output parsing only; defer the malformed-response retry.

### Day 21 — 2026-12-06 (weekend, 6h, core)

- **Domain/Topic**: python / python-typing-static-analysis
- **Objective**: Weekly review: re-solve the scheduled DSA/ML topics from a blank file, audit the week against the constitution, re-plan.
- **Artifact**: `progress/reviews/week-03.md`
- **Verification**: roadmap review writes the Generated section; both re-solves recorded pass/fail
- **Notes topic**: What the re-solve revealed about which parts of trees-II and heaps were not actually retained
- **Minimum viable**: Re-solve one topic instead of two; log the skip honestly.
- **Prerequisites**: 17, 19

**Review** (day 21): resolves arrays-hashing, binary-search, stacks-monotonic, trees-construct-serialize

## Week 4 — Backtracking, graphs, and retrieval foundations

Domains: python, dsa, applied-ai · Outcome: Backtracking and graph-traversal patterns solved cold; a retrieval pipeline built end to end over a real corpus.

### Day 22 — 2026-12-07 (weekday, 4h, core)

- **Domain/Topic**: python / python-profiling
- **Objective**: Profile a CPU-bound function, find the actual bottleneck, and fix it — then prove the fix with a measurement, not a guess.
- **Artifact**: `python/profiling/slow_function.py`
- **Verification**: pytest python/profiling/ passes; benchmarks.json shows before/after timing
- **Notes topic**: Why the bottleneck you assume is almost never the one the profiler shows
- **Minimum viable**: Profile and identify the bottleneck; defer the optimization itself.

### Day 23 — 2026-12-08 (weekday, 4h, core)

- **Domain/Topic**: dsa / backtracking
- **Objective**: Solve backtracking problems from scratch: subsets, permutations, combination sum.
- **Artifact**: `dsa/backtracking/solutions.py`
- **Verification**: pytest dsa/backtracking/ passes; complexity asserted per solution
- **Notes topic**: Why backtracking is DFS with an undo step, and what happens if you forget the undo
- **Minimum viable**: Subsets and permutations only; defer combination sum.

### Day 24 — 2026-12-09 (weekday, 4h, core)

- **Domain/Topic**: applied-ai / prompt-engineering-eval-harness
- **Objective**: Build a prompt-evaluation harness: a labeled set of prompt/expected-behavior pairs, scored automatically against a baseline prompt.
- **Artifact**: `applied-ai/prompt-engineering-eval-harness/harness.py`
- **Verification**: pytest applied-ai/prompt-engineering-eval-harness/ passes; benchmarks.json reports pass rate vs the baseline prompt
- **Notes topic**: Why 'the prompt seems to work' is not evidence, and what a labeled eval set actually buys you
- **Minimum viable**: 5-case eval set instead of 20; defer the baseline-prompt comparison.
- **Prerequisites**: 20

### Day 25 — 2026-12-10 (weekday, 4h, core)

- **Domain/Topic**: dsa / graphs-bfs-dfs-topo
- **Objective**: Solve graph BFS/DFS and topological-sort problems from scratch.
- **Artifact**: `dsa/graphs-bfs-dfs-topo/solutions.py`
- **Verification**: pytest dsa/graphs-bfs-dfs-topo/ passes; complexity asserted per solution
- **Notes topic**: Why topological sort is only defined for a DAG, and how to detect the cycle that breaks it
- **Minimum viable**: BFS and DFS only; defer topological sort.

### Day 26 — 2026-12-11 (weekday, 4h, core)

- **Domain/Topic**: applied-ai / retrieval-chunking-embeddings
- **Objective**: Build a chunking and embedding pipeline from scratch over a real (small, non-proprietary) text corpus.
- **Artifact**: `applied-ai/retrieval-chunking-embeddings/ingest.py`
- **Verification**: pytest applied-ai/retrieval-chunking-embeddings/ passes against a committed sample corpus
- **Notes topic**: Why chunk size and overlap change what gets retrieved later, not just how it's stored
- **Minimum viable**: Fixed-size chunking only; defer overlap and semantic-boundary chunking.

### Day 27 — 2026-12-12 (weekend, 6h, core)

- **Domain/Topic**: applied-ai / retrieval-vector-search
- **Objective**: Build vector search over yesterday's embeddings, then add a hybrid (keyword + vector) retrieval mode.
- **Artifact**: `applied-ai/retrieval-vector-search/search.py`
- **Verification**: pytest applied-ai/retrieval-vector-search/ passes; benchmarks.json compares vector-only vs hybrid recall on a labeled query set
- **Notes topic**: Why pure vector search misses exact-keyword queries that hybrid retrieval catches
- **Minimum viable**: Vector-only search; defer the hybrid mode to day 30's evaluation day.
- **Prerequisites**: 26

### Day 28 — 2026-12-13 (weekend, 6h, core)

- **Domain/Topic**: python / python-profiling
- **Objective**: Weekly review: re-solve the scheduled DSA/ML topics from a blank file, audit the week against the constitution, re-plan.
- **Artifact**: `progress/reviews/week-04.md`
- **Verification**: roadmap review writes the Generated section; both re-solves recorded pass/fail
- **Notes topic**: What the re-solve revealed about which parts of backtracking and graphs-I were not actually retained
- **Minimum viable**: Re-solve one topic instead of two; log the skip honestly.
- **Prerequisites**: 23, 25

**Review** (day 28): resolves sliding-window, linked-lists, trees-traversals, heaps-priority-queues, backtracking

## Week 5 — Graphs II, retrieval evaluation, and the first neural net

Domains: dsa, applied-ai, ml · Outcome: Union-Find and Dijkstra solved cold; retrieval quality measured, not assumed; a neural net's forward/backward pass built from scratch.

### Day 29 — 2026-12-14 (weekday, 4h, core)

- **Domain/Topic**: dsa / graphs-union-find-dijkstra
- **Objective**: Solve Union-Find and Dijkstra's-algorithm problems from scratch.
- **Artifact**: `dsa/graphs-union-find-dijkstra/solutions.py`
- **Verification**: pytest dsa/graphs-union-find-dijkstra/ passes; complexity asserted per solution
- **Notes topic**: Why union-by-rank plus path compression gets Union-Find to near-O(1) amortized, and what breaks without either
- **Minimum viable**: Union-Find only; defer Dijkstra.

### Day 30 — 2026-12-15 (weekday, 4h, core)

- **Domain/Topic**: applied-ai / retrieval-evaluation
- **Objective**: Build a retrieval evaluation harness: recall@k and a faithfulness check against a labeled query/answer set, comparing vector-only vs hybrid from day 27.
- **Artifact**: `applied-ai/retrieval-evaluation/eval_harness.py`
- **Verification**: pytest applied-ai/retrieval-evaluation/ passes; benchmarks.json reports recall@k and faithfulness for both retrieval modes
- **Notes topic**: Why 'faithfulness' (did the answer actually use the retrieved text) is a different failure mode than 'recall' (was the right text even retrieved)
- **Minimum viable**: Recall@k only; defer the faithfulness check.
- **Prerequisites**: 27

### Day 31 — 2026-12-16 (weekday, 4h, core)

- **Domain/Topic**: applied-ai / agent-control-flow
- **Objective**: Build a multi-step planning loop: the agent decides how many steps it needs and in what order, rather than following a fixed script.
- **Artifact**: `applied-ai/agent-control-flow/planner.py`
- **Verification**: pytest applied-ai/agent-control-flow/ passes against at least 3 distinct planning scenarios
- **Notes topic**: Why a fixed-step loop (like day 6's) breaks on a task whose step count isn't known in advance
- **Minimum viable**: One planning scenario instead of three; defer the rest.
- **Prerequisites**: 6

### Day 32 — 2026-12-17 (weekday, 4h, core)

- **Domain/Topic**: ml / neural-net-scratch
- **Objective**: Implement a 2-layer neural network's forward and backward pass from scratch in NumPy — no autograd.
- **Artifact**: `ml/neural-net-scratch/network.py`
- **Verification**: pytest ml/neural-net-scratch/ passes: gradient-checked against a numerical approximation
- **Notes topic**: Why backprop is the chain rule applied layer by layer, and what a gradient check actually verifies
- **Minimum viable**: Forward pass and a numerical gradient check only; defer the full backward-pass implementation.
- **Prerequisites**: 10

### Day 33 — 2026-12-18 (weekday, 4h, core)

- **Domain/Topic**: ml / neural-net-scratch
- **Objective**: Reimplement day 32's network using torch.autograd and compare training curves.
- **Artifact**: `ml/neural-net-scratch/network_torch.py`
- **Verification**: pytest ml/neural-net-scratch/test_network_torch.py passes; benchmarks.json compares loss curves, scratch vs torch
- **Notes topic**: What torch.autograd buys you beyond 'less code to write' — and what it hides about what's actually happening
- **Minimum viable**: Get the torch version training; defer the loss-curve comparison plot/analysis.

### Day 34 — 2026-12-19 (weekend, 6h, core)

- **Domain/Topic**: applied-ai / multi-agent-orchestration
- **Objective**: Extend day 31's planner to coordinate two specialized agents (e.g. a researcher and a writer) rather than one generalist.
- **Artifact**: `applied-ai/multi-agent-orchestration/orchestrator.py`
- **Verification**: pytest applied-ai/multi-agent-orchestration/ passes against a 2-agent handoff scenario
- **Notes topic**: Why splitting one agent's responsibilities into two narrower agents can reduce failure modes, and where it adds coordination overhead instead
- **Minimum viable**: A single hand-off between two agents; defer any retry/escalation logic between them.
- **Prerequisites**: 31

### Day 35 — 2026-12-20 (weekend, 6h, core)

- **Domain/Topic**: ml / neural-net-scratch
- **Objective**: Weekly review: re-solve the scheduled DSA/ML topics from a blank file, audit the week against the constitution, re-plan. Milestone check: is code-review-triage-agent ready to start?
- **Artifact**: `progress/reviews/week-05.md`
- **Verification**: roadmap review writes the Generated section; both re-solves recorded pass/fail; roadmap coverage shows milestone readiness
- **Notes topic**: What the re-solve revealed about which parts of graphs-II were not actually retained
- **Minimum viable**: Re-solve one topic instead of two; log the skip honestly.
- **Prerequisites**: 29, 32

**Review** (day 35): resolves binary-search, stacks-monotonic, graphs-bfs-dfs-topo, gradient-descent-scratch

## Week 6 — DP I and Claude-specific agentic tooling (slip-risk week: holiday period)

Domains: dsa, applied-ai, systems · Outcome: 1D dynamic programming solved cold; Claude Code skills, the Claude Agent SDK, and MCP practiced as vehicles for the generic agentic patterns already learned.

### Day 36 — 2026-12-21 (weekday, 4h, core)

- **Domain/Topic**: dsa / dp-1d
- **Objective**: Solve 1D dynamic programming problems from scratch: climbing stairs, house robber, coin change.
- **Artifact**: `dsa/dp-1d/solutions.py`
- **Verification**: pytest dsa/dp-1d/ passes; complexity asserted per solution
- **Notes topic**: Why memoizing a recursive solution and building a bottom-up table are the same idea with different call orders
- **Minimum viable**: Climbing stairs and house robber only; defer coin change.

### Day 37 — 2026-12-22 (weekday, 4h, optional)

- **Domain/Topic**: applied-ai / claude-code-skills-vehicle
- **Objective**: Build a Claude Code skill that implements day 31's multi-step planning pattern — the generic concept is the practice objective, Claude Code's skill mechanism is just the vehicle.
- **Artifact**: `applied-ai/claude-code-skills-vehicle/skill_demo.py`
- **Verification**: pytest applied-ai/claude-code-skills-vehicle/ passes; the skill reproduces day 31's planning behavior
- **Notes topic**: What a Claude Code skill actually packages (instructions plus optional tools), and why that's the same shape as the planner from day 31
- **Minimum viable**: Describe the skill's structure in NOTES.md without a full working implementation.
- **Prerequisites**: 31

### Day 38 — 2026-12-23 (weekday, 4h, optional)

- **Domain/Topic**: applied-ai / claude-agent-sdk
- **Objective**: Use the Claude Agent SDK to reimplement day 34's two-agent orchestration — the generic concept (multi-agent handoff) is what's being practiced, the SDK is the vehicle.
- **Artifact**: `applied-ai/claude-agent-sdk/orchestrator_sdk.py`
- **Verification**: pytest applied-ai/claude-agent-sdk/ passes against the same 2-agent handoff scenario as day 34
- **Notes topic**: What the Claude Agent SDK handles for you that day 34's hand-rolled orchestrator had to do manually
- **Minimum viable**: Describe the SDK's orchestration primitives in NOTES.md without a full working port.
- **Prerequisites**: 34

### Day 39 — 2026-12-24 (weekday, 4h, core)

- **Domain/Topic**: systems / systems-serving-batching-caching
- **Objective**: Design and simulate a request-batching and response-caching layer for a model-serving endpoint.
- **Artifact**: `systems/serving-batching-caching/design.md`
- **Verification**: systems/serving-batching-caching/simulate.py demonstrates throughput improvement from batching under a stated load profile
- **Notes topic**: Why batching trades latency for throughput, and why that's the right trade for some workloads and the wrong one for others
- **Minimum viable**: Design document only; defer the simulation script.

### Day 40 — 2026-12-25 (weekday, 4h, optional)

- **Domain/Topic**: systems / systems-queues-backpressure
- **Objective**: Add a bounded queue with backpressure to day 39's design: what happens when requests arrive faster than they can be served.
- **Artifact**: `systems/queues-backpressure/queue_sim.py`
- **Verification**: pytest systems/queues-backpressure/ passes, including a test that the queue rejects rather than grows unbounded under sustained overload
- **Notes topic**: Why an unbounded queue under sustained overload just delays the failure instead of preventing it
- **Minimum viable**: Bounded queue only; defer the backpressure-signaling mechanism.
- **Prerequisites**: 39

### Day 41 — 2026-12-26 (weekend, 6h, optional)

- **Domain/Topic**: applied-ai / mcp-server-client
- **Objective**: Build an MCP server exposing day 6's weather-lookup tool, and an MCP client that calls it — the generic concept (tool-use over a standard protocol) is what's being practiced.
- **Artifact**: `applied-ai/mcp-server-client/server.py`
- **Verification**: pytest applied-ai/mcp-server-client/ passes: the MCP client successfully calls the MCP server's tool
- **Notes topic**: What MCP standardizes that day 6's ad-hoc tool-calling loop didn't: a protocol other clients and servers can also speak
- **Minimum viable**: Describe the MCP server/client shape in NOTES.md without a full working implementation.
- **Prerequisites**: 6

### Day 42 — 2026-12-27 (weekend, 6h, core)

- **Domain/Topic**: ml / neural-net-scratch
- **Objective**: Weekly review: re-solve the scheduled DSA/ML topics from a blank file, audit the week against the constitution, re-plan.
- **Artifact**: `progress/reviews/week-06.md`
- **Verification**: roadmap review writes the Generated section; both re-solves recorded pass/fail
- **Notes topic**: What the re-solve revealed about which parts of DP-1D were not actually retained
- **Minimum viable**: Re-solve one topic instead of two; log the skip honestly.
- **Prerequisites**: 36

**Review** (day 42): resolves trees-construct-serialize, linked-lists, graphs-union-find-dijkstra, neural-net-scratch

## Week 7 — DP II, agent error handling, and inference-serving system design (slip-risk week: holiday period)

Domains: dsa, applied-ai, systems · Outcome: 2D dynamic programming solved cold; agent error handling and non-deterministic-system evaluation deepened; an inference-serving system designed under stated constraints.

### Day 43 — 2026-12-28 (weekday, 4h, core)

- **Domain/Topic**: dsa / dp-2d
- **Objective**: Solve 2D dynamic programming problems from scratch: grid paths, longest common subsequence, edit distance.
- **Artifact**: `dsa/dp-2d/solutions.py`
- **Verification**: pytest dsa/dp-2d/ passes; complexity asserted per solution
- **Notes topic**: Why edit distance's DP table is a grid of 'cost to transform this prefix into that prefix,' not a formula to memorize
- **Minimum viable**: Grid paths and LCS only; defer edit distance.
- **Prerequisites**: 36

### Day 44 — 2026-12-29 (weekday, 4h, core)

- **Domain/Topic**: applied-ai / agent-error-handling
- **Objective**: Extend day 6's malformed-tool-call retry to handle a wider failure taxonomy: timeouts, partial responses, and a tool that raises instead of returning malformed output.
- **Artifact**: `applied-ai/agent-error-handling/error_taxonomy.py`
- **Verification**: pytest applied-ai/agent-error-handling/ passes against all 3 new failure cases plus day 6's original 3
- **Notes topic**: Why a tool that raises needs different handling than a tool that returns a malformed result — one is 'retry with correction,' the other might not be retryable at all
- **Minimum viable**: Handle the timeout case only; defer the other two.
- **Prerequisites**: 6

### Day 45 — 2026-12-30 (weekday, 4h, core)

- **Domain/Topic**: applied-ai / eval-nondeterministic-systems
- **Objective**: Build an LLM-as-judge evaluator for a non-deterministic task, and measure the judge's own agreement rate against a human-labeled sample.
- **Artifact**: `applied-ai/eval-nondeterministic-systems/judge.py`
- **Verification**: pytest applied-ai/eval-nondeterministic-systems/ passes; benchmarks.json reports judge-vs-human agreement rate
- **Notes topic**: Why an LLM-as-judge needs its own accuracy measured against ground truth — a judge you haven't validated is just a second unverified opinion
- **Minimum viable**: Run the judge on 5 cases instead of 20; still report the agreement rate on that smaller sample.

### Day 46 — 2026-12-31 (weekday, 4h, optional)

- **Domain/Topic**: systems / systems-feature-stores
- **Objective**: Design a feature store's read/write path for a model that needs both batch-computed and real-time features.
- **Artifact**: `systems/feature-stores/design.md`
- **Verification**: systems/feature-stores/design.md states the read/write path, consistency guarantees, and staleness tolerance explicitly
- **Notes topic**: Why serving the same feature computed two different ways (batch vs real-time) risks training/serving skew
- **Minimum viable**: Read path only; defer the write-path and staleness design.

### Day 47 — 2027-01-01 (weekday, 4h, core)

- **Domain/Topic**: systems / systems-inference-serving-design
- **Objective**: Design an inference-serving system handling 2+ model backends, stating its batching, caching, and failure-isolation strategy — this is milestone 2's design document.
- **Artifact**: `systems/inference-serving-design/design.md`
- **Verification**: systems/inference-serving-design/design.md names the backends, the batching/caching strategy, and what happens when one backend is unhealthy
- **Notes topic**: Why failure isolation between backends matters even when only one backend is unhealthy: how a naive design still breaks for the other
- **Minimum viable**: Name the backends and the failure-isolation strategy; defer the batching/caching detail.
- **Prerequisites**: 39, 40

### Day 48 — 2027-01-02 (weekend, 6h, core)

- **Domain/Topic**: applied-ai / rate-limiting-caching
- **Objective**: Implement rate-limit backoff and response caching for day 20's LLM API client, and measure the request-count reduction from caching.
- **Artifact**: `applied-ai/rate-limiting-caching/client_with_backoff.py`
- **Verification**: pytest applied-ai/rate-limiting-caching/ passes, including a simulated 429 response triggering backoff
- **Notes topic**: Why exponential backoff with jitter avoids a thundering-herd retry storm that plain fixed-delay retry doesn't
- **Minimum viable**: Backoff only; defer the caching layer.
- **Prerequisites**: 20

### Day 49 — 2027-01-03 (weekend, 6h, core)

- **Domain/Topic**: ml / neural-net-scratch
- **Objective**: Weekly review: re-solve the scheduled DSA/ML topics from a blank file, audit the week against the constitution, re-plan. Milestone check: is inference-gateway ready to start?
- **Artifact**: `progress/reviews/week-07.md`
- **Verification**: roadmap review writes the Generated section; both re-solves recorded pass/fail; roadmap coverage shows milestone readiness
- **Notes topic**: What the re-solve revealed about which parts of DP-2D were not actually retained
- **Minimum viable**: Re-solve one topic instead of two; log the skip honestly.
- **Prerequisites**: 43

**Review** (day 49): resolves trees-traversals, heaps-priority-queues, dp-1d, gradient-descent-scratch

## Week 8 — Intervals/greedy, transformers, and inference optimization

Domains: dsa, ml, applied-ai · Outcome: Intervals and greedy scheduling solved cold; attention built from scratch; a model quantized with the accuracy/latency/memory trade-off measured, not claimed.

### Day 50 — 2027-01-04 (weekday, 4h, core)

- **Domain/Topic**: dsa / intervals-greedy
- **Objective**: Solve intervals and greedy-scheduling problems from scratch: merge intervals, meeting rooms, activity selection.
- **Artifact**: `dsa/intervals-greedy/solutions.py`
- **Verification**: pytest dsa/intervals-greedy/ passes; complexity asserted per solution
- **Notes topic**: Why sorting by end time (not start time) is what makes activity selection's greedy choice provably optimal
- **Minimum viable**: Merge intervals only; defer meeting rooms and activity selection.

### Day 51 — 2027-01-05 (weekday, 4h, core)

- **Domain/Topic**: ml / transformers-attention-scratch
- **Objective**: Implement scaled dot-product attention from scratch in NumPy: query/key/value projections, the attention-score matrix, and the weighted sum.
- **Artifact**: `ml/transformers-attention-scratch/attention.py`
- **Verification**: pytest ml/transformers-attention-scratch/ passes against a known attention-output test case
- **Notes topic**: Why attention scores are divided by sqrt(d_k) before the softmax, and what happens to the gradient if you skip that scaling
- **Minimum viable**: Single-head attention only; defer multi-head.
- **Prerequisites**: 32

### Day 52 — 2027-01-06 (weekday, 4h, core)

- **Domain/Topic**: ml / transformers-attention-scratch
- **Objective**: Reimplement day 51's attention using a library's multi-head attention layer and compare outputs on the same input.
- **Artifact**: `ml/transformers-attention-scratch/attention_torch.py`
- **Verification**: pytest ml/transformers-attention-scratch/test_attention_torch.py passes: outputs match day 51's single-head case within tolerance
- **Notes topic**: What multi-head attention buys over single-head, and why the library version's API hides the Q/K/V projections day 51 made explicit
- **Minimum viable**: Get the library layer running; defer the numerical-match comparison against day 51.

### Day 53 — 2027-01-07 (weekday, 4h, core)

- **Domain/Topic**: applied-ai / inference-optimization-quantization
- **Objective**: Quantize a small trained model (int8) and measure the accuracy/latency/memory trade-off against the unquantized baseline — this feeds the compression-validation-suite milestone directly.
- **Artifact**: `applied-ai/inference-optimization-quantization/quantize.py`
- **Verification**: pytest applied-ai/inference-optimization-quantization/ passes; benchmarks.json reports accuracy, latency, and memory before/after quantization
- **Notes topic**: Why quantization's latency win isn't free: what accuracy you give up, and how to decide if that trade is worth it
- **Minimum viable**: Measure latency and memory only; defer the accuracy comparison to day 59.

### Day 54 — 2027-01-08 (weekday, 4h, core)

- **Domain/Topic**: applied-ai / red-teaming-adversarial-prompts
- **Objective**: Build a small adversarial-prompt test suite against day 20's LLM client: prompt injection, jailbreak attempts, and off-topic redirection.
- **Artifact**: `applied-ai/red-teaming-adversarial-prompts/attack_suite.py`
- **Verification**: pytest applied-ai/red-teaming-adversarial-prompts/ passes; benchmarks.json reports pass rate against each attack category
- **Notes topic**: Why a model that resists one phrasing of a prompt injection often still falls to a paraphrase of the same attack
- **Minimum viable**: Prompt injection category only; defer jailbreak and off-topic redirection.
- **Prerequisites**: 20

### Day 55 — 2027-01-09 (weekend, 6h, optional)

- **Domain/Topic**: ml / training-dynamics
- **Objective**: Train day 32's network with and without regularization (dropout, weight decay) and compare generalization on a held-out set.
- **Artifact**: `ml/training-dynamics/regularization.py`
- **Verification**: pytest ml/training-dynamics/ passes; benchmarks.json shows train/validation loss gap with and without regularization
- **Notes topic**: Why a shrinking training loss alongside a growing validation loss is overfitting, not 'still improving'
- **Minimum viable**: Dropout only; defer the weight-decay comparison.
- **Prerequisites**: 32

### Day 56 — 2027-01-10 (weekend, 6h, core)

- **Domain/Topic**: ml / neural-net-scratch
- **Objective**: Weekly review: re-solve the scheduled DSA/ML topics from a blank file, audit the week against the constitution, re-plan.
- **Artifact**: `progress/reviews/week-08.md`
- **Verification**: roadmap review writes the Generated section; both re-solves recorded pass/fail
- **Notes topic**: What the re-solve revealed about which parts of intervals-greedy were not actually retained
- **Minimum viable**: Re-solve one topic instead of two; log the skip honestly.
- **Prerequisites**: 50

**Review** (day 56): resolves backtracking, graphs-bfs-dfs-topo, graphs-union-find-dijkstra, dp-2d

## Week 9 — Tries, classical ML evaluation, and milestone 1 build

Domains: dsa, ml, applied-ai, systems · Outcome: Tries solved cold; a classical ML baseline trained and evaluated against the neural net; the code-review-triage-agent milestone's scaffolding and eval set built.

### Day 57 — 2027-01-11 (weekday, 4h, core)

- **Domain/Topic**: dsa / tries
- **Objective**: Solve trie problems from scratch: insert/search/prefix-search, word search II.
- **Artifact**: `dsa/tries/solutions.py`
- **Verification**: pytest dsa/tries/ passes; complexity asserted per solution
- **Notes topic**: Why a trie's prefix search is O(k) in the query length regardless of how many words are stored, unlike scanning a list
- **Minimum viable**: Insert/search only; defer prefix-search and word-search-II.

### Day 58 — 2027-01-12 (weekday, 4h, core)

- **Domain/Topic**: ml / classical-ml-comparison
- **Objective**: Train a classical ML baseline (gradient-boosted trees or logistic regression) on a labeled dataset and compare against day 32's neural net on the same split.
- **Artifact**: `ml/classical-ml-comparison/baseline.py`
- **Verification**: pytest ml/classical-ml-comparison/ passes; benchmarks.json reports accuracy for both models on the same held-out split
- **Notes topic**: Why a classical model matching or beating a neural net on a small tabular dataset isn't a surprise — it's the expected result
- **Minimum viable**: Train the classical baseline only; defer the neural-net comparison to day 59.
- **Prerequisites**: 32

### Day 59 — 2027-01-13 (weekday, 4h, core)

- **Domain/Topic**: ml / ml-evaluation-methodology
- **Objective**: Build a small evaluation methodology document and harness: dataset split strategy, the metric chosen and why, and the baseline every claim in this programme has been compared against.
- **Artifact**: `ml/ml-evaluation-methodology/eval_report.py`
- **Verification**: pytest ml/ml-evaluation-methodology/ passes; the report cross-references every ML day's benchmarks.json from this programme
- **Notes topic**: Why 'the metric' isn't a fixed choice — accuracy, F1, and recall tell different stories, and the eval methodology has to name which one matters and why
- **Minimum viable**: Document the methodology; defer cross-referencing every prior day's benchmark.
- **Prerequisites**: 58

### Day 60 — 2027-01-14 (weekday, 4h, core)

- **Domain/Topic**: applied-ai / milestone1-triage-agent-scaffold
- **Objective**: Scaffold the code-review-triage-agent: ingest a PR diff, run it through day 44's error-handling-aware tool loop with a linter and test-runner tool.
- **Artifact**: `applied-ai/milestone1-triage-agent-scaffold/triage.py`
- **Verification**: pytest applied-ai/milestone1-triage-agent-scaffold/ passes against a sample PR diff fixture
- **Notes topic**: Why triaging a PR diff needs the same malformed-tool-call recovery as day 6/44 — a linter's output is just another tool result that can come back malformed
- **Minimum viable**: Triage against one PR diff fixture only; defer the FastAPI wrapper.
- **Prerequisites**: 24, 31, 44

### Day 61 — 2027-01-15 (weekday, 4h, core)

- **Domain/Topic**: applied-ai / milestone1-triage-agent-eval
- **Objective**: Build a labeled set of real PRs with known issues and score day 60's agent's precision/recall against a no-agent baseline — this is the milestone's actual evaluation evidence.
- **Artifact**: `applied-ai/milestone1-triage-agent-eval/eval_set.py`
- **Verification**: pytest applied-ai/milestone1-triage-agent-eval/ passes; benchmarks.json reports precision/recall vs the no-agent baseline
- **Notes topic**: Why 'the agent caught the bug in the demo' isn't evidence — precision/recall against a labeled set, the same discipline as day 24's prompt eval, is
- **Minimum viable**: 5 labeled PRs instead of 20; still report precision/recall on that smaller set.
- **Prerequisites**: 60

### Day 62 — 2027-01-16 (weekend, 6h, optional)

- **Domain/Topic**: systems / systems-distributed-fundamentals
- **Objective**: Design a distributed system's consistency and partition-tolerance trade-off for a specific scenario (e.g. a shared feature cache across model replicas).
- **Artifact**: `systems/distributed-fundamentals/design.md`
- **Verification**: systems/distributed-fundamentals/design.md names the consistency model chosen and what it costs under a network partition
- **Notes topic**: Why 'strongly consistent and always available during a partition' isn't a real option — CAP forces an explicit choice, not an oversight to fix
- **Minimum viable**: Name the consistency model choice; defer the full partition-behavior analysis.

### Day 63 — 2027-01-17 (weekend, 6h, core)

- **Domain/Topic**: dsa / tries
- **Objective**: Weekly review: re-solve the scheduled DSA/ML topics from a blank file, audit the week against the constitution, re-plan. Milestone check: is compression-validation-suite ready to start?
- **Artifact**: `progress/reviews/week-09.md`
- **Verification**: roadmap review writes the Generated section; both re-solves recorded pass/fail; roadmap coverage shows milestone readiness
- **Notes topic**: What the re-solve revealed about which parts of tries were not actually retained
- **Minimum viable**: Re-solve one topic instead of two; log the skip honestly.
- **Prerequisites**: 57

**Review** (day 63): resolves neural-net-scratch, dp-1d, intervals-greedy, transformers-attention-scratch, training-dynamics, tries, classical-ml-comparison, ml-evaluation-methodology

## Week 10 — Bit manipulation, design problems, and milestone 2 build — programme wrap-up

Domains: dsa, applied-ai, git · Outcome: Bit manipulation and LRU/LFU design solved cold; the inference-gateway milestone built; the full 70-day programme closed out and audited against the constitution.

### Day 64 — 2027-01-18 (weekday, 4h, core)

- **Domain/Topic**: dsa / bit-manipulation
- **Objective**: Solve bit-manipulation problems from scratch: single number (XOR trick), counting bits, subset generation via bitmask.
- **Artifact**: `dsa/bit-manipulation/solutions.py`
- **Verification**: pytest dsa/bit-manipulation/ passes; complexity asserted per solution
- **Notes topic**: Why XOR-ing every element cancels all pairs and leaves only the unmatched one — and why that only works when every other element appears exactly twice
- **Minimum viable**: Single number and counting bits only; defer bitmask subset generation.

### Day 65 — 2027-01-19 (weekday, 4h, core)

- **Domain/Topic**: dsa / design-lru-lfu-cache
- **Objective**: Implement an LRU cache from scratch (hashmap + doubly-linked list, O(1) get/put), then an LFU cache variant.
- **Artifact**: `dsa/design-lru-lfu-cache/lru_cache.py`
- **Verification**: pytest dsa/design-lru-lfu-cache/ passes; benchmarks.json confirms O(1) get/put against a growing cache size
- **Notes topic**: Why a hashmap alone can't give O(1) eviction-of-least-recently-used, and what the doubly-linked list adds
- **Minimum viable**: LRU cache only; defer the LFU variant.

### Day 66 — 2027-01-20 (weekday, 4h, core)

- **Domain/Topic**: applied-ai / milestone2-inference-gateway-scaffold
- **Objective**: Build the inference-gateway's core: route requests across 2 model backends behind a single FastAPI endpoint, with request batching from day 39's design.
- **Artifact**: `applied-ai/milestone2-inference-gateway-scaffold/gateway.py`
- **Verification**: pytest applied-ai/milestone2-inference-gateway-scaffold/ passes: requests route to both backends and batch per day 39's strategy
- **Notes topic**: Why routing and batching have to be designed together — batching across backends with different latency profiles can starve the faster one
- **Minimum viable**: Route to 2 backends without batching; defer the batching layer.
- **Prerequisites**: 39, 47

### Day 67 — 2027-01-21 (weekday, 4h, core)

- **Domain/Topic**: applied-ai / milestone2-inference-gateway-resilience
- **Objective**: Add health checks and automatic fallback to day 66's gateway, then load-test it and measure success rate with a backend forced unhealthy, against a no-fallback baseline.
- **Artifact**: `applied-ai/milestone2-inference-gateway-resilience/health_check.py`
- **Verification**: pytest applied-ai/milestone2-inference-gateway-resilience/ passes; benchmarks.json reports success rate with and without fallback, one backend forced unhealthy
- **Notes topic**: Why a health check needs its own failure handling — a health check that hangs is worse than no health check at all
- **Minimum viable**: Health check only; defer the automatic-fallback routing.
- **Prerequisites**: 66

### Day 68 — 2027-01-22 (weekday, 4h, optional)

- **Domain/Topic**: git / git-advanced-workflows
- **Objective**: Practice an interactive rebase to clean up a messy commit history, a git bisect to find a regression, and resolve a seeded merge conflict.
- **Artifact**: `git/git-advanced-workflows/drill.sh`
- **Verification**: drill.sh exits 0 after the rebase, bisect, and conflict-resolution steps all complete
- **Notes topic**: Why git bisect's binary search over commit history is the same algorithmic idea as day 8's binary search, applied to history instead of an array
- **Minimum viable**: Bisect drill only; defer rebase and conflict-resolution drills.
- **Prerequisites**: 4

### Day 69 — 2027-01-23 (weekend, 6h, optional)

- **Domain/Topic**: applied-ai / applied-ai-stretch
- **Objective**: Stretch/buffer day: extend either the retrieval pipeline (day 27/30) or the triage agent (day 60/61) with one additional real eval case, or catch up on any carried day.
- **Artifact**: `applied-ai/applied-ai-stretch/extension.py`
- **Verification**: pytest applied-ai/applied-ai-stretch/ passes against the one new eval case added
- **Notes topic**: What the extra eval case revealed that the original set didn't cover
- **Minimum viable**: Use this day entirely to catch up on any carried day instead; that satisfies the day's purpose.

### Day 70 — 2027-01-24 (weekend, 6h, core)

- **Domain/Topic**: python / python-typing-static-analysis
- **Objective**: Final weekly review: re-solve the scheduled DSA/ML topics from a blank file, audit the full 10-week programme against the constitution, and record final role-coverage readiness.
- **Artifact**: `progress/reviews/week-10.md`
- **Verification**: roadmap review writes the Generated section; roadmap coverage reports final readiness per role; roadmap validate --strict exits 0
- **Notes topic**: What changed between the week-1 plan and what was actually built by day 70 — and why that gap is the real record of what was learned, not a failure to follow the plan exactly
- **Minimum viable**: Re-solve one topic instead of two; log the skip honestly. The validate --strict gate still applies.
- **Prerequisites**: 64, 65

**Review** (day 70): resolves dp-2d, intervals-greedy, transformers-attention-scratch, training-dynamics, tries, classical-ml-comparison, ml-evaluation-methodology, bit-manipulation, design-lru-lfu-cache

