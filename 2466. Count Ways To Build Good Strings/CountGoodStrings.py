from typing import Dict


class Solution:
    
    def count(self, used: int, lo: int, hi: int, one: int, zero: int, memo: Dict[int, int]) -> int:
        
        if used >= hi:
            return 0 if used > hi else 1
        
        if used in memo:
            return memo[used]
        
        count = 1 if used >= lo else 0
        add_zeroes = self.count(used+zero, lo, hi, one, zero, memo)
        add_ones = self.count(used+one, lo, hi, one, zero, memo)
        
        memo[used] = add_zeroes + add_ones + count
        MOD = 10**9 + 7
        memo[used] %= MOD
        return memo[used]
    
    
    # O(n) time,
    # O(n) space,
    # Approach: top down dp, 
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        return self.count(0, low, high, one, zero, {})

    
    # O(n) time,
    # O(n) space,
    # Approach: bottom-up dp, tabulation
    def countGoodStrings2(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0 for _ in range(high+1)]
        for i in range(low, high+1):
            dp[i] = 1
            
        for i in range(high-1, -1, -1):
            if i + zero <= high:
                dp[i] += dp[i+zero]
                
            if i + one <= high:
                dp[i] += dp[i+one]
                
            dp[i] %= MOD
                
        return dp[0]