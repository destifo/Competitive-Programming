from typing import List


class Solution:
    # O(n^3) time, TLE
    # O(n^2) space,
    # Approach: dp, memoizaiton
    def maxProfit(self, prices: List[int]) -> int:
        
        def findMaxProfit(index: int) -> int:
            n = len(prices)

            if index in memo.keys():
                return memo[index]
            
            if index >= n-1:
                return 0
            
            max_profit = 0
            for i in range(index+1, n):
                curr_profit = prices[i] - prices[index]
                if curr_profit <= 0:    continue

                if i >= n-2:
                    max_profit = max(max_profit, curr_profit)
                    
                for j in range(i+2, n):
                    max_profit = max(max_profit, findMaxProfit(j) + curr_profit)

            memo[index] = max_profit    
            return max_profit
        
        ans = 0
        for i in range(len(prices)):
            memo = {}
            ans = max(ans, findMaxProfit(i))
            
        return ans


    # O(n) time,
    # O(n) space,
    # Approach: dp, memoization
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}
        
        def findProfit(index: int, buying) -> int:
            
            if index >= n:
                return 0
            
            if (index, buying) in dp.keys():
                return dp[(index, buying)]
                
            if buying:
                profit = findProfit(index+1, False) - prices[index]
            else:
                profit = findProfit(index+2, True) + prices[index]

            skipIndexProfit = findProfit(index+1, buying)
            max_profit = max(profit, skipIndexProfit)
            dp[(index, buying)] = max_profit

            return dp[(index, buying)]
           
        return findProfit(0, True)


sol = Solution()
print(sol.maxProfit([1,3,5,4,3,7,6,9,2,4]
))
# [6,1,6,4,3,0,2]