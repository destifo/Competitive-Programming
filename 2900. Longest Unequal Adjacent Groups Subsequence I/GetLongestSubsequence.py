from typing import List


class Solution:
    
    # O(n^2) time,
    # O(n^2) space,
    # Approach: dp, 
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp = [[word] for word in words]
        
        longest_len = 0
        for i in range(len(words)-1, -1, -1):
            word1 = words[i]
            curr_longest_index = -1
            for j in range(i, len(words)):
                if groups[i] == groups[j]:
                    continue
                    
                if curr_longest_index == -1 or len(dp[j]) > len(dp[curr_longest_index]):
                    curr_longest_index = j
                    
            if curr_longest_index != -1 and len(dp[curr_longest_index]) >= len(dp[i]):
                dp[i] = [word1, *dp[curr_longest_index]]
        
            longest_len = max(longest_len, len(dp[i]))
            
        for seq in dp:
            if len(seq) == longest_len:
                return seq
            
        return []