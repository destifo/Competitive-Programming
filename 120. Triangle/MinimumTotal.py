'''
https://leetcode.com/problems/triangle/
'''


class Solution:
    # O(n2) space complexity, O(n * m) time complexity
    def minimumTotal(self, triangle: List[list]):
        n = len(triangle)
        dp = [[0 for j in range(n)] for i in range(n)]
        
        for i in range(n):
            dp[n-1][i] = triangle[n-1][i]
        
        for row in range(n-2, -1, -1):
            nums = triangle[row]
            for index, num in enumerate(nums):
                dp[row][index] = min(dp[row + 1][index], dp[row + 1][index + 1]) + num
                
        return dp[0][0]
            

    # # O(m*n) space complexity, O(n * m) time complexity
    def minimumTotal2(self, triangle: list):
        n = len(triangle)
        dp = []
        for i in range(n):
            lst = [0 for j in range(i + 1)]
            dp.append(lst)
        
        for i in range(n):
            dp[n-1][i] = triangle[n-1][i]
        
        for row in range(n-2, -1, -1):
            nums = triangle[row]
            for index, num in enumerate(nums):
                dp[row][index] = min(dp[row + 1][index], dp[row + 1][index + 1]) + num
                
        return dp[0][0]