"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return
        self.ans = []
        def flatten(root):
            if root is not None:
                self.ans.append(root)
                if root.child is not None:
                    flatten(root.child)
                flatten(root.next)
        flatten(head)
        res = []
        for idx,el in enumerate(self.ans):
            el.child = None
            if idx == 0:
                el.next = None
                el.prev = None
                el.next = self.ans[idx+1]
            else:
                el.next = None
                el.prev = None
                if idx != len(self.ans)-1:
                    el.next = self.ans[idx + 1]
                    el.prev = self.ans[idx - 1]
                else:
                    el.prev = self.ans[idx-1]
                    el.next = None
        return self.ans[0]
 """
 Approach - Traverse the LL recursively, store them in a list and link them later.
 """
