'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

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