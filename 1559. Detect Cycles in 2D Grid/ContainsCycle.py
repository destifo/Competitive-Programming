from typing import List, Tuple


class Solution:
    
    def inBound(self, row: int, col: int, grid: List[List[int]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        if row < 0 or row >= ROWS:
            return False
        
        if col < 0 or col >= COLS:
            return False
        
        return True
    
    
    def getNeighbors(self, row: int, col: int, grid: List[List[int]]) -> List[Tuple[int]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        nbrs = []
        
        for x, y in directions:
            new_row, new_col = row+x, col+y
            if self.inBound(new_row, new_col, grid) and grid[row][col] == grid[new_row][new_col]:
                nbrs.append((new_row, new_col))
                
        return nbrs
    
    
    def hasCycle(self, row: int, col: int, parent: Tuple[int], grid: List[List[int]], color: List[List[int]]) -> bool:
        
        if color[row][col] == 1:
            return True
        
        if color[row][col] == 2:
            return False
        
        color[row][col] = 1
        for nbr in self.getNeighbors(row, col, grid):
            if nbr == parent:
                continue
            nbr_row, nbr_col = nbr
            if self.hasCycle(nbr_row, nbr_col, (row, col), grid, color):
                return True
        
        color[row][col] = 2
        return False
    
    
    # O(n*m) time,
    # O(n*m) space,
    # Approach: dfs coloring, 
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        color = [[0 for _ in range(m)] for _ in range(n)]
        
        for row in range(n):
            for col in range(m):
                if color[row][col]:
                    continue
                if self.hasCycle(row, col, (-1, -1), grid, color):
                    return True
                
        return False