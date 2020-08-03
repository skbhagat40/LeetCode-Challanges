"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(e for e in s if e.isalnum())
        return string.lower() == string[::-1].lower()
