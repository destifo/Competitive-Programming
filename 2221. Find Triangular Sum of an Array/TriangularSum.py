'''
https://leetcode.com/problems/find-triangular-sum-of-an-array/
'''


from typing import List


class Solution:
    # O(n/2 * (n + 1)) time and space, 
    # Approach: Top down dp
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [[1 for i in range(n-j)] for j in range(n)]
        
        ans[0] = nums
        
        for i in range(1, n):
            for j in range(n-i):
                ans[i][j] = ans[i-1][j] + ans[i-1][j+1] % 10
                
        return ans[n-1][0] % 10