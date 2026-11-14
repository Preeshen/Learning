"""Sliding-window techniques."""

from __future__ import annotations


def longest_substring_without_repeating(s: str) -> int:
    """O(n) time, O(min(n, alphabet)) space.

    Grow the window by advancing the right edge; when a repeat is found, shrink from the left
    until the repeat is gone — never re-scan from scratch.
    """
    seen: dict[str, int] = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best


def min_window_substring(s: str, t: str) -> str:
    """Smallest substring of s containing all characters of t (with multiplicity).

    O(n + m) time, O(m) space. Expand right until the window is valid, then shrink left as far
    as possible while staying valid, recording the best window seen.
    """
    if not t or not s:
        return ""

    need: dict[str, int] = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    missing = len(t)

    left = 0
    best_left, best_right = 0, -1

    for right, ch in enumerate(s):
        if need.get(ch, 0) > 0:
            missing -= 1
        need[ch] = need.get(ch, 0) - 1

        while missing == 0:
            if best_right == -1 or (right - left) < (best_right - best_left):
                best_left, best_right = left, right
            need[s[left]] = need.get(s[left], 0) + 1
            if need[s[left]] > 0:
                missing += 1
            left += 1

    return s[best_left:best_right + 1] if best_right != -1 else ""


def max_sum_subarray_of_size_k(nums: list[int], k: int) -> int:
    """O(n) time, O(1) space. Slide a fixed-size window, adding one and dropping one each step."""
    if len(nums) < k:
        return 0
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        best = max(best, window_sum)
    return best
