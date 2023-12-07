from typing import List


class Solution:
    
    def flipRow(self, row: int, grid: List[List[int]]) -> None:
        for col in range(len(grid[0])):
            grid[row][col] = 1 if grid[row][col] == 0 else 0
    
    
    def flipCol(self, col: int, grid: List[List[int]]) -> None:
        for row in range(len(grid)):
            grid[row][col] = 1 if grid[row][col] == 0 else 0
    
    
    def calcSum(self, grid: List[List[int]]) -> int:
        
        tot = 0
        for row in grid:
            num_str = "".join([str(bit) for bit in row])
            num = int(num_str, 2)
            tot += num
            
        return tot
    
    
    # O(n*m) time,
    # O(1) space,
    # Approach: counting, greedy
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        for row in range(rows):
            if grid[row][0] == 0:
                self.flipRow(row, grid)
        
        half_row = rows//2
        for col in range(1, cols):
            zero_count = 0
            for row in range(rows):
                if grid[row][col] == 0:
                    zero_count += 1
                    
            if zero_count > half_row:
                self.flipCol(col, grid)

        return self.calcSum(grid)