'''
https://leetcode.com/problems/substring-with-concatenation-of-all-words/
'''


from collections import Counter
from typing import List


class Solution:
    # O(n^2) time, n len of all words combined in word(the anlaysis is not precise)
    # O(n^2) space,
    # Approach: Sliding window, hashmap
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def convertToSubstr(word, interval):
            l, r = 0, interval
            n = len(word)
            substrs = []
            
            while r <= n:
                substrs.append(word[l:r])
                l += interval
                r += interval
            
            # print(substrs)
            # print
            return substrs
        
        
        n = len(words)
        m = len(s)
        words_set = Counter(words)
        words_len = len(words[0])
        l, r = 0, (n * words_len)
        # print(r)
        
        ans = []
        while r <= m:
            word = s[l:r]
            substr_lst = convertToSubstr(word, words_len)
            if Counter(substr_lst) == words_set:
                ans.append(l)
            l +=1
            r +=1
                
        return ans