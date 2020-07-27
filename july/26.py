"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
"""
from functools import reduce
class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        while len(str(res)) != 1:
            res = reduce(lambda x,y: int(x) + int(y), str(res))
        return res
        
