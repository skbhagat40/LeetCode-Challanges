"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        in_map = {val:idx for idx,val in enumerate(inorder)}
        post_map = {val:idx for idx,val in enumerate(postorder)}
        
        def bt(in_l, in_r, post_l, post_r):
            if in_r < in_l or post_r < post_l:
                return
            r = TreeNode(postorder[post_r])
            partition_idx = in_map[postorder[post_r]]
            l_count = abs(in_l - partition_idx)
            post_r_l_b = post_l + l_count - 1
            r_count = abs(partition_idx - in_r)
            if l_count > 0:
                r.left = bt(in_l, partition_idx-1, post_l, post_r_l_b )
            if r_count > 0:
                r.right = bt(partition_idx+1, in_r, post_r_l_b + 1, post_r-1)
            return r
        return bt(0, len(inorder)-1, 0, len(postorder)-1)
