# Arrays & hashing (+ prefix sums)

**Problem it solves**: "have I seen this value before" and "what's the sum of this range"
questions that would otherwise require rescanning the array for every query.

**Mechanism**: a hash map gives O(1) average-case lookup, turning an O(n) "has this been seen"
scan into O(1). Prefix sums precompute cumulative totals so any range sum becomes a single
subtraction instead of a rescan, and combined with a hash map of prefix-sum frequencies, "count
subarrays summing to target" becomes O(n) instead of checking every (start, end) pair.

**Failure modes**: `longest_consecutive_sequence` without the `n - 1 not in num_set` guard would
re-walk the same run from every element in it, degrading from O(n) to O(n^2) silently — the bug
produces correct answers, just slowly, so it only shows up under a timing benchmark, not a
correctness test.

**Trade-offs**: `benchmarks.json` measured the hashmap-vs-naive gap directly rather than asserting
it: at n=100 the hashmap is 13x faster, but at n=10,000 it's 2,557x faster — the ratio growing with
n is the actual evidence of O(n) vs O(n^2), not just "it was faster once." A hash map costs O(n)
extra space that the naive nested loop doesn't pay.
