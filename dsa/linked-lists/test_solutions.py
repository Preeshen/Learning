import importlib.util
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "linked_lists_solutions", Path(__file__).resolve().parent / "solutions.py"
)
solutions = importlib.util.module_from_spec(_SPEC)
sys.modules["linked_lists_solutions"] = solutions
_SPEC.loader.exec_module(solutions)

build_list = solutions.build_list
to_list = solutions.to_list
reverse_list = solutions.reverse_list
has_cycle = solutions.has_cycle
detect_cycle_start = solutions.detect_cycle_start
merge_k_sorted_lists = solutions.merge_k_sorted_lists


def test_reverse_list():
    head = build_list([1, 2, 3, 4, 5])
    reversed_head = reverse_list(head)
    assert to_list(reversed_head) == [5, 4, 3, 2, 1]


def test_reverse_empty_list():
    assert reverse_list(None) is None


def test_has_cycle_false():
    head = build_list([1, 2, 3])
    assert not has_cycle(head)


def test_has_cycle_true():
    head = build_list([1, 2, 3])
    head.next.next.next = head.next  # cycle back into the list
    assert has_cycle(head)


def test_detect_cycle_start():
    head = build_list([1, 2, 3, 4])
    cycle_entry = head.next  # node with val=2
    head.next.next.next.next = cycle_entry
    assert detect_cycle_start(head) is cycle_entry


def test_detect_cycle_start_none_when_no_cycle():
    head = build_list([1, 2, 3])
    assert detect_cycle_start(head) is None


def test_merge_k_sorted_lists():
    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    merged = merge_k_sorted_lists(lists)
    assert to_list(merged) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_merge_k_sorted_lists_with_empty_lists():
    lists = [None, build_list([1, 2]), None]
    merged = merge_k_sorted_lists(lists)
    assert to_list(merged) == [1, 2]
