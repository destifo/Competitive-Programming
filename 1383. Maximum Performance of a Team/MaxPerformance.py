'''
https://leetcode.com/problems/maximum-performance-of-a-team/
'''


import heapq
from typing import List


class Solution:
    # O(nlogn) time,
    # O(n) space,
    # Approach: heap, sorting,
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = [(efficiency[i], speed[i]) for i in range(n)]
        engineers.sort(reverse=True)
        
        max_perf = 0
        min_heap = []
        tot_speed = 0
        
        for engineer in engineers:
            eng_speed = engineer[1]
            min_eff = engineer[0]
            
            heapq.heappush(min_heap, eng_speed)
            tot_speed += eng_speed
            if len(min_heap) > k:
                tot_speed -=heapq.heappop(min_heap)
            
            max_perf = max(max_perf, (tot_speed * min_eff))
            
        MOD = 10**9 + 7
        return max_perf % MOD