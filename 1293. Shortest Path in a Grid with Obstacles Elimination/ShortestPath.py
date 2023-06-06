from collections import defaultdict, deque
from typing import List, Tuple


class Solution:
    
    def inBounds(self, row: int, col: int, grid: List[List[int]]) -> bool:
        
        if row < 0 or row >= len(grid):
            return False
        
        if col < 0 or col >= len(grid[0]):
            return False
        
        return True
    
    
    def getNeighbors(self, coord: Tuple[int], grid: List[List[int]]) -> List[Tuple[int]]:
        row, col = coord
        nbrs = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for x, y in directions:
            new_row, new_col = row+x, col+y
            if self.inBounds(new_row, new_col, grid):
                nbrs.append((new_row, new_col))
                
        return nbrs
    
    
    def findMinPath(self, coord: Tuple[int], limit: int, grid: List[List[int]]) -> int:
        
        queue = deque()
        queue.append((coord, limit))
        dist = 0
        max_k = defaultdict(int)
        max_k[coord] = limit
        visited = set()
        
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                curr_coord, k = queue.popleft()
                if k < max_k[curr_coord] or (k, curr_coord) in visited:
                    continue

                if curr_coord == (len(grid)-1, len(grid[0])-1):
                    return dist
                curr_row, curr_col = curr_coord
                curr_val = grid[curr_row][curr_col]
                visited.add((k, curr_coord))
                if curr_val > k:
                    continue

                k -= curr_val
                for nbr in self.getNeighbors(curr_coord, grid):
                    max_k[nbr] = max(max_k[nbr], k)
                    queue.append((nbr, k))
                
            dist += 1
            
        return -1

    
    # O(m*n) time,
    # O(m*n) space,
    # Approach: bfs, 
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        return self.findMinPath((0, 0), k, grid)