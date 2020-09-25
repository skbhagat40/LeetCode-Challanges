from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1 = Counter(s)
        c2 = Counter(t)
        for k2, v2 in c2.items():
            v1 = c1.get(k2, 0)
            if v1 != v2:
                return k2
