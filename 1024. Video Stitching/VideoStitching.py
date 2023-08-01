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
    
    
    # O(n^2) time,
    # O(n) space,
    # Approach: bottom up dp, sorting
    def videoStitching2(self, clips: List[List[int]], time: int) -> int:
        dp = [float('inf') for _ in range(time+1)]
        dp[0] = 0
        
        clips.sort()
        for clip in clips:
            start, end = clip
            for t in range(start, end+1):
                if t > time:
                    break
                dp[t] = min(dp[t], dp[start]+1)
                
        return dp[time] if dp[time] != float('inf') else -1