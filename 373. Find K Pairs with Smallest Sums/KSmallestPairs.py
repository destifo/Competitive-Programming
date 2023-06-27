import heapq
from typing import List


class Solution:
    
    # O(klogn) time,
    # O(n) space,
    # Approach: heap, 
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(nums1)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
            
        pairs = []
        while k > 0 and heap:
            k -= 1
            _, index1, index2 = heapq.heappop(heap)
            
            pairs.append((nums1[index1], nums2[index2]))
            if index2 + 1 < len(nums2):
                next_sum = nums1[index1] + nums2[index2+1]
                heapq.heappush(heap, (next_sum, index1, index2+1))
        
        return pairs