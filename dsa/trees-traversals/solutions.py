"""Tree traversals and BST-property problems."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


def inorder(root: TreeNode | None) -> list[int]:
    """Left, node, right. O(n) time, O(h) space (recursion stack, h = height)."""
    raise NotImplementedError


def preorder(root: TreeNode | None) -> list[int]:
    """Node, left, right. O(n) time, O(h) space."""
    raise NotImplementedError


def postorder(root: TreeNode | None) -> list[int]:
    """Left, right, node. O(n) time, O(h) space."""
    raise NotImplementedError


def is_valid_bst(root: TreeNode | None) -> bool:
    """O(n) time, O(h) space.

    A BST is valid iff its in-order traversal is strictly increasing — checking each node
    against a (low, high) bound passed down from its ancestors is the O(n) way to verify this
    without materializing the full traversal.
    """
    raise NotImplementedError


def max_depth(root: TreeNode | None) -> int:
    """O(n) time, O(h) space."""
    raise NotImplementedError


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """O(n) time, O(h) space. Works for a general binary tree, not just a BST.

    If p and q are in different subtrees of the current node, the current node is the LCA —
    neither recursive call alone can "see" both, so the split point is where they converge.
    """
    raise NotImplementedError
