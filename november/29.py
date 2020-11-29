"""
Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window

Example - 

Input: nums = [9,11], k = 2
Output: [11]
"""

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # deque based approach
        # nlogn solution
        if len(nums) == 1:
            return nums
        if k == 1:
            return nums
        res = []
        q = deque()
        for i in range(len(nums)):
            val = nums[i]
            if i == 0:
                q.append(i)
                continue
            # trim the queue
            while len(q) and q[0] <= i - k:
                q.popleft()
            if val < nums[q[-1]]:
                q.append(i)
            else:
                while True:
                    if val > nums[q[-1]]:
                        q.pop()
                        if len(q) == 0:
                            q.append(i)
                            break
                    else:
                        q.append(i)
                        break
            if i >= k-1:
                res.append(nums[q[0]])
        return res
        
"""
Solution Approach - Using deque, removing un-necessary entries. initial thought - use a heap. but finding where to delete in a heap takes O(n) complexity.
Use deque. whenever we exceed the window we popleft. While expanding the window - If it is greater, we remove the smaller ones. If it's smaller, we keep it for
future use.
"""
