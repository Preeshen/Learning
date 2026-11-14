import importlib.util
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "sliding_window_solutions", Path(__file__).resolve().parent / "solutions.py"
)
solutions = importlib.util.module_from_spec(_SPEC)
sys.modules["sliding_window_solutions"] = solutions
_SPEC.loader.exec_module(solutions)

longest_substring_without_repeating = solutions.longest_substring_without_repeating
min_window_substring = solutions.min_window_substring
max_sum_subarray_of_size_k = solutions.max_sum_subarray_of_size_k


def test_longest_substring_without_repeating():
    assert longest_substring_without_repeating("abcabcbb") == 3


def test_longest_substring_without_repeating_all_unique():
    assert longest_substring_without_repeating("abcdef") == 6


def test_longest_substring_without_repeating_empty():
    assert longest_substring_without_repeating("") == 0


def test_min_window_substring():
    assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC"


def test_min_window_substring_no_valid_window():
    assert min_window_substring("A", "AA") == ""


def test_max_sum_subarray_of_size_k():
    assert max_sum_subarray_of_size_k([2, 1, 5, 1, 3, 2], 3) == 9


def test_max_sum_subarray_too_short():
    assert max_sum_subarray_of_size_k([1, 2], 3) == 0
