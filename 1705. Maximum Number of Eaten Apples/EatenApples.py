import heapq
from typing import List


class Solution:
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: heap, greedy, 
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        
        eaten = 0
        for i in range(len(apples)):
            if apples[i] != 0:
                heapq.heappush(heap, (i+days[i], apples[i]))
                
            while heap and heap[0][0] <= i:
                heapq.heappop(heap)
            
            if heap:
                eaten += 1
                heap[0] = (heap[0][0], heap[0][1]-1)
            
            if heap and heap[0][1] == 0:
                heapq.heappop(heap)
        
        time = len(apples)
        while heap:
            rot_day, appls = heapq.heappop(heap)
            avail_days = rot_day-time
            if avail_days <= 0:
                continue
            
            curr_eaten = min(avail_days, appls)
            eaten += curr_eaten
            time += curr_eaten
        
        return eaten
            