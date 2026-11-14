"""Sliding-window techniques."""

from __future__ import annotations


def longest_substring_without_repeating(s: str) -> int:
    """O(n) time, O(min(n, alphabet)) space.

    Grow the window by advancing the right edge; when a repeat is found, shrink from the left
    until the repeat is gone — never re-scan from scratch.
    """
    raise NotImplementedError


def min_window_substring(s: str, t: str) -> str:
    """Smallest substring of s containing all characters of t (with multiplicity).

    O(n + m) time, O(m) space. Expand right until the window is valid, then shrink left as far
    as possible while staying valid, recording the best window seen.
    """
    raise NotImplementedError


def max_sum_subarray_of_size_k(nums: list[int], k: int) -> int:
    """O(n) time, O(1) space. Slide a fixed-size window, adding one and dropping one each step."""
    raise NotImplementedError
