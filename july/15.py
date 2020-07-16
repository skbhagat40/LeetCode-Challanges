"""
Given an input string, reverse the string word by word.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')[::-1]
        res = ''
        for idx, word in enumerate(words):
            if word and not word.isspace():
                res += word
                res += ' '
        return res[:-1]
        
