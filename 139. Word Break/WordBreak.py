from typing import List


class Solution:
    
    # O(n*m) time, n --> len(s), m --> len(wordDict)
    # O(n) time,
    # Approach: bottom up dp, string, 
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[-1] = True
        
        '''
        
        dp = [f, f, f, f, T]
        
        '''
        
        for i in range(len(s)-1, -1, -1):
            size = len(s)-i
            for word in wordDict:
                if size >= len(word):
                    if word == s[i:i+len(word)]:
                        dp[i] = dp[i] or dp[i+len(word)]
        return dp[0]