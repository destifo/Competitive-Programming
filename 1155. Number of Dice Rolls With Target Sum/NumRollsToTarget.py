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