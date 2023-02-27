import heapq
from typing import List


class Solution:
    
    # O(len(ranges)log(len(ranges))) time,
    # O(len(ranges)) space,
    # Approach: heap, greedy, 
    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = []
        for i, rng in enumerate(ranges):
            taps.append((i-rng, i+rng))
        taps.sort(reverse=True)
        
        curr_pos = 0
        max_heap = []
        taps_used = 0

        while taps and taps[-1][0] <= curr_pos:
            heapq.heappush(max_heap, -taps.pop()[1])
        
        while max_heap and curr_pos < n:
            furthest = -heapq.heappop(max_heap)
            curr_pos = furthest
            taps_used += 1
                
            while taps and taps[-1][0] <= curr_pos:
                heapq.heappush(max_heap, -taps.pop()[1])
            
        return taps_used if curr_pos >= n else -1