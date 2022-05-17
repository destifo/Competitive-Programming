'''
https://leetcode.com/problems/shift-2d-grid/
'''

class Solution:
    def shiftGrid(self, grid, k: int):
        def shift():
            m = len(grid)
            n = len(grid[0])
            lastElement = grid[m-1][n-1]

            for row in range(m - 1, -1, -1):
                for col in range(n - 1, -1, -1):
                    grid[row][col] = grid[row-1][n-1] if col == 0 else grid[row][col-1]

            grid[0][0] = lastElement

        for i in range(k):
            shift()

        return grid