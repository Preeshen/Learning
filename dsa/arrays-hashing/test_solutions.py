import importlib.util
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "arrays_hashing_solutions", Path(__file__).resolve().parent / "solutions.py"
)
solutions = importlib.util.module_from_spec(_SPEC)
sys.modules["arrays_hashing_solutions"] = solutions
_SPEC.loader.exec_module(solutions)

two_sum = solutions.two_sum
two_sum_naive = solutions.two_sum_naive
group_anagrams = solutions.group_anagrams
longest_consecutive_sequence = solutions.longest_consecutive_sequence
prefix_sum_subarray_count = solutions.prefix_sum_subarray_count


def test_two_sum_found():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)


def test_two_sum_not_found():
    assert two_sum([1, 2], 10) is None


def test_two_sum_naive_matches_two_sum():
    assert two_sum_naive([2, 7, 11, 15], 9) == (0, 1)


def test_group_anagrams():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    groups_as_sets = {frozenset(g) for g in result}
    assert frozenset(["eat", "tea", "ate"]) in groups_as_sets
    assert frozenset(["tan", "nat"]) in groups_as_sets
    assert frozenset(["bat"]) in groups_as_sets


def test_longest_consecutive_sequence():
    assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4


def test_longest_consecutive_sequence_empty():
    assert longest_consecutive_sequence([]) == 0


def test_prefix_sum_subarray_count():
    assert prefix_sum_subarray_count([1, 1, 1], 2) == 2


def test_prefix_sum_subarray_count_with_negatives():
    assert prefix_sum_subarray_count([1, -1, 0], 0) == 3
