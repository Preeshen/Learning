## Day 001 — 2026-11-14 — project-tooling {#day-001}

**Status**: complete · **Commit**: e50b89af73fd720e2fea86de1900ad4304d16350 · **Domain**: python · **Effort**: 4 h

**Built**: Env report script reading uv.lock, with a committed lockfile

**Broke**: tomllib needs uv.lock to exist before env_report can read it

**Non-obvious**: A lockfile not committed is not a lockfile

## Day 002 — 2026-11-14 — arrays-hashing {#day-002}

**Status**: complete · **Commit**: ed68ddcdf1c9338bef8d442cece24eb9eec7158b · **Domain**: dsa · **Effort**: 4 h

**Built**: Hashmap two-sum/group-anagrams/longest-consecutive/prefix-sum solutions with a scaling benchmark vs the naive O(n^2) baseline

**Broke**: longest_consecutive_sequence without the n-1-not-in-set guard re-walks every run from every element

**Non-obvious**: The speedup ratio has to grow with n to prove O(n) vs O(n^2); a single measurement at one size doesn't

## Day 003 — 2026-11-14 — two-pointers {#day-003}

**Status**: complete · **Commit**: 442ea708a0f6b94e1e98e2c025a86701f2c99b26 · **Domain**: dsa · **Effort**: 4 h

**Built**: Two-pointer solutions for two-sum-sorted, palindrome check, container-with-most-water, and three-sum

**Broke**: three_sum produced duplicate triplets until the inner-loop duplicate skip was added after the outer-loop skip

**Non-obvious**: Skipping duplicates at the outer loop alone isn't enough; the inner pointer needs its own skip after a match

## Day 004 — 2026-11-14 — git-fundamentals {#day-004}

**Status**: skipped · **Commit**: - · **Domain**: git · **Effort**: 4 h

**Built**: -

**Broke**: -

**Non-obvious**: Deferred: optional day, prioritizing core DSA/ML/applied-ai content first per FR-018

## Day 005 — 2026-11-14 — sliding-window {#day-005}

**Status**: complete · **Commit**: 01cea047c2cba1b45d2943622677e0d69632f91f · **Domain**: dsa · **Effort**: 4 h

**Built**: Sliding-window solutions: longest-substring-without-repeating, min-window-substring, max-sum-subarray-of-size-k

**Broke**: min_window_substring's missing counter needs to increment only when a character's count crosses 0->positive while shrinking, not on every removal

**Non-obvious**: Sliding window's O(n) claim depends on the window's validity being tracked incrementally, not recomputed from scratch each step

## Day 006 — 2026-11-14 — tool-calling {#day-006}

**Status**: complete · **Commit**: 04c4dd633e3f1c7e2d8969447c28f749a8c47548 · **Domain**: applied-ai · **Effort**: 6 h

**Built**: Tool-calling loop with malformed-argument retry, wrapped behind FastAPI

**Broke**: First no-retry benchmark trial hit IndexError: the clean-path script needs a final-answer entry too, not just the tool call

**Non-obvious**: A malformed tool call is a prompt bug, not a transient failure -- bare retry reproduces the same error without telling the model what broke

**Re-solve**: arrays-hashing — PASSED

**Re-solve**: two-pointers — PASSED

## Day 007 — 2026-11-14 — arrays-hashing {#day-007}

**Status**: complete · **Commit**: 9a67c33597b471fdaa01b34c4815f207678d3127 · **Domain**: dsa · **Effort**: 6 h

**Built**: Week 1 review written; both scheduled re-solves ran from a blank file

**Broke**: Found and fixed a gate-check bug: review days were unconditionally failing because the generic check assumed a code artifact

**Non-obvious**: Re-solving from a blank file is a materially different test than recognizing the solution when reading it back

## Day 008 — 2026-11-14 — binary-search {#day-008}

**Status**: complete · **Commit**: 39080ed647cc804da38a0fa245c3958af2dd2191 · **Domain**: dsa · **Effort**: 4 h

**Built**: Binary search, rotated-array search, and search-on-answer (Koko eating bananas) from scratch

**Broke**: Nothing broke

**Non-obvious**: Search-on-answer reframes an optimization as a monotonic predicate you binary search over, not over an array

## Day 009 — 2026-11-14 — stacks-monotonic {#day-009}

**Status**: complete · **Commit**: ac1077a9806e262ca3ee89629931820d369876e9 · **Domain**: dsa · **Effort**: 4 h

**Built**: Valid-parentheses, daily-temperatures, and largest-rectangle-in-histogram via a monotonic stack

**Broke**: Nothing broke

**Non-obvious**: A monotonic stack's amortized O(n) claim depends on each element being pushed and popped exactly once -- a wrong push/pop condition silently degrades to O(n^2)

## Day 010 — 2026-11-14 — gradient-descent-scratch {#day-010}

**Status**: complete · **Commit**: 95c2e520cb87ddd7e7f47253b6c0a252378c7955 · **Domain**: ml · **Effort**: 4 h

**Built**: Gradient descent and linear regression from scratch in NumPy, benchmarked against scikit-learn's closed-form OLS fit

**Broke**: An untuned learning rate (tried 0.5 first) diverged instead of converging

**Non-obvious**: Gradient descent can match the closed-form answer, but only with real iteration and tuning cost that OLS skips entirely -- that gap is why neural nets need it at all

## Day 011 — 2026-11-14 — linked-lists {#day-011}

**Status**: complete · **Commit**: fb3227caf60304b3574b69e0eed6de7d27a29027 · **Domain**: dsa · **Effort**: 4 h

**Built**: Linked-list reversal, Floyd's cycle detection and cycle-start, merge-k-sorted-lists via a heap

**Broke**: Nothing broke

**Non-obvious**: Floyd's algorithm's correctness depends on a distance argument (the gap closes by 1 each step once both pointers are in the cycle) -- not something to pattern-match without deriving once

## Day 012 — 2026-11-14 — cost-latency-budgeting {#day-012}

**Status**: complete · **Commit**: ab792d883673093cd2a4277f32b6d8a02ac93819 · **Domain**: applied-ai · **Effort**: 4 h

**Built**: Token-cost and latency instrumentation wrapping day 6's tool-calling loop; benchmarked 20 requests

**Broke**: p50/p95 latency came out as ~0ms -- honest, not broken, since FixtureModel has no real network hop

**Non-obvious**: Fixture-backed days can prove the instrumentation works even though the latency numbers themselves won't be meaningful until run against a live API

## Day 013 — 2026-11-14 — trees-traversals {#day-013}

**Status**: complete · **Commit**: 3229389b1248ad17737690111400a47b003bc2ad · **Domain**: dsa · **Effort**: 6 h

**Built**: Tree traversals (in/pre/post-order), BST validation via ancestor bounds, max depth, and lowest common ancestor

**Broke**: A naive parent-only BST check passes a subtle violation (grandchild value out of grandparent's range); only the ancestor-bound version catches it

**Non-obvious**: Inorder traversal of a valid BST is always sorted -- that's sometimes a cheaper validation trick than bound-passing recursion, at the cost of O(n) extra space

