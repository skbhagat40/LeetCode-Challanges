"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        # do bfs and reverse alternatively
        levels = [[root.val]]
        current_level = deque([root])
        next_level = deque()
        while current_level:
            node = current_level.popleft()
            # print(node)
            if node:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
                if not current_level:
                    if next_level:
                        levels.append([el.val for el in next_level])
                        current_level = next_level
                        next_level = deque()
        for idx,el in enumerate(levels):
            if idx % 2 == 1:
                levels[idx] = el[::-1]
        return levels
        
