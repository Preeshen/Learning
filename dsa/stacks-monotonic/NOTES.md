# Stacks & monotonic stack

**Problem it solves**: "next greater/smaller element" style questions, and matching/nesting
validation — both need to look back at previously seen elements in a structured order.

**Mechanism**: a stack gives O(1) access to "the most recent unmatched thing." A *monotonic*
stack additionally keeps its elements sorted (increasing or decreasing) by popping anything that
violates the order before pushing — that pop is where the "next greater element" answer for the
popped item gets resolved, in amortized O(1) per element overall.

**Failure modes**: the amortized-O(n) claim depends on each element being pushed and popped at
most once — if the push/pop condition is wrong (e.g., `<=` instead of `<`), the stack can grow
unboundedly and the algorithm silently degrades to O(n^2) without an obvious symptom until tested
on larger inputs.

**Trade-offs**: the monotonic stack trades a more complex invariant to reason about for strictly
better asymptotic behavior than the naive nested-loop approach it replaces (O(n) vs O(n^2) for
daily_temperatures).
