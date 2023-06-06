'''
https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
'''


class Solution:
    # O(n) time
    # O(n) space
    def finalPrices(self, prices: list[int]) -> list[int]:
        n = len(prices)
        stack = []
        answer = prices.copy()
        
        for i in range(n):
            curr_price = prices[i]
            while stack and prices[stack[-1]] >= curr_price:
                answer[stack[-1]] = prices[stack[-1]] - curr_price
                stack.pop()
                
            stack.append(i)
            
        return answer