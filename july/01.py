"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        lo, hi = 0, n
        while lo <= hi:
            mid = (lo + hi)//2
            if mid*(mid+1)//2 <= n:
                ans = mid
                lo = mid + 1
            else:
                hi = mid -1
        return ans

# concept used - Binary Search
