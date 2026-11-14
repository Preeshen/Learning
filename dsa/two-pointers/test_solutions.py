import importlib.util
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "two_pointers_solutions", Path(__file__).resolve().parent / "solutions.py"
)
solutions = importlib.util.module_from_spec(_SPEC)
sys.modules["two_pointers_solutions"] = solutions
_SPEC.loader.exec_module(solutions)

two_sum_sorted = solutions.two_sum_sorted
is_palindrome = solutions.is_palindrome
max_area_container = solutions.max_area_container
three_sum = solutions.three_sum


def test_two_sum_sorted_found():
    assert two_sum_sorted([1, 2, 3, 4, 6], 6) == (1, 3)


def test_two_sum_sorted_not_found():
    assert two_sum_sorted([1, 2, 3], 100) is None


def test_is_palindrome_true_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama")


def test_is_palindrome_false():
    assert not is_palindrome("race a car")


def test_max_area_container():
    assert max_area_container([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_three_sum_finds_all_unique_triplets():
    result = set(three_sum([-1, 0, 1, 2, -1, -4]))
    assert result == {(-1, -1, 2), (-1, 0, 1)}


def test_three_sum_no_triplets():
    assert three_sum([1, 2, 3]) == []
