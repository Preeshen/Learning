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
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def preorder(root: TreeNode | None) -> list[int]:
    """Node, left, right. O(n) time, O(h) space."""
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def postorder(root: TreeNode | None) -> list[int]:
    """Left, right, node. O(n) time, O(h) space."""
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def is_valid_bst(root: TreeNode | None) -> bool:
    """O(n) time, O(h) space.

    A BST is valid iff its in-order traversal is strictly increasing — checking each node
    against a (low, high) bound passed down from its ancestors is the O(n) way to verify this
    without materializing the full traversal.
    """
    def check(node: TreeNode | None, low: float, high: float) -> bool:
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return check(node.left, low, node.val) and check(node.right, node.val, high)

    return check(root, float("-inf"), float("inf"))


def max_depth(root: TreeNode | None) -> int:
    """O(n) time, O(h) space."""
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """O(n) time, O(h) space. Works for a general binary tree, not just a BST.

    If p and q are in different subtrees of the current node, the current node is the LCA —
    neither recursive call alone can "see" both, so the split point is where they converge.
    """
    if root is None or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right
