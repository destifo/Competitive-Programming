from collections import deque
from typing import List, Tuple


class Solution:
    
    def inBound(self, row: int, col: int, grid: List[List[int]]) -> bool:        
        if row < 0 or row >= len(grid):
            return False
        
        if col < 0 or col >= len(grid[0]):
            return False
        
        return True
    
    
    def getNeighbors(self, coord: Tuple[int], grid: List[List[int]]) -> List[Tuple[int]]:
        
        nbrs = []
        row, col = coord
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for x, y in directions:
            new_row, new_col = row+x, col+y
            if not self.inBound(new_row, new_col, grid):
                nbrs.append((-1, -1))
            elif grid[new_row][new_col] == 0:
                nbrs.append((new_row, new_col))
                
        return nbrs
            
    
    def areClosedLands(self, coord: Tuple[int], grid: List[List[int]]) -> bool:
        
        queue = deque()
        queue.append(coord)
        is_closed = True
        
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                land = queue.popleft()
                if land == (-1, -1):
                    is_closed = False
                    continue
                
                if grid[land[0]][land[1]] != 0:
                    continue
                grid[land[0]][land[1]] = 1
                for nbr in self.getNeighbors(land, grid):
                    queue.append(nbr)

        return is_closed
    
    
    # O(m*n) time,
    # O(1) space,
    # Approach: bfs, 
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        lands = []
        closed_lands = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    lands.append((row, col))

        for land in lands:
            row, col = land
            if grid[row][col] != 0:
                continue
                
            if self.areClosedLands((row, col), grid):
                closed_lands += 1

        return closed_lands