'''
https://leetcode.com/problems/kth-largest-element-in-an-array/
'''


import heapq
from typing import List


class Solution:
    # straight forward soln, but have to do it the other way around
    def findKthLargest(self, nums: list[int], k: int):
        nums.sort()
        return nums[-k]

    
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_heap = []
        
        for i in range(n):
            heapq.heappush(max_heap, -nums[i])
        
        result = None
        for i in range(k):
            result = -heapq.heappop(max_heap)
            
        return result


    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        pivot = nums[0]
        left = [num for num in nums if num < pivot]
        mid = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]
        
        if len(right) >= k:
            return self.findKthLargest(right, k)
        elif len(right) + len(mid) >= k:
            return mid[0]
        else:
            return self.findKthLargest(left, k-len(right)-len(mid))