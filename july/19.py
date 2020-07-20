"""
Given two binary strings, return their sum (also a binary string).
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return "{0:b}".format(int(a,2)+int(b,2))
        
