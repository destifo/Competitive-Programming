import heapq
from typing import List


class Solution:
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: heap
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        for i, (arr, leav) in enumerate(times):
            times[i] = [arr, leav, i]
        
        times.sort()
        waiting_leave = []
        next_chair = 0
        prev_used_chairs = []
        
        # print(times)
        for arr, leav, friend in times:
            while waiting_leave and waiting_leave[0][0] <= arr:
                _, chair = heapq.heappop(waiting_leave)
                heapq.heappush(prev_used_chairs, chair)
            
            # print(friend, arr, leav, prev_used_chairs, waiting_leave)
            curr_chair = next_chair
            if prev_used_chairs:
                curr_chair = heapq.heappop(prev_used_chairs)
            else:
                next_chair += 1
                
            if friend == targetFriend:
                return curr_chair
                
            heapq.heappush(waiting_leave, (leav, curr_chair))
        
        return -1
