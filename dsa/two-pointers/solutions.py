"""Two-pointer techniques."""

from __future__ import annotations


def two_sum_sorted(nums: list[int], target: int) -> tuple[int, int] | None:
    """nums is sorted. O(n) time, O(1) space — replaces an O(n^2) pair search."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        total = nums[lo] + nums[hi]
        if total == target:
            return lo, hi
        if total < target:
            lo += 1
        else:
            hi -= 1
    return None


def is_palindrome(s: str) -> bool:
    """O(n) time, O(1) space. Compare from both ends inward, skipping non-alphanumerics."""
    lo, hi = 0, len(s) - 1
    while lo < hi:
        while lo < hi and not s[lo].isalnum():
            lo += 1
        while lo < hi and not s[hi].isalnum():
            hi -= 1
        if s[lo].lower() != s[hi].lower():
            return False
        lo += 1
        hi -= 1
    return True


def max_area_container(heights: list[int]) -> int:
    """Container With Most Water. O(n) time, O(1) space.

    Moving the shorter wall's pointer inward is always correct: the area is bounded by the
    shorter wall, so keeping it fixed and moving the taller wall can only ever shrink the width
    without any chance of increasing the limiting height.
    """
    lo, hi = 0, len(heights) - 1
    best = 0
    while lo < hi:
        area = min(heights[lo], heights[hi]) * (hi - lo)
        best = max(best, area)
        if heights[lo] < heights[hi]:
            lo += 1
        else:
            hi -= 1
    return best


def three_sum(nums: list[int]) -> list[tuple[int, int, int]]:
    """All unique triplets summing to 0. O(n^2) time, O(1) extra space (beyond sorting).

    Sort first, fix the smallest element, then two-pointer the rest — turns an O(n^3) brute
    force into O(n^2).
    """
    nums = sorted(nums)
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicate "first" elements
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if total == 0:
                result.append((nums[i], nums[lo], nums[hi]))
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
            elif total < 0:
                lo += 1
            else:
                hi -= 1
    return result
