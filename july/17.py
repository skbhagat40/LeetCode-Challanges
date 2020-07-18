"""
Given a non-empty array of integers, return the k most frequent elements.
"""

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return sorted(c.keys(), key = lambda x: c[x], reverse=True)[:k]
