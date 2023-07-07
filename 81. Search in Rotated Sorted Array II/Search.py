from typing import List


class Solution:
    
    def existsInFirst(self, num: int, start: int, nums: List[int]) -> bool:
        return num >= nums[start]
    
    def isUnknownGroup(self, num: int, start: int, nums: List[int]) -> bool:
        return num == nums[start]
    
    
    # O(n) time,
    # O(1) space,
    # Approach: binary search, 
    def search(self, nums: List[int], target: int) -> bool:
        
        lo, hi = 0, len(nums)-1
        
        while lo <= hi:
            mid = (lo+hi)//2
            mid_group = 1 if self.existsInFirst(nums[mid], lo, nums) else 2
            target_group = 1 if self.existsInFirst(target, lo, nums) else 2
            if nums[mid] == target:
                return True
            elif self.isUnknownGroup(nums[mid], lo, nums):
                lo += 1
            elif mid_group != target_group:
                if mid_group == 1:
                    lo = mid+1
                else:
                    hi = mid-1
            else:
                if nums[mid] > target:
                    hi = mid-1
                else:
                    lo = mid+1
                    
        return False