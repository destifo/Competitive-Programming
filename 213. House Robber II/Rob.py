'''
https://leetcode.com/problems/house-robber-ii/
'''

class Solution:
    # just consider doing both scenarios, one where 1st isn't considered and 2nd last one isn't
    def rob(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[n - 1] = nums[n - 1]
        dp[n - 2] = max(dp[n - 1], nums[n - 2])
        
        for i in range(n - 3, 0, -1):
            num = 0 if i == 0 else nums[i]
            currVal = dp[i + 2] + num
            dp[i] = max(currVal, dp[i + 1])
            

        dp1 = [0] * n
        dp1[n - 2] = 0
        dp1[n - 2] = max(dp1[n - 1], nums[n - 2])
        for i in range(n - 3, -1, -1):
            currVal = dp1[i + 2] + nums[i]
            dp1[i] = max(currVal, dp1[i + 1])

        return max(dp[0], dp1[0])


sol = Solution()
print(sol.rob([200,3,140,20,10]))