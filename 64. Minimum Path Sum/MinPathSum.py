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