"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def tr(r1, r2):
            if r1 is not None and r2 is not None:
                return (r1.val == r2.val and tr(r1.left, r2.left) and tr(r1.right, r2.right))
            else:
                if r1 is None and r2 is None:
                    return True
                return False       
        return tr(p, q)
       
"""
Solution Approach - Traverse both trees in pre-order manner. return True if their root are same.
"""
