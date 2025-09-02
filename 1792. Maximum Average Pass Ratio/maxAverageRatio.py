import heapq
from typing import List

class Solution:

    # O(mlogn) time, m -> extraStudents, n -> classes
    # O(n) space,
    # Approach: greedy, heap
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []

        for pas, tot in classes:
            curr_ratio = pas / tot
            inc_ratio = (pas+1) / (tot+1)
            ratio_change = inc_ratio - curr_ratio
            heapq.heappush(max_heap, (-ratio_change, pas, tot))

        
        for i in range(extraStudents):
            ratio, pas, tot = heapq.heappop(max_heap)
            new_ratio = (pas / tot) + (-ratio)
            inc_ratio = (pas+2) / (tot+2)
            ratio_change = inc_ratio - new_ratio
            heapq.heappush(max_heap, (-ratio_change, pas+1, tot+1))

        ans = 0
        for (_, pas, tot) in max_heap:
            ans += pas/tot

        return ans/len(classes)
