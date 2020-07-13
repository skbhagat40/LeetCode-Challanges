"""
Reverse bits of a given 32 bits unsigned integer.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        b = "{0:b}".format(n)
        b = "0"*(32-len(b)) + b
        return int(b[::-1],2)
        
