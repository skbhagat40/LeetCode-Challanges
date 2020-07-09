"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""

from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if len(set(nums)) == 1 and nums[0] == 0 and len(nums) > 3:
            
        if len(nums) < 3:
            return []
        s = Counter(nums)
        ans = set()
        for idx, el in enumerate(nums):
            # s = -el
            if el==0:
                if s[el] > 2:
                    ans.add((0, 0, 0))
                continue
            for n in nums[idx+1:]:
                if -(n+el) in s:
                    if -(n+el) == n or -(n+el) == el:
                        if s[-(n+el)] > 1:
                            if len(set([el, n, -(n+el)])) == 2:
                                ans.add(tuple(sorted((el,n,-(n+el)))))
                            else:
                                if s[n] > 2 or s[el] > 2:
                                    ans.add(tuple(sorted((el,n,-(n+el)))))
                    else:
                        ans.add(tuple(sorted((el,n,-(n+el)))))
        return list(ans)
