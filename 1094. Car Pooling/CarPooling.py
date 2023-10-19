from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: prefix sum, 
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        farthest_pos = max([trip[2] for trip in trips])
        ppl_at_time = [0 for _ in range(farthest_pos)]
        
        for num_p, From, to in trips:
            ppl_at_time[From] += num_p
            if to < farthest_pos:
                ppl_at_time[to] -= num_p
                
        for i in range(1, farthest_pos):
            ppl_at_time[i] += ppl_at_time[i-1]
            if ppl_at_time[i] > capacity:
                return False
            
        return ppl_at_time[0] <= capacity