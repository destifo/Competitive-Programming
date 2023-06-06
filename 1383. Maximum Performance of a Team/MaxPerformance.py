'''
https://leetcode.com/problems/maximum-performance-of-a-team/
'''


import heapq
from typing import List


class Solution:
    # O(nlogn) time,
    # O(n) space,
    # Approach: heap, sorting
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # we create a array of tuples, (efficiency[i], speed[i])
        engineers = [(efficiency[i], speed[i]) for i in range(n)]
        # we will sort the our array in descending order of the engineers efficiency
        engineers.sort(reverse=True)
        
        # we create variables to hold the max performance, and tot speed when we iterate through our engineers array
        # we will also have a min heap to store our min speed during our iteration, 
        # poping the next min speed will be possible that way
        max_perf = 0
        min_heap = []
        tot_speed = 0
        
        for engineer in engineers:
            eng_speed = engineer[1]
            min_eff = engineer[0]
            
            # we add our current
            heapq.heappush(min_heap, eng_speed)
            tot_speed += eng_speed
            
            # if tot engnrs are more than k, we pop the slowest engineer
            if len(min_heap) > k:
                tot_speed -=heapq.heappop(min_heap)
            
            # we calculate the max perf we can get from this round of engineers
            curr_max = tot_speed * min_eff
            # update our max perf, 
            max_perf = max(max_perf, curr_max)
            
        MOD = 10**9 + 7
        return max_perf % MOD