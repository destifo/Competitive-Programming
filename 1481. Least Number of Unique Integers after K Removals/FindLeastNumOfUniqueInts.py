import heapq
from typing import Counter, List


class Solution:
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: heap, counting, hashmap
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        nums_count = Counter(arr)
        heap = []
        
        for num, freq in nums_count.items():
            heapq.heappush(heap, freq)
            
        while heap:
            curr_freq = heap[0]
            if curr_freq > k:
                break
            
            heapq.heappop(heap)
            k -= curr_freq
            
        return len(heap)