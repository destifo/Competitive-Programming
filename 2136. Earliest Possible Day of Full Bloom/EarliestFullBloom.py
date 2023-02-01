from typing import List


class Solution:
    
    # O(nlog) time,
    # O(n) space,
    # Approach: greedy, 
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        curr_time = 0
        earliest = 0
        plant_growth_time = [ (growTime[i], plantTime[i]) for i in range(len(plantTime)) ]
        
        plant_growth_time.sort(reverse=True)

        for growth_time, plant_time in plant_growth_time:
            curr_time += plant_time
            earliest = max(earliest, curr_time+growth_time)
            
        return earliest