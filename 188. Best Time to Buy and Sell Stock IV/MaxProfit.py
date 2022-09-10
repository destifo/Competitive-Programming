from typing import List


class Solution:
    # O(n) time,
    # O(n*k) space,
    # Approach: dp, memoization
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = {}
        
        def findMaxProfit(index: int, buying: bool, tx: int) -> int:
            
            if tx == k or index >= len(prices): return 0
            
            if (index, buying, tx) in dp:
                return dp[(index, buying, tx)]
            
            profit = 0
            if buying:
                profit = findMaxProfit(index+1, False, tx) - prices[index]
                
            else:
                profit = findMaxProfit(index+1, True, tx+1) + prices[index]
                
            skiped_profit = findMaxProfit(index+1, buying, tx)
            
            dp[(index, buying, tx)] = max(profit, skiped_profit)
            return dp[(index, buying, tx)]
        
        return findMaxProfit(0, True, 0)   