"""
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.
"""
from collections import defaultdict
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        m = defaultdict(list)
        ans = 0
        def traverse(root, depth, position):
            if root is not None:
                nonlocal m
                nonlocal ans
                m[depth].append(position)
                ans = max(ans, max(m[depth]) - min(m[depth]) + 1)
                traverse(root.left, depth + 1, 2*position + 1)
                traverse(root.right, depth + 1, 2*position + 2)
        traverse(root, 0, 0)
        return ans
 """
 Approach - do pre-order traversal, keep track of node positions
 """
