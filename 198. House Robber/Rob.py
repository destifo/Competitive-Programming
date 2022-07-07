'''
https://leetcode.com/problems/house-robber/
'''

class Solution:
    # did it 5 mins
    def rob(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[n - 1] = nums[n - 1]
        dp[n - 2] = max(dp[n - 1], nums[n - 2])
        
        for i in range(n - 3, -1, -1):
            currVal = dp[i + 2] + nums[i]
            dp[i] = max(currVal, dp[i + 1])

        return dp[0]

    
    # done in some other day
    def rob2(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0 for i in range(n)]
        if n == 1:  return nums[0]
        
        for i in range(n-1, -1, -1):
            if i > n - 3:
                dp[i] = nums[i]
            elif i == n - 3:
                dp[i] = nums[i] + nums[i+2]
            else:
                dp[i] = nums[i] + max(dp[i+2], dp[i+3])
            
            
        return max(dp[0], dp[1])
