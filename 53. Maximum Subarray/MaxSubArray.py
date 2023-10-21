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
    
    
    # O(n) time,
    # O(1) space,
    # Approach: prefix sum, 
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        prev_smallest = 0
        tot = 0
        
        for num in nums:
            tot += num
            curr_best_sum = (tot-prev_smallest)
            ans = max(ans, curr_best_sum)
            prev_smallest = min(prev_smallest, tot)
            
        return ans