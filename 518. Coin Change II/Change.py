from typing import List


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