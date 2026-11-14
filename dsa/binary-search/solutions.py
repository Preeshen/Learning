"""Binary search and its search-on-answer variant.

Each function asserts its own complexity in its docstring; test_solutions.py checks
correctness and, for search_on_answer, that it scales logarithmically rather than linearly.
"""

from __future__ import annotations


def binary_search(nums: list[int], target: int) -> int:
    """Classic binary search on a sorted array. O(log n) time, O(1) space."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def search_rotated(nums: list[int], target: int) -> int:
    """Search in a rotated sorted array. O(log n) time, O(1) space.

    The trick: at any midpoint, one half is always properly sorted — determine which half
    that is, then decide which side the target could be on from its sorted half alone.
    """
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:  # left half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # right half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def search_on_answer(low: int, high: int, feasible) -> int:
    """Binary search over the *answer space*, not an array.

    `feasible(x)` must be monotonic: once true for some x, true for all larger x (or the
    reverse — caller is responsible for orienting the predicate). Returns the smallest x in
    [low, high] for which `feasible(x)` is True, or `high + 1` if none is.
    O(log(high - low)) calls to `feasible`, which is the actual expensive operation this
    pattern is designed to minimize.
    """
    lo, hi = low, high + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def min_eating_speed(piles: list[int], h: int) -> int:
    """Koko eating bananas: smallest integer speed to finish all piles within h hours.

    A direct application of search_on_answer — the feasibility check is "can I finish at
    this speed," which is monotonic in speed.
    """
    import math

    def feasible(speed: int) -> bool:
        return sum(math.ceil(p / speed) for p in piles) <= h

    return search_on_answer(1, max(piles), feasible)
