from typing import Dict, List


class Solution:
    
    def smallStoneWeight(self, index, stones: List[int], memo: Dict[int, int]) -> int:
        
        if index == len(stones):
            return abs(sum(stones))
        
        state = (index, sum(stones[:index]))
        if state in memo:
            return memo[state]
        
        added = self.smallStoneWeight(index+1, stones, memo)
        
        stones[index] = -stones[index]
        minused = self.smallStoneWeight(index+1, stones, memo)
        stones[index] = -stones[index]
        
        memo[state] = min(added, minused)
        return min(added, minused)
                
    
    # O(n*max(stones)) time,
    # O(n*max(stones)) space,
    # Approach: dp, 
    def lastStoneWeightII(self, stones: List[int]) -> int:
        return self.smallStoneWeight(0, stones, {})