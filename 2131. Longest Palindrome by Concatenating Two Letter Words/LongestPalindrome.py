from collections import defaultdict
from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: hash table, string, greedy
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        memo = defaultdict(int)
        pali_words = {}
        for word in words:
            rev = word[::-1]
            if memo[rev] > 0:
                ans += 4
                memo[rev] -= 1
                if rev == word:
                    pali_words[word] -= 1
                    if pali_words[word] == 0:  pali_words.pop(word)
                continue
            elif rev == word:
                pali_words[word] = pali_words.get(word, 0) + 1
            memo[word] += 1
        
        ans += 2 if len(pali_words) > 0 else 0
        return ans