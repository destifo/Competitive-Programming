from typing import List


class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: array, simulation, 
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        start = 0
        end = 0
        tot = 0
        
        for time in timeSeries:
            if end < time:
                tot += (end-start)
                start = time
                end = start + duration
            else:
                end = time + duration
        
        tot += (end-start)
        
        return tot