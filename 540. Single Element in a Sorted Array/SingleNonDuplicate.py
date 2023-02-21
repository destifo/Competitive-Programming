from typing import List


class Solution:
    
    def countAfterIndex(self, index: int, nums: List[int]) -> int:
        
        if index > 0 and nums[index] == nums[index-1]:
            index -= 1

        return len(nums) - index
    
    
    # O(logn) time,
    # O(1) space,
    # Approach: binary search, 
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        
        while lo <= hi:
            mid = (lo+hi)//2
            count = self.countAfterIndex(mid, nums)
            
            if (mid == 0 or (mid > 0 and nums[mid-1] != nums[mid])) and (mid == len(nums)-1 or (mid < len(nums)-1 and nums[mid] != nums[mid+1])):
                return nums[mid]
            elif count % 2 == 1:
                lo = mid+1
            else:
                hi = mid-1
                
        return nums[0]