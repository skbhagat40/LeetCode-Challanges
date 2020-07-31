"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1: 1, 2: 2}
        def helper(n):
            res = cache.get(n, None)
            if res:
                return res
            else:
                cache[n] = helper(n-1) + helper(n-2)
                return cache[n]
        return helper(n)
"""
Solution Approach - Dynamic programming (recursion with memoization)
"""
