# Roadmap (generated — do not hand-edit; see roadmap.yaml)

70 days · 2 weeks · 2026-11-16 to 2027-01-24

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

