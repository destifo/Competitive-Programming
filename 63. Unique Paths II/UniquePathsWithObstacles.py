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