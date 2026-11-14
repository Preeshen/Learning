"""Arrays & hashing, including prefix sums."""

from __future__ import annotations


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """O(n) time, O(n) space. A hash map turns 'has this complement been seen' into O(1)."""
    raise NotImplementedError


def two_sum_naive(nums: list[int], target: int) -> tuple[int, int] | None:
    """O(n^2) time, O(1) space. The baseline two_sum benefits are measured against."""
    raise NotImplementedError


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """O(n * k log k) time where k = max string length. Hash by sorted-character signature."""
    raise NotImplementedError


def longest_consecutive_sequence(nums: list[int]) -> int:
    """O(n) time, O(n) space. A hash set lets each run be counted only from its true start."""
    raise NotImplementedError


def prefix_sum_subarray_count(nums: list[int], target: int) -> int:
    """Count subarrays summing to `target`. O(n) time, O(n) space.

    prefix[j] - prefix[i] == target means the subarray (i, j] sums to target — so for each
    running prefix sum, count how many earlier prefix sums equal (current - target).
    """
    raise NotImplementedError
