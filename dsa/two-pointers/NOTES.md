# Two pointers

**Problem it solves**: finding a pair (or more) of elements satisfying some condition on a
sorted array, without checking every pair.

**Mechanism**: two indices move toward each other (or together in one direction) based on a
comparison that lets one side be ruled out entirely at each step — e.g., in `two_sum_sorted`, if
the current pair's sum is too small, the only way to increase it is to move the low pointer up
(the high pointer is already as large as it can usefully be).

**Failure modes**: `three_sum`'s duplicate-skipping logic is the easy part to get wrong — skipping
duplicates at the *outer* loop (`nums[i] == nums[i-1]`) prevents duplicate triplets starting with
the same first element, but forgetting the *inner* skip (`nums[lo] == nums[lo-1]` after a match)
produces duplicate triplets within the same `i`.

**Trade-offs**: two pointers requires sorted input (or a problem that's naturally sorted), which
costs O(n log n) up front if the input isn't already sorted — still a net win over O(n^2), but not
free. `max_area_container`'s greedy pointer-move (always move the shorter wall) only works because
it's provably safe to discard the shorter wall's current position; that argument has to be made
explicitly, not assumed by analogy to other two-pointer problems.
