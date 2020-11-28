"""
Longest Substring with atleast K repeating characters.

Problem Description - 
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k

Example - 
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

The problem with two pointer based approach - whenever we encounter a new character (e.g. 'b' ), we have 2 options, either move right hoping we might find more (k-1) 'b' , or we move the left pointer.
The approach we are taking here is to exhaust all possiblities. We iterate over all possible no. of unique characters i.e. (1 .. to .. 26) let's call it T.
For each T , we run the following sliding window algo - 
1. if moreEqK <= T, we move to right. We keep track of freq. of characters in the window. If freq == k, we do Found += 1. If the freq. of a char is 0, we do moreEqK += 1.
2. if moreEqK > T, we shift the left pointer. If the feq of char at left pointer >= k, we do Found -= 1
3. We check for the condition and update the ans. ans = max(ans, j-i). condition - Found == len(list(freq.filter(lambda x: x >0))) . basically all the elements in the freq array
which have non-zero value are == k.
"""
from collections import Counter, defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for u_w_c in range(1, 27):
            i, j = 0, 0
            moreEqK = 0
            arr = [0]*27
            Found = 0
            while j < len(s) and i < len(s) and i <= j:
                if j >= len(s):
                    break
                if moreEqK <= u_w_c:
                    # handle case 1. shift towards right.
                    if arr[ord(s[j]) - ord('a')] == 0:
                        moreEqK += 1
                    arr[ord(s[j]) - ord('a')] += 1
                    if arr[ord(s[j]) - ord('a')] == k:
                        Found += 1
                    j += 1
                else:
                    # handle case 2. shift towards left. shift the window
                    if arr[ord(s[i]) - ord('a')]  == k:
                        Found -= 1
                    arr[ord(s[i]) - ord('a')] -= 1
                    if arr[ord(s[i]) - ord('a')] == 0:
                        moreEqK -= 1
                    i += 1
                if Found == len(list(filter(lambda x: x>0, arr))):
                    ans = max(ans, j-i)
                
        return ans
                    
