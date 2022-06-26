'''
https://leetcode.com/problems/kth-largest-element-in-an-array/
'''


import heapq


class Solution:
    # straight forward soln, but have to do it the other way around
    def findKthLargest(self, nums: list[int], k: int):
        nums.sort()
        return nums[-k]

    
    # using heap sort
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_heap = []
        
        for i in range(n):
            heapq.heappush(max_heap, -nums[i])
        
        result = None
        for i in range(k):
            result = -heapq.heappop(max_heap)
            
        return result