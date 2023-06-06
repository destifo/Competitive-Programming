from typing import List


class Solution:
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: heap, sorting, greedy, 
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        
        capital_to_profits = [(capital[i], profits[i]) for i in range(len(profits))]
        capital_to_profits.sort(reverse=True)
        
        heap = []
        for _ in range(k):
            while capital_to_profits and capital_to_profits[-1][0] <= w:
                heapq.heappush(heap, -capital_to_profits.pop()[1])
                
            if not heap:
                break
                
            max_val = -heapq.heappop(heap)
            w += max_val
            
        return w