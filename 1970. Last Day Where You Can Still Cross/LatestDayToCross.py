from collections import deque
from typing import List, Tuple


class Solution:
    
    def inBound(self, row: int, col: int, grid: List[List[int]]) -> bool:
        
        if row < 0 or row >= len(grid):
            return False
        
        if col < 0 or col >= len(grid[0]):
            return False
        
        return True
    
    
    def getNeighbors(self, row: int, col: int, grid: List[List[int]]) -> List[Tuple[int]]:
        
        nbrs = []
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        for x, y in directions:
            nbr_row, nbr_col = row+x, col+y
            if self.inBound(nbr_row, nbr_col, grid) and grid[nbr_row][nbr_col] == 0:
                nbrs.append((nbr_row, nbr_col))
                
        return nbrs
    
    
    def isCrossable(self, n: int, m: int, index: int, cells: List[List[int]]) -> bool:
        grid = [[0 for _ in range(m)] for _ in range(n)]
        queue = deque()
        visited = set()
        for r, c in cells[:index+1]:
            grid[r-1][c-1] = 1
            
        for col in range(m):
            if grid[0][col] == 0:   queue.append((0, col))
        
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                row, col = queue.popleft()
                if row == len(grid)-1:  return True
                for nbr_row, nbr_col in self.getNeighbors(row, col, grid):
                    queue.append((nbr_row, nbr_col))
                    grid[nbr_row][nbr_col] = 1
                    
        return False
        
    
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        lo, hi = 0, len(cells)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if self.isCrossable(row, col, mid, cells):
                lo = mid+1
            else:
                hi = mid-1
                
        return lo