"""Arrays & hashing, including prefix sums."""

from __future__ import annotations


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """O(n) time, O(n) space. A hash map turns 'has this complement been seen' into O(1)."""
    seen: dict[int, int] = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return seen[complement], i
        seen[n] = i
    return None


def two_sum_naive(nums: list[int], target: int) -> tuple[int, int] | None:
    """O(n^2) time, O(1) space. The baseline two_sum benefits are measured against."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return None


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """O(n * k log k) time where k = max string length. Hash by sorted-character signature."""
    groups: dict[tuple, list[str]] = {}
    for s in strs:
        key = tuple(sorted(s))
        groups.setdefault(key, []).append(s)
    return list(groups.values())


def longest_consecutive_sequence(nums: list[int]) -> int:
    """O(n) time, O(n) space. A hash set lets each run be counted only from its true start."""
    num_set = set(nums)
    longest = 0
    for n in num_set:
        if n - 1 not in num_set:  # only start counting from the beginning of a run
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest


def prefix_sum_subarray_count(nums: list[int], target: int) -> int:
    """Count subarrays summing to `target`. O(n) time, O(n) space.

    prefix[j] - prefix[i] == target means the subarray (i, j] sums to target — so for each
    running prefix sum, count how many earlier prefix sums equal (current - target).
    """
    counts: dict[int, int] = {0: 1}
    running_sum = 0
    total = 0
    for n in nums:
        running_sum += n
        total += counts.get(running_sum - target, 0)
        counts[running_sum] = counts.get(running_sum, 0) + 1
    return total
