"""Stack and monotonic-stack patterns."""

from __future__ import annotations


def is_valid_parentheses(s: str) -> bool:
    """O(n) time, O(n) space. A stack of open brackets; close brackets must match the top."""
    raise NotImplementedError


def daily_temperatures(temps: list[int]) -> list[int]:
    """For each day, how many days until a warmer temperature (0 if none).

    O(n) time, O(n) space. A monotonic (decreasing) stack of indices: whenever the current
    temperature is warmer than the stack's top, that's the answer for every index still on the
    stack that's cooler — pop and record, rather than rescanning forward from each day.
    """
    raise NotImplementedError


def largest_rectangle_in_histogram(heights: list[int]) -> int:
    """O(n) time, O(n) space, via a monotonic (non-decreasing) stack of (index, height)."""
    raise NotImplementedError
