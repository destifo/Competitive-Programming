from collections import defaultdict
from typing import List


class Solution:
    
    # O(m*n) time,
    # O(m*n) space,
    # Approach: counting
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ones_row = defaultdict(int)
        ones_col = defaultdict(int)
        zeroes_row = defaultdict(int)
        zeroes_col = defaultdict(int)
        
        ROWS, COLS = len(grid), len(grid[0])
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    zeroes_row[row] += 1
                    zeroes_col[col] += 1
                else:
                    ones_row[row] += 1
                    ones_col[col] += 1
        
        diff = [ [0 for _ in range(COLS)] for _ in range(ROWS) ]
        for row in range(ROWS):
            for col in range(COLS):
                diff[row][col] = ones_row[row] + ones_col[col] - zeroes_row[row] - zeroes_col[col]
                
        return diff