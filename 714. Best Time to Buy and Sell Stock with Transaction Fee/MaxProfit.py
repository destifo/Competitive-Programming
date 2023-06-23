from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: bottom up dp, 
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        dp = [[0, 0] for _ in range(len(prices))]
        dp[-1] = [0, prices[-1]-fee]
        
        for i in range(len(prices)-2, -1, -1):
            dp[i][0] = max(dp[i+1][0], dp[i+1][1]-prices[i])
            dp[i][1] = max(dp[i+1][1], dp[i+1][0]+prices[i]-fee)
            
        return dp[0][0]