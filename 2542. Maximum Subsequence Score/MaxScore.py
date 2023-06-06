import heapq
from typing import List


class Solution:
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: heap, sorting, 
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        combined_nums = []
        for i in range(len(nums1)):
            combined_nums.append((nums2[i], nums1[i]))
            
        combined_nums.sort(reverse=True)
        
        heap = []
        tot = 0
        max_score = float('-inf')
        for i in range(len(nums1)):
            curr_min, num1 = combined_nums[i]
            heapq.heappush(heap, num1)
            tot += num1
            
            if len(heap) == k:
                max_score = max(max_score, tot*curr_min)
                tot -= heapq.heappop(heap)
            
        return max_score