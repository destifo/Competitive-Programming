from typing import List


class Solution:
    
    
    # O(n^2 * m) time,
    # O(1) space,
    # Approach: matrix, bottom up dp
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        for row in range(len(grid)-2, -1, -1):
            for col in range(len(grid[0])-1, -1, -1):
                min_choice = float('inf')
                next_row = row + 1
                curr_val = grid[row][col]
                for next_row_col in range(len(grid[0])):
                    min_choice = min(min_choice, grid[next_row][next_row_col] + moveCost[curr_val][next_row_col])
                    
                grid[row][col] += min_choice
                
        return min(grid[0])