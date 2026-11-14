import importlib.util
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "binary_search_solutions", Path(__file__).resolve().parent / "solutions.py"
)
solutions = importlib.util.module_from_spec(_SPEC)
sys.modules["binary_search_solutions"] = solutions
_SPEC.loader.exec_module(solutions)

binary_search = solutions.binary_search
search_rotated = solutions.search_rotated
search_on_answer = solutions.search_on_answer
min_eating_speed = solutions.min_eating_speed


def test_binary_search_found():
    assert binary_search([1, 3, 5, 7, 9, 11], 7) == 3


def test_binary_search_not_found():
    assert binary_search([1, 3, 5, 7, 9, 11], 4) == -1


def test_binary_search_empty():
    assert binary_search([], 1) == -1


def test_search_rotated_found_left_half():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 5) == 1


def test_search_rotated_found_right_half():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 1) == 5


def test_search_rotated_not_found():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_search_on_answer_finds_threshold():
    assert search_on_answer(0, 20, lambda x: x >= 7) == 7


def test_min_eating_speed():
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30


def test_search_on_answer_scales_logarithmically_not_linearly():
    calls = {"count": 0}

    def feasible(x: int) -> bool:
        calls["count"] += 1
        return x >= 999_999

    search_on_answer(0, 2_000_000, feasible)
    assert calls["count"] < 30
