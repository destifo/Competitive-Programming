import heapq
from typing import List


class Solution:
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: heap, two pointers, 
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        pool = []
        left, right = candidates-1, len(costs)-candidates
        if left >= right:
            left = len(costs)//2
            right = left + 1
        
        for i in range(left+1):
            heapq.heappush(pool, (costs[i], i))
            
        for i in range(right, len(costs)):
            heapq.heappush(pool, (costs[i], i))
        
        total_cost = 0
        while k > 0:
            cost, index = heapq.heappop(pool)
            total_cost += cost
            k -= 1
            
            if right-left > 1:
                if index > left:
                    right -= 1
                    heapq.heappush(pool, (costs[right], right))
                else:
                    left += 1
                    heapq.heappush(pool, (costs[left], left))
                    
        return total_cost