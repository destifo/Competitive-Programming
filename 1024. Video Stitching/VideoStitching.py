import heapq
from typing import List


class Solution:
    
    def addToHeap(self, time: int, clips: List[int], heap: List[int]) -> None:
        
        while clips and clips[-1][0] <= time:
            start, end = clips.pop()
            heapq.heappush(heap, -end)
    

    # O(nlogn) time,
    # O(n) space,
    # Approach: sorting, heap, greedy, heap + sorting
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(reverse=True)
        heap = []
        ans = 0
        
        t = 0
        while t < time:
            self.addToHeap(t, clips, heap)
            if not heap or -heap[0] <= t:    return -1
            
            curr_end = -heapq.heappop(heap)
            t = curr_end
            ans += 1
            
        return ans