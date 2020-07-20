"""
Remove all elements from a linked list of integers that have value val.
"""
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return
        curr = head
        prev = None
        while curr is not None:
            if curr.val == val:
                if prev is None:
                    head = head.next
                    curr = head
                    continue
                else:
                    prev.next = curr.next
                    curr = curr.next
                    continue
            prev = curr
            curr = curr.next
        return head
