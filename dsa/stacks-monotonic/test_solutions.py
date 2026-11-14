import importlib.util
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "stacks_monotonic_solutions", Path(__file__).resolve().parent / "solutions.py"
)
solutions = importlib.util.module_from_spec(_SPEC)
sys.modules["stacks_monotonic_solutions"] = solutions
_SPEC.loader.exec_module(solutions)

is_valid_parentheses = solutions.is_valid_parentheses
daily_temperatures = solutions.daily_temperatures
largest_rectangle_in_histogram = solutions.largest_rectangle_in_histogram


def test_valid_parentheses_true():
    assert is_valid_parentheses("()[]{}")


def test_valid_parentheses_false_mismatched():
    assert not is_valid_parentheses("(]")


def test_valid_parentheses_false_unclosed():
    assert not is_valid_parentheses("(()")


def test_daily_temperatures():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_daily_temperatures_no_warmer_day():
    assert daily_temperatures([30, 20, 10]) == [0, 0, 0]


def test_largest_rectangle_in_histogram():
    assert largest_rectangle_in_histogram([2, 1, 5, 6, 2, 3]) == 10


def test_largest_rectangle_single_bar():
    assert largest_rectangle_in_histogram([5]) == 5
