'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

from typing import List


class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        curr_max = prices[n-1]
        max_profit = 0

        for i in range(n-2, -1, -1):
            curr_price = prices[i]
            max_profit = max(max_profit, curr_max - curr_price)
            curr_max = max(curr_max, curr_price)

        return max_profit


    # O(n) time,
    # O(n) space,
    # Approach: dp, memoization, recursion
    def maxProfit2(self, prices: List[int]) -> int:
        memo = {}
        
        def transaction(index: int, buying: bool) -> int:
            
            if index == len(prices):
                return 0
            
            if (index, buying) in memo:
                return memo[(index, buying)]
            
            if buying:
                buy = transaction(index+1, not buying) - prices[index]
                not_buy = transaction(index+1, buying)
                
                profit = max(buy, not_buy)
            else:
                sold = prices[index]
                not_sold = transaction(index+1, buying)
                
                profit = max(sold, not_sold)
                
            memo[(index, buying)] = profit
            return profit
        
        return transaction(0, buying=True)