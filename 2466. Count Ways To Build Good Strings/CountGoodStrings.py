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