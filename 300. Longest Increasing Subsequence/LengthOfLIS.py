from typing import List


class Solution:
    
    # O(n^2) time,
    # O(n) space,
    # Approach: bottom up dp, 
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        ans = 1
        
        for i in range(n-2, -1, -1):
            longest = 0
            for j in range(i, n):
                if nums[j] > nums[i]:
                    longest = max(longest, dp[j])
            dp[i] += longest
            ans = max(ans, dp[i])
            
        return ans
    
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: binary search, 
    def lengthOfLIS2(self, nums: List[int]) -> int:
        n = len(nums)
        seq = [float('inf') for _ in range(n)]
        ans = 0
        
        for num in nums:
            left, right = 0, ans
            while left <= right:
                mid = (left+right)//2
                if seq[mid] < num:
                    left += 1
                else:
                    right -= 1
            seq[left] = num
            if left == ans:
                ans += 1

        return ans