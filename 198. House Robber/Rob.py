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
