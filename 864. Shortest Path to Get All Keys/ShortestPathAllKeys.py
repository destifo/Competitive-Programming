from collections import deque
from copy import deepcopy
from typing import List


class Solution:
    
    def isInbound(self, row, col, grid):
        
        ROWS, COLS = len(grid), len(grid[0])
        
        if row < 0 or row >= ROWS:
            return False
        
        if col < 0 or col >= COLS:
            return False
        
        return True
    
    
    def getNeighbors(self, coord, grid):
        
        nbrs = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dirc in directions:
            
            new_row, new_col = coord[0] + dirc[0], coord[1] + dirc[1]
            if self.isInbound(new_row, new_col, grid) and grid[new_row][new_col] != "#":
                nbrs.append((new_row, new_col))
                
        return nbrs
    
    
    def unlockAllDoors(self, coord, tot_keys, grid):
        queue = deque()
        curr_keys = tuple()
        queue.append((coord, curr_keys))
        visited = set()
        
        depth = 0
        
        while queue:
            queue_len = len(queue)
            
            for _ in range(queue_len):
                curr_coord, curr_keys = queue.popleft()
                sorted_tuple = tuple(sorted(curr_keys))
                if (curr_coord, sorted_tuple) in visited:
                    continue
                    
                if len(curr_keys) == tot_keys:
                    return depth
                
                visited.add((curr_coord, sorted_tuple))
                
                for nbr in self.getNeighbors(curr_coord, grid):
                    val = grid[nbr[0]][nbr[1]]
                    if val.islower() and val not in curr_keys:
                        queue.append((nbr, curr_keys + (val,)))
                        continue
                        
                    if val.isupper() and val.lower() not in curr_keys:
                        continue
                        
                    queue.append((nbr, deepcopy(curr_keys)))
            
            depth += 1
            
        return -1
    
    # too lazy to analyze complexity
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        tot_keys = 0
        start = (0, 0)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col].islower():
                    tot_keys += 1
                    
                if grid[row][col] == "@":
                    start = (row, col)
                    
            grid[row] = list(grid[row])
        
        moves = self.unlockAllDoors(start, tot_keys, grid)

        return moves if moves != float('inf') else -1