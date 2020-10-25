"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

"""
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # stack based solution !!
        stack = []
        s3 = None
        for i in range(len(nums)-1,-1,-1):
            el = nums[i]
            if i == len(nums)-1:
                stack.append(el)
                continue
            if s3 and len(stack) and el < s3:
                return True
            if el < stack[-1]:
                stack.append(el)
            else:
                while True:
                    if el > stack[-1]:
                        s3 = stack.pop()
                        if len(stack) == 0:
                            stack.append(el)
                            break
                    else:
                        stack.append(el)
                        break
        return False
"""
Intuition / Approach - whatever we pop from the stack becomes s3, s2 is the maximum here and each element is the candidate for s1. stack to keep track of all
greater elements, pop -> becomes s3, and each one is s1
"""
