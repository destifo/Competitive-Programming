from typing import List


class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: greedy, sliding window
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        l, r = 0, 2
        
        while r < len(nums):
            if nums[r] + nums[r-1] > nums[l]:
                return nums[r] + nums[r-1] + nums[l]
            
            l +=1
            r +=1
            
        return 0