'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''


from typing import List


class Solution:
    # O(logn) time,
    # O(1) time, 
    # Approach: binary search,
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        def binarySearchMin(lo, hi) -> int:
            while lo <= hi:
                mid = (lo+hi)//2
                prev = (mid-1)%n
                nxt = (mid+1)%n
                
                if nums[mid] < nums[prev] and nums[mid] < nums[nxt]:
                    return nums[mid]
                elif nums[mid] > nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
                    
            return nums[lo]
                    
        return binarySearchMin(0, n-1)