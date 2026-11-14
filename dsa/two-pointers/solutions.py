"""Two-pointer techniques."""

from __future__ import annotations


def two_sum_sorted(nums: list[int], target: int) -> tuple[int, int] | None:
    """nums is sorted. O(n) time, O(1) space — replaces an O(n^2) pair search."""
    raise NotImplementedError


def is_palindrome(s: str) -> bool:
    """O(n) time, O(1) space. Compare from both ends inward, skipping non-alphanumerics."""
    raise NotImplementedError


def max_area_container(heights: list[int]) -> int:
    """Container With Most Water. O(n) time, O(1) space.

    Moving the shorter wall's pointer inward is always correct: the area is bounded by the
    shorter wall, so keeping it fixed and moving the taller wall can only ever shrink the width
    without any chance of increasing the limiting height.
    """
    raise NotImplementedError


def three_sum(nums: list[int]) -> list[tuple[int, int, int]]:
    """All unique triplets summing to 0. O(n^2) time, O(1) extra space (beyond sorting).

    Sort first, fix the smallest element, then two-pointer the rest — turns an O(n^3) brute
    force into O(n^2).
    """
    raise NotImplementedError
