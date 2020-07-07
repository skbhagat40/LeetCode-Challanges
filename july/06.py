"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join([str(el) for el in digits]))
        return list(str(num+1))
        
