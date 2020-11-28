"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum %2 != 0:
            return False
        wt = total_sum // 2
        cache = {}
        def dp(idx, wt):
            if idx < 0:
                return False
            if wt < 0:
                return False
            if wt == 0:
                return True
            nonlocal cache
            ret = cache.get((idx, wt), None)
            if ret is not None:
                return ret
            ret = dp(idx-1, wt-nums[idx]) or dp(idx-1, wt)
            cache[(idx, wt)] = ret
            return ret
        return dp(len(nums)-1, wt)
        
"""
Solution approach - one dimensional dp problem, with weight constraint as total_sum // 2
"""
