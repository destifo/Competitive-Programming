'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''


from typing import List


class Solution:
    # O(logn) time,
    # O(1) space,
    # Approach: binary search,
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        pos = [-1, -1]
        if n == 0:  return pos
        
        def findFirstPos(start, end) -> int:
            mid = (start + end)//2
            num = nums[mid]
            
            if num == target and (mid == 0 or nums[mid-1] != target):
                return mid
            elif start >= end-1:
                if nums[end] == target:
                    return end
                return -1
            elif num < target:
                return findFirstPos(mid, end)
            else:
                return findFirstPos(start, mid)
            
        
        def findLastPos(start, end) -> int:
            mid = (start + end)//2
            num = nums[mid]
            
            if num == target and (mid == len(nums)-1 or nums[mid+1] != target):
                return mid
            elif start >= end-1:
                if nums[end] == target:
                    return end
                return -1
            elif num > target:
                return findLastPos(start, mid)
            else:
                return findLastPos(mid, end)
            
        pos[0] = findFirstPos(0, n-1)
        pos[1] = findLastPos(pos[0], n-1)
        
        return pos