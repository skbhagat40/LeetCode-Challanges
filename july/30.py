"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if len(s) == 1:
            return [s] if s in wordDict else []
        d = set(wordDict)
        if any(map(lambda x: x not in set("".join(d)), set(s))): # when there is one char in s which not present in any word in d.
            return []
        res = set()
        seen = set()
        def helper(l,r, wordlist):
            if (l,r,tuple(wordlist)) in seen:
                return
            else:
                seen.add((l,r,tuple(wordlist)))
            nonlocal res
            if l >= len(s):
                if len("".join(wordlist)) == len(s):
                    res.add(tuple(wordlist))
                return
            if r >= len(s) + 1:
                if len("".join(wordlist)) == len(s):
                    res.add(tuple(wordlist))
                return
            if s[l:r] in d:
                wl = wordlist[:]
                wl.append(s[l:r])
                helper(r,r+1,wl)
                helper(l,r+1,wordlist)
            helper(l,r+1,wordlist)
        helper(0,0,[])
        return [" ".join(el) for el in res]
"""
Solution Approach - DP with memoization. element of choice - if a word is in dictionary, we can either include it in our answer, or look for future words.
"""
