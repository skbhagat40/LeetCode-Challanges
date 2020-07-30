"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        cache = {}
        if len(prices) == 2:
            return max(prices[1] - prices[0], 0)
        A = prices
        def helper(i):
            if i == 0:
                return 0
            if i < 0:
                return 0
            else:
                res = cache.get(i, None)
                if res:
                    return res
                else:
                    if i >= 1:
                        cache[i] = max([max(-(A[i-el] - A[i]) +  helper(i-el-2), helper(i-el)) for el in range(1, i+1)])
                    else:
                        return 0
                    return cache[i]
        res = max(helper(len(prices)-1), 0)
        return res
"""
Solution Approach - Dynamic Programming. (Explore all possiblities).
"""
