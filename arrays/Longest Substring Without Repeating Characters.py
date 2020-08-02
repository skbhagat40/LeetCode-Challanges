"""
Given a string, find the length of the longest substring without repeating characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        i, j = 0, 0
        ans = 0
        while j < len(s):
            if s[j] not in char_set:
                char_set.add(s[j])
                j += 1
            else:
                ans = max(ans, j-i)
                while i < j:
                    char_set.remove(s[i])
                    if s[i] == s[j]:
                        i += 1
                        break
                    i += 1
        if j == len(s):
            ans = max(ans, j-i)
        return ans
"""
Solution Approach - Sliding Window
"""
