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


    # O(nlogn) time,
    # O(1) space,
    # Approach: sorting, math, greedy
    def largestPerimeter2(self, nums: List[int]) -> int:
        nums.sort()
        
        nums_len = len(nums)
        
        for i in range(nums_len-1, 1, -1):
            if nums[i] < (nums[i-1] + nums[i-2]):
                return sum(nums[i-2:i+1])
            
        return 0