'''
https://leetcode.com/problems/minimum-path-sum/
'''


from typing import List


class Solution:
    # O(n*m) time,
    # O(n*m) space,
    # Approach: dp, matrix, hashtable
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        
        def findMin(x:int, y:int) -> int:
            n = len(grid)
            m = len(grid[0])
            key = (x, y)
            
            if key in memo.keys():
                return memo[key]
            
            if x >= n or y >= m:
                return float('inf')
            if x == n-1 and y == m-1:
                return grid[x][y]
            
            down_move = findMin(x, y+1)
            right_move = findMin(x+1, y)
            
            memo[key] = grid[x][y] + min(down_move, right_move)
            return memo[key]
        
        return findMin(0, 0)
    

    def inBound(self, coord, grid):
        row, col = coord
        
        return row < len(grid) and col < len(grid[0])
    
    
    # O(m*n) time,
    # O(m*n) space,
    # Approach: bottom-up dp, tabulation, 
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[-1][-1] = grid[-1][-1]
        
        for row in range(len(grid)-1, -1, -1):
            for col in range(len(grid[0])-1, -1, -1):
                if dp[row][col] != -1:
                    continue
                
                right_val = float('inf')
                if self.inBound((row, col+1), grid):
                    right_val = dp[row][col+1]
                    
                bottom_val = float('inf')
                if self.inBound((row+1, col), grid):
                    bottom_val = dp[row+1][col]
                    
                dp[row][col] = grid[row][col] + min(right_val, bottom_val)
                
        return dp[0][0]