# Sliding window

**Problem it solves**: finding the best contiguous subarray/substring satisfying some condition,
without rescanning the whole sequence for every possible window.

**Mechanism**: maintain a window [left, right] and a running summary of its contents (a count map,
a sum, a missing-character counter). Growing the window updates the summary incrementally;
shrinking it does the same in reverse — neither direction ever re-derives the summary from
scratch, which is what keeps the whole algorithm O(n) instead of O(n^2).

**Failure modes**: in `min_window_substring`, the `missing` counter must only increment back up
when a character's count crosses from 0 to positive while shrinking — incrementing it on every
character removal (even ones not in `t`) would prematurely declare the window invalid and shrink
past the actual answer.

**Trade-offs**: sliding window needs the "best window" property to be monotonic in window size in
some sense (shrinking never un-satisfies a satisfied window in the fixed-size case, or the
missing-count logic correctly tracks validity in the variable-size case) — it doesn't apply to
every "subarray" problem, only ones where a window's validity can be tracked incrementally rather
than needing to be recomputed from scratch.
