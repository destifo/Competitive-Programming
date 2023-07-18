from typing import Dict, List, Tuple


class Solution:
    
    def findMaxValue(self, index: int, day: int, selected: int, k: int, events: List[List[int]], memo: Dict[Tuple[int], int]) -> int:
        
        while index < len(events) and events[index][0] < day:
            index += 1
        
        if index == len(events) or selected == k:
            return 0
        
        state = (index, selected)
        if state in memo:
            return memo[state]
        
        start, end, val = events[index]
        take = val + self.findMaxValue(index+1, end+1, selected+1, k, events, memo)
        skip = self.findMaxValue(index+1, day, selected, k, events, memo)
        
        memo[state] = max(take, skip)
        return memo[state]
    
    
    # O(n*k) time,
    # O(n) space,
    # Approach: dp, 
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        
        return self.findMaxValue(0, 1, 0, k, events, {})