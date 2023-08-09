from typing import List


class Solution:
    
    def isValidDiff(self, diff: int, p: int, nums: List[int]) -> bool:
        pairs = 0
        
        skip = False
        for i in range(len(nums)-1):
            if skip:
                skip = False
                continue
            if nums[i+1]-nums[i] <= diff:
                pairs += 1
                skip = True
            if pairs >= p:
                return True
        
        return False
    
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: binary search, 
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        lo, hi = 0, nums[-1]-nums[0]
        ans = hi
        
        while lo <= hi:
            mid = (lo+hi)//2
            if self.isValidDiff(mid, p, nums):
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
                
        return ans