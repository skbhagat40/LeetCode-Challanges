"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
"""
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)+1):
            ans.extend(list(itertools.combinations(nums, r=i)))
        return ans
