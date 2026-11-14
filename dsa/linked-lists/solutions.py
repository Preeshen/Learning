"""Linked-list fundamentals: reversal, fast-slow pointers, cycle detection, merge-k."""

from __future__ import annotations

import heapq
from dataclasses import dataclass


@dataclass
class ListNode:
    val: int
    next: "ListNode | None" = None


def build_list(values: list[int]) -> ListNode | None:
    head: ListNode | None = None
    tail: ListNode | None = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_list(head: ListNode | None) -> list[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def reverse_list(head: ListNode | None) -> ListNode | None:
    """O(n) time, O(1) space. Rewire each node's `next` to point backward as we walk forward."""
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def has_cycle(head: ListNode | None) -> bool:
    """Floyd's fast-slow pointer. O(n) time, O(1) space — no visited set needed."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def detect_cycle_start(head: ListNode | None) -> ListNode | None:
    """Find the node where a cycle begins, or None if there is no cycle.

    O(n) time, O(1) space. After the fast/slow pointers meet inside the cycle, restarting one
    pointer from head and advancing both at the same speed meets exactly at the cycle's start —
    a consequence of the distance algebra (not something to just memorize without deriving once).
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            pointer = head
            while pointer is not slow:
                pointer = pointer.next
                slow = slow.next
            return pointer
    return None


def merge_k_sorted_lists(lists: list[ListNode | None]) -> ListNode | None:
    """O(n log k) time, O(k) space, using a min-heap of (value, tiebreak, node)."""
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    tail = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
