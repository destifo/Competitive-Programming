from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: dp, hashtable
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        
        ans = 1
        for num in arr:
            dp[num] = dp.get(num-difference, 0) + 1
            ans = max(ans, dp[num])
            
        return ans