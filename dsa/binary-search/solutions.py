"""Binary search and its search-on-answer variant.

Each function asserts its own complexity in its docstring; test_solutions.py checks
correctness and, for search_on_answer, that it scales logarithmically rather than linearly.
"""

from __future__ import annotations


def binary_search(nums: list[int], target: int) -> int:
    """Classic binary search on a sorted array. O(log n) time, O(1) space."""
    raise NotImplementedError


def search_rotated(nums: list[int], target: int) -> int:
    """Search in a rotated sorted array. O(log n) time, O(1) space.

    The trick: at any midpoint, one half is always properly sorted — determine which half
    that is, then decide which side the target could be on from its sorted half alone.
    """
    raise NotImplementedError


def search_on_answer(low: int, high: int, feasible) -> int:
    """Binary search over the *answer space*, not an array.

    `feasible(x)` must be monotonic: once true for some x, true for all larger x (or the
    reverse — caller is responsible for orienting the predicate). Return the smallest x in
    [low, high] for which `feasible(x)` is True, or `high + 1` if none is.
    O(log(high - low)) calls to `feasible`, which is the actual expensive operation this
    pattern is designed to minimize.
    """
    raise NotImplementedError


def min_eating_speed(piles: list[int], h: int) -> int:
    """Koko eating bananas: smallest integer speed to finish all piles within h hours.

    A direct application of search_on_answer — the feasibility check is "can I finish at
    this speed," which is monotonic in speed.
    """
    raise NotImplementedError
