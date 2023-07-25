from typing import List


class Solution:
    
    # O(logn) time,
    # O(1) space, 
    # Approach: binary search, 
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 1, len(arr)-2
        
        while lo <= hi:
            mid = (lo+hi)//2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] > arr[mid]:
                hi = mid-1
            else:
                lo = mid+1
                
        return -1