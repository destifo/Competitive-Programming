from typing import Dict, List, Tuple


class Solution:
    
    def canReach(self, index: int, unit: int, stones: List[int], index_of: Dict[int, int], memo: Dict[Tuple[int], int]) -> bool:
        
        if index == len(stones)-1:
            return True
        
        nxt = stones[index] + unit
        if nxt not in index_of:
            return False
        
        state = (index, unit)
        if state in memo:
            return memo[state]
        
        nxt_index = index_of[nxt]
        memo[state] = self.canReach(nxt_index, unit+1, stones, index_of, memo) or self.canReach(nxt_index, unit, stones, index_of, memo) or (self.canReach(nxt_index, unit-1, stones, index_of, memo) if unit-1 > 0 else False)
        return memo[state]
    
    
    # O(n^2) time,
    # O(n^2) space,
    # Approach: top down dp, 
    def canCross(self, stones: List[int]) -> bool:
        index_of = {}
        for index, stone in enumerate(stones):
            index_of[stone] = index
        return self.canReach(0, 1, stones, index_of, {})