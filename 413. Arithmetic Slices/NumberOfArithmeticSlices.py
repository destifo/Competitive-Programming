'''
https://leetcode.com/problems/arithmetic-slices/
'''


from typing import List


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: dp,
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dp = [0 for i in range(n)]
        
        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp[i] = dp[i-1]+1
                ans+= dp[i]
                
        return ans


    # O(n) time,
    # O(1) space,
    # Approach: dp,
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dp = 0
        
        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp = dp+1
                ans+= dp
            else:
                dp = 0
                
        return ans