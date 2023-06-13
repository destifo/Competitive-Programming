from collections import defaultdict
from typing import List


class Solution:
    
    # O(n^2) time,
    # O(n^2) space,
    # Approach: hash table, grid
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        row_hashes = defaultdict(int)
        
        for row in grid:
            row_hashes[tuple(row)] += 1

        for col in range(len(grid)):
            col_vals = []
            for row in range(len(grid)):
                col_vals.append(grid[row][col])
            
            col_tuple = tuple(col_vals)
            ans += row_hashes[col_tuple]
                
        return ans