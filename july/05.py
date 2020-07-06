"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s1 = "{0:b}".format(x)
        s2 = "{0:b}".format(y)
        if len(s1) < len(s2):
            s1 = "0"*(len(s2)-len(s1)) + s1
        if len(s2) < len(s1):
            s2 = "0"*(len(s1)-len(s2)) + s2
        d = 0
        for x,y in zip(s1,s2):
            if x != y:
                d += 1
        return d
