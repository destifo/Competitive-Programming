'''
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
'''


from typing import List


class Solution:
    # O(m*n) time, 
    # O(m*n) space,
    # Approach: dp, tabulation
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        # max_len = 0
                
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    # max_len = max(max_len, dp[i][j])
                    
        return max(max(length) for length in dp)


sol = Solution()
print(sol.findLength([1,1,0,0,1]
,[1,1,0,0,0]))