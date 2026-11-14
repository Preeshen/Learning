# Binary search (+ search-on-answer)

**Problem it solves**: finding a value — or the boundary of a property — in a sorted or
monotonic space without scanning every element.

**Mechanism**: halve the search space each step by comparing the midpoint against the target.
"Search on answer" generalizes this: instead of searching an array, search the space of possible
*answers* (e.g., eating speeds, days, capacities) using a monotonic feasibility predicate —
`feasible(x)` is false then true (or vice versa) as x increases, so the same halving logic applies.

**Failure modes**: off-by-one errors in the `lo`/`hi` update (classic: forgetting `mid + 1` /
`mid - 1` causes infinite loops on a 2-element range). In rotated-array search, the mistake is
checking `nums[lo] < nums[mid]` instead of `<=` — with 2 elements, strict `<` misclassifies which
half is sorted.

**Trade-offs**: search-on-answer trades an O(log range) search for O(range) calls to `feasible`,
which is only a win when `feasible` itself is expensive (as in `min_eating_speed`, where it sums
over all piles). For a cheap `feasible`, scanning range directly can be simpler to reason about.
