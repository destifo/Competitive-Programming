from collections import defaultdict
from typing import Dict, List, Tuple


class Solution:
    
    def findNumWays(self, index: int, buffet: Dict[str, int], target_index: int, target: str, memo: Dict[Tuple[int], int]) -> int:
        
        if target_index == len(target):
            return 1
        
        if index == len(buffet):
            return 0
        
        state = (index, target_index)
        if state in memo:
            return memo[state]
        
        ways = self.findNumWays(index+1, buffet, target_index, target, memo)
        if buffet[index][target[target_index]] > 0:
            ways += buffet[index][target[target_index]]*(self.findNumWays(index+1, buffet, target_index+1, target, memo))
        
        MOD = (10**9) + 7
        ways %= MOD
        memo[state] = ways
        return ways
    
    
    # O(len(target)*len(word[i])) time,
    # O(len(target)*len(word[i])) space,
    # Approach: top down dp, string
    def numWays(self, words: List[str], target: str) -> int:
        words_buffet = []
        
        for i in range(len(words[0])):
            cnt = defaultdict(int)
            for word in words:
                cnt[word[i]] += 1
            words_buffet.append(cnt)
        
        MOD = (10**9) + 7
        return self.findNumWays(0, words_buffet, 0, target, {}) % MOD
    

    # O(len(target)*len(word[i])) time,
    # O(len(target)*len(word[i])) space,
    # Approach: bottom up dp, string, tabulation
    def numWays2(self, words: List[str], target: str) -> int:
        words_buffet = []
        
        for i in range(len(words[0])):
            cnt = defaultdict(int)
            for word in words:
                cnt[word[i]] += 1
            words_buffet.append(cnt)
        
        MOD = (10**9) + 7
        dp = [[0 for _ in range(len(target)+1)] for _ in range(len(words[0])+1)]
        
        for row in range(len(words[0])):
            dp[row][len(target)-1] = words_buffet[row][target[-1]]
        
        for row in range(len(words[0])-1, -1, -1):
            for col in range(len(target)-1, -1, -1):
                if words_buffet[row][target[col]] > 0:
                    dp[row][col] += (words_buffet[row][target[col]] * dp[row+1][col+1])
                        
                dp[row][col] += dp[row+1][col]
                dp[row][col] %= MOD
        
        return dp[0][0]