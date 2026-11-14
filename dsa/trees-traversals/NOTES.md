# Trees I — traversals & BST properties

**Problem it solves**: visiting every node of a tree in a defined order, and checking whether a
tree satisfies the BST invariant (left subtree < node < right subtree, recursively).

**Mechanism**: the three traversal orders differ only in when the node's own value is emitted
relative to its children — that's the entire difference between inorder/preorder/postorder.
Validating a BST by passing down a (low, high) bound as you recurse is what makes it O(n): the
alternative of just comparing each node to its immediate parent misses violations from a more
distant ancestor.

**Failure modes**: `test_is_valid_bst_false_subtle_violation` is the case that catches a wrong
implementation — a right child whose value is less than its grandparent's but still greater than
its immediate parent passes a "compare to parent only" check while violating the real BST
invariant. Only the ancestor-bound version catches it.

**Trade-offs**: inorder traversal of a valid BST is always sorted — that property is sometimes
*cheaper* to exploit directly (e.g., validate by checking the inorder list is strictly increasing)
than the bound-passing recursion, at the cost of O(n) extra space for the materialized list
instead of O(h) for the bound-passing version's recursion stack.
