'''
https://leetcode.com/problems/jump-game/
'''


from typing import List


class Solution:
    # O(n^2) time, 
    # O(n) space, 
    # Approach: Dynamic programming,
    # just made it past the test, needs optimization
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        dp = [False for i in range(n-1)]
        if nums[n-2] > 0:
            dp[n-2] = True
        
        for i in range(n-3, -1, -1):
            if (i + nums[i] >= n-1):
                dp[i] = True
                continue
            for j in range(1, nums[i]+1):
                if dp[i+j]:
                    dp[i] = True
                    break
        
        return dp[0]