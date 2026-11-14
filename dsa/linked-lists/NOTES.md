# Linked lists (reversal, fast-slow, cycle, merge-k)

**Problem it solves**: sequential access with O(1) insertion/deletion at a known position, at the
cost of O(n) random access — and a family of pointer-manipulation problems that test whether you
can reason about aliasing correctly without a debugger.

**Mechanism**: reversal rewires `next` pointers one at a time while walking forward, keeping a
`prev` reference so nothing is lost. Fast-slow (Floyd's) pointers exploit that in a cycle, a
pointer moving twice as fast as another must eventually lap it — proving they'll meet requires a
distance argument (if the cycle has length C, the gap closes by 1 each step once both are in the
cycle, so they meet within C steps). Merge-k uses a heap to always pull the smallest head across
k lists in O(log k) rather than O(k) per step.

**Failure modes**: forgetting to save `curr.next` before overwriting it during reversal loses the
rest of the list permanently — there's no way to recover it once `curr.next = prev` runs. In cycle
detection, checking `slow == fast` by value instead of identity would falsely report a cycle in
any list with duplicate values.

**Trade-offs**: Floyd's algorithm is O(1) space, but a visited-set approach is easier to get right
first and is O(n) space — worth knowing both, since interviewers sometimes ask for the O(1) space
version specifically to test whether you know this exists.
