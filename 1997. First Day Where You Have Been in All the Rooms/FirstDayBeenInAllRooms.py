from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: bottom-up dp, 
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0 for _ in range(n)]
        MOD = 10**9 + 7
        
        for i in range(1, n):
            dp[i] = dp[i-1] + 2
            dp[i] += (dp[i-1] - dp[nextVisit[i-1]])
            dp[i] %= MOD
        print(dp)    
        return dp[-1]