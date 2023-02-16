from typing import List


class Solution:
    
    def findMaxSum(self, index: int, nums: List[int]) -> int:
        if index >= len(nums):
            return 0
        
        next_sum = self.findMaxSum(index+1, nums)
        self.max_sum = max(self.max_sum, next_sum + nums[index], nums[index])
        if next_sum < 0:
            return nums[index]
        
        return next_sum + nums[index]
    
    
    # O(n) time,
    # O(n) space,
    # Approach: divide and conquer,
    def maxSubArray(self, nums: List[int]) -> int:
        self.max_sum = float('-inf')
        temp = self.findMaxSum(0, nums)
        
        return max(self.max_sum, temp)