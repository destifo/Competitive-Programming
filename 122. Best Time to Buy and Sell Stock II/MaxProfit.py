'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''


from typing import List


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: dp, recursion, memoization
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def findMaxProfit(index: int, buying: bool) -> int:
            if index >= len(prices):
                return 0
            
            if (index, buying) in dp:
                return dp[(index, buying)]
            
            if buying:
                profit = findMaxProfit(index+1, False) - prices[index]
            else:
                profit = findMaxProfit(index+1, True) + prices[index]
                
            skipped_profit = findMaxProfit(index+1, buying)
            
            dp[(index, buying)] = max(profit, skipped_profit)
            return max(profit, skipped_profit)
        
        return findMaxProfit(0, True)