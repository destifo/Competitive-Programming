from typing import List


class Solution:
    
    # O(n^2) time,
    # O(n) space,
    # Approach: bottom-up dp, 
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        count = [1 for _ in range(len(nums))]
        
        max_len = 1
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    if dp[j]+1 > dp[i]:
                        count[i] = 0
                    dp[i] = max(dp[i], dp[j]+1)
                    max_len = max(max_len, dp[i])
                
                    if dp[i] == dp[j]+1:
                        count[i] += count[j]
                    
        ans = 0
        for i in range(len(nums)):
            if dp[i] == max_len:
                ans += count[i]
        
        return ans