from typing import Dict, Tuple


class Solution:
    # O(n*target) time,
    # O(n*target) space,
    # Approach: dp top-down, memoization
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        MOD = (10**9)+7
            
        def findCombinations(depth: int, rem: int) -> int: 
            if depth == n:
                if rem == 0:   return 1
                return 0
            
            if rem <= 0:
                return 0
            
            if (depth, rem) in memo:
                return memo[(depth, rem)]
            
            combinations = 0
            for i in range(1, k+1):
                combinations += findCombinations(depth+1, rem-i)
            
            memo[(depth, rem)] = (combinations%MOD)
            return memo[(depth, rem)]
        
        return findCombinations(0, target)
    
    
    def findRolls(self, n: int, k: int, rem: int, memo: Dict[Tuple[int], int]) -> int:
        
        if rem == 0 and n == 0:
            return 1
        
        if n == 0 or rem <= 0:
            return 0
        
        state = (n, rem)
        if state in memo:
            return memo[state]
        
        ways = 0
        for i in range(1, k+1):
            ways += self.findRolls(n-1, k, rem-i, memo)
        
        memo[state] = ways
        return ways
    
    
    # O(n*target*k) time,
    # O(n*target*k) space,
    # Approach: dp, top down
    def numRollsToTarget2(self, n: int, k: int, target: int) -> int:
        
        MOD = 10**9 + 7
        return self.findRolls(n, k, target, {}) % MOD