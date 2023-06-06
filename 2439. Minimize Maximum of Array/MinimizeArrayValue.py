import math
from typing import List


class Solution:
    
    def validMaximum(self, nums: List[int], maxm: int) -> bool:
        remaining = 0
        
        for i in range(len(nums)-1, 0, -1):
            if nums[i] <= maxm:
                remaining = max(0, remaining-(maxm-nums[i]))
                continue
                
            remaining += (nums[i]-maxm)
            
        return nums[0] + remaining <= maxm
            
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: binary search, 
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        lo, hi = 0, max(nums)
        ans = hi
        
        while lo <= hi:
            mid = (lo+hi)//2
            
            if self.validMaximum(nums, mid):
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
        
        return ans
    

    # O(n) time,
    # O(1) space,
    # Approach: greedy, prefix sum, 
    def minimizeArrayValue2(self, nums: List[int]) -> int:
        prev_tot = 0
        ans = -1
        
        for i, num in enumerate(nums):
            prev_tot += num
            
            ans = max(ans, math.ceil(prev_tot/(i+1)))
            
        return ans