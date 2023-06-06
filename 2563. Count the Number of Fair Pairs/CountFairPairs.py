from typing import List


class Solution:
    
    def findValidSmallest(self, nums: List[int], target: int, start: int) -> int:
        
        lo, hi = start, len(nums)-1
        ans = len(nums)
        
        while lo <= hi:
            mid = (lo+hi)//2
            
            if nums[mid] >= target:
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
                
        return ans
    
    
    def findValidLargest(self, nums: List[int], target: int, start: int) -> int:
        
        lo, hi = start, len(nums)-1
        ans = start
        
        while lo <= hi:
            mid = (lo+hi)//2
            
            if nums[mid] <= target:
                ans = mid+1
                lo = mid+1
            else:
                hi = mid-1
                
        return ans
    
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: binary search, sorting, 
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        
        for index, num in enumerate(nums):
            count = self.findValidLargest(nums, upper-num, index+1) - self.findValidSmallest(nums, lower-num, index+1)
            ans += count
            
        return ans