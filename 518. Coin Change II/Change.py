from typing import Dict, List, Tuple


class Solution:
    
    def findNumberOfWays(self, index: int, amount: int, coins: List[int], memo) -> int:
        if amount == 0:
            return 1
        
        if index == len(coins):
            return 0
        
        if (index, amount) in memo:
            return memo[(index, amount)]
        
        ways = 0
        curr_take = 0
        while curr_take <= amount:
            ways += self.findNumberOfWays(index+1, amount-curr_take, coins, memo)
            curr_take += coins[index]
            
        memo[(index, amount)] = ways
        return ways
    
    
    # O(amount*len(coins)) time,
    # O(amount*len(coins)) space,
    # Approach: top down dp, memoization
    def change(self, amount: int, coins: List[int]) -> int:
        
        return self.findNumberOfWays(0, amount, coins, {})
    
    
    def countWays(self, index: int, rem: int, coins: List[int], memo: Dict[Tuple[int], int]) -> int:
        if rem == 0:
            return 1
        
        if rem < 0 or index == len(coins):
            return 0
        
        state = (index, rem)
        if state in memo:
            return memo[state]
        
        ways = self.countWays(index, rem-coins[index], coins, memo)
        ways += self.countWays(index+1, rem, coins, memo)
        
        memo[state] = ways
        return ways
    
    
    # O(len(coins)*amount) time,
    # O(len(coins)*amount) space,
    # Approach: dp, combinatorics, 
    def change(self, amount: int, coins: List[int]) -> int:
        
        return self.countWays(0, amount, coins, {})
    
    
    # O(len(coins)*amount) time,
    # O(len(coins)*amount) space,
    # Approach: bottom up dp, combinatorics, 
    def change2(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(n)] for _ in range(amount+1)]
        
        for i in range(n):
            dp[0][i] = 1
            
        for rem in range(1, amount+1):
            for j in range(n-1, -1, -1):
                coin = coins[j]
                if rem >= coin:
                    dp[rem][j] += dp[rem-coin][j]
                if j < n-1:
                    dp[rem][j] += dp[rem][j+1]

        return dp[amount][0]