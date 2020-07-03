"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
"""
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        levels = deque([[root.val]])
        current_level = deque([root])
        next_level = deque()
        while current_level:
            current_node = current_level.popleft()
            if current_node is not None:
                if current_node.left is not None:
                    next_level.append(current_node.left)
                if current_node.right is not None:
                    next_level.append(current_node.right)
                if not current_level:
                    if next_level:
                        levels.appendleft([el.val for el in next_level if el is not None])
                        current_level = next_level
                        next_level = deque()
        return levels
