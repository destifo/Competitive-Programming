from collections import deque
from typing import List


class Solution:
    
    def isInBounds(self, a, b, dimension) -> bool:
        if a < 0 or a >= dimension:
            return False
        
        if b < 0 or b >= dimension:
            return False
        
        return True
    
    
    def getNeighbors(self, coord, grid):
        
        dimension = len(grid)
        row, col = coord
        neighbors = []
        
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for dirc in directions:
            new_row, new_col = row+dirc[0], col+dirc[1]
            if self.isInBounds(new_row, new_col, dimension) and grid[new_row][new_col] == 0:
                neighbors.append((new_row, new_col))
                
        return neighbors
            
    
    
    def bfs(self, queue, grid):
        
        depth = -1
        
        while queue:
            n = len(queue)
            depth += 1
            for _ in range(n):
                curr_coord = queue.popleft()
                curr_row, curr_col = curr_coord
                
                for nb in self.getNeighbors(curr_coord, grid):
                    queue.append(nb)
                    grid[nb[0]][nb[1]] = 1
                    
        
        return depth if depth > 0 else -1
    
    # O(n^2) time,
    # O(1) space,
    # Approach: bfs, graph, 
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        dimension = len(grid)
        lands = deque()
        for row in range(dimension):
            for col in range(dimension):
                if grid[row][col] == 1:
                    lands.append((row, col))
                    
        return self.bfs(lands, grid)