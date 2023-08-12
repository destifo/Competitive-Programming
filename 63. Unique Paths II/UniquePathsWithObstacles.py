from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        memo = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] or obstacleGrid[0][0]:
            return 0

        def calc_unique(a, b):
            if a == m - 1 and b == n - 1:
                return 1

            if a >= m or b >= n:
                return 0

            if obstacleGrid[a][b]:
                return 0

            if not memo.get((a + 1, b), None):
                memo[(a + 1, b)] = calc_unique(a+1, b)
            if not memo.get((a, b+1), None):
                memo[(a, b+1)] = calc_unique(a, b+1)
            
            return memo[(a+1, b)] + memo[(a, b+1)]
        
        return calc_unique(0, 0)
    
    
    # O(n*m) time,
    # O(n*m) space,
    # Approach: bottom up dp, 
    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[-1][-1] = 1
        if obstacleGrid[-1][-1] == 1:
            return 0
        
        for row in range(n-1, -1, -1):
            for col in range(m-1, -1, -1):
                if obstacleGrid[row][col] == 1:
                    continue
                if row+1 < n:
                    dp[row][col] += dp[row+1][col]
                if col+1 < m:
                    dp[row][col] += dp[row][col+1]
                    
        return dp[0][0]