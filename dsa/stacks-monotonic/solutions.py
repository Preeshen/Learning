"""Stack and monotonic-stack patterns."""

from __future__ import annotations


def is_valid_parentheses(s: str) -> bool:
    """O(n) time, O(n) space. A stack of open brackets; close brackets must match the top."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


def daily_temperatures(temps: list[int]) -> list[int]:
    """For each day, how many days until a warmer temperature (0 if none).

    O(n) time, O(n) space. A monotonic (decreasing) stack of indices: whenever the current
    temperature is warmer than the stack's top, that's the answer for every index still on the
    stack that's cooler — pop and record, rather than rescanning forward from each day.
    """
    result = [0] * len(temps)
    stack: list[int] = []  # indices, temps strictly decreasing bottom to top
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            prev = stack.pop()
            result[prev] = i - prev
        stack.append(i)
    return result


def largest_rectangle_in_histogram(heights: list[int]) -> int:
    """O(n) time, O(n) space, via a monotonic (non-decreasing) stack of (index, height)."""
    stack: list[tuple[int, int]] = []
    max_area = 0
    for i, h in enumerate(heights + [0]):
        start = i
        while stack and stack[-1][1] >= h:
            idx, height = stack.pop()
            start = idx
            max_area = max(max_area, height * (i - idx))
        stack.append((start, h))
    return max_area
