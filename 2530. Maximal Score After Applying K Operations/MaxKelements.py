import heapq
import math
from typing import List


class Solution:
    
    # O(k) time,
    # O(n) space,
    # Approach: heap, 
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = []
        for i, num in enumerate(nums):
            heapq.heappush(max_heap, -num)
        
        score = 0
        while k > 0:
            k -=1
            num = -heapq.heappop(max_heap)
            score += num
            num = math.ceil(num/3)
            heapq.heappush(max_heap, -num)
            
        return score