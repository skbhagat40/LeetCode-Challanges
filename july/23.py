"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
"""
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return filter(lambda x: c[x]==1, c)

# without using extra space.
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for el in nums:
            res = res ^ el
        i = 0
        while not(res & 1<<i):
            i += 1
        xor1, xor2 = 0, 0
        for el in nums:
            if el & (1<<i):
                xor1 ^= el
            else:
                xor2 ^= el
        return [xor1, xor2]
        
