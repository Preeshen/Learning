import importlib.util
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "trees_traversals_solutions", Path(__file__).resolve().parent / "solutions.py"
)
solutions = importlib.util.module_from_spec(_SPEC)
sys.modules["trees_traversals_solutions"] = solutions
_SPEC.loader.exec_module(solutions)

TreeNode = solutions.TreeNode
inorder = solutions.inorder
preorder = solutions.preorder
postorder = solutions.postorder
is_valid_bst = solutions.is_valid_bst
max_depth = solutions.max_depth
lowest_common_ancestor = solutions.lowest_common_ancestor


def make_bst() -> TreeNode:
    #        5
    #      /   \
    #     3     8
    #    / \   / \
    #   1   4 7   9
    n1, n4, n7, n9 = TreeNode(1), TreeNode(4), TreeNode(7), TreeNode(9)
    n3 = TreeNode(3, n1, n4)
    n8 = TreeNode(8, n7, n9)
    root = TreeNode(5, n3, n8)
    return root


def test_inorder_is_sorted_for_valid_bst():
    root = make_bst()
    assert inorder(root) == [1, 3, 4, 5, 7, 8, 9]


def test_preorder():
    root = make_bst()
    assert preorder(root) == [5, 3, 1, 4, 8, 7, 9]


def test_postorder():
    root = make_bst()
    assert postorder(root) == [1, 4, 3, 7, 9, 8, 5]


def test_is_valid_bst_true():
    assert is_valid_bst(make_bst())


def test_is_valid_bst_false_subtle_violation():
    # right child of a left subtree violates the ancestor bound, not just the local parent
    root = TreeNode(5, TreeNode(3, None, TreeNode(6)), TreeNode(8))
    assert not is_valid_bst(root)


def test_max_depth():
    assert max_depth(make_bst()) == 3


def test_max_depth_empty():
    assert max_depth(None) == 0


def test_lowest_common_ancestor():
    root = make_bst()
    n1 = root.left.left
    n4 = root.left.right
    assert lowest_common_ancestor(root, n1, n4) is root.left


def test_lowest_common_ancestor_different_subtrees():
    root = make_bst()
    n1 = root.left.left
    n7 = root.right.left
    assert lowest_common_ancestor(root, n1, n7) is root
