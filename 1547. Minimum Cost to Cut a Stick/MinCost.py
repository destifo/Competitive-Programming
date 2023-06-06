from typing import Dict, List, Tuple


class Solution:
    
    def cut(self, start: int, end: int, cuts: List[int], memo: Dict[Tuple[int], int]) -> int:
        
        if start >= end-1:
            return 0
        
        if (start, end) in memo:
            return memo[(start, end)]
        
        min_cost = float('inf')
        curr_len = cuts[end]-cuts[start]
        for i in range(start+1, end):
            curr_cost = self.cut(start, i, cuts, memo) + self.cut(i, end, cuts, memo) + curr_len
            min_cost = min(min_cost, curr_cost)
        
        memo[(start, end)] = min_cost
        return min_cost
            
    
    # O(len(cuts)^2) time,
    # O(len(cuts)^2) space,
    # Approach: top-down dp, memoization, 
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0, *cuts, n]
        cuts.sort()
        return self.cut(0, len(cuts)-1, cuts, {})