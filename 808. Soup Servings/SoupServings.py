from typing import Dict, Tuple


class Solution:
    
    def calcProb(self, a: int, b: int, memo: Dict[Tuple[int], int]) -> None:
        
        if a == 0 and b == 0:
            return 0.5
        
        if a == 0:
            return 1
            
        if b == 0:
            return 0
        
        state = (a, b)
        if state in memo:
            return memo[state]
        
        # the 4 operations,
        ops = [[100, 0], [75, 25], [50, 50], [25, 75]]
        prob = 0
        for x, y in ops:
            prob += (0.25) * self.calcProb(max(a-x, 0), max(b-y, 0), memo)
            
        memo[state] = prob
        return prob
        
    
    # O(n^2) time for n < 5000 else O(1)
    # O(n) space,
    # Approach: dp top down, math
    def soupServings(self, n: int) -> float:
        return self.calcProb(n, n, {}) if n < 5000 else 1