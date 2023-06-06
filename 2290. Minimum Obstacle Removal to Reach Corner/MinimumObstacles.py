import heapq
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
            if self.inBounds(new_row, new_col, grid) and grid[new_row][new_col] != 2:
                nbrs.append((new_row, new_col))
                
        return nbrs
    
    
    def findMinRemovals(self, coord: Tuple[int], grid: List[List[int]]) -> int:
        row, col = coord
        heap = []
        memo = {}
        memo[coord] = 0
        heapq.heappush(heap, (grid[row][col], coord))
        
        while heap:
            removals, curr_coord = heapq.heappop(heap)
            if curr_coord == (len(grid)-1, len(grid[0])-1):
                return removals
            
            if memo[curr_coord] < removals:
                continue
            
            for nbr in self.getNeighbors(curr_coord, grid):
                nbr_removal = removals+grid[nbr[0]][nbr[1]]
                if nbr not in memo or memo[nbr] > nbr_removal:
                    memo[nbr] = nbr_removal
                    heapq.heappush(heap, (removals+grid[nbr[0]][nbr[1]], nbr))
                
        return -1
            
    
    # O(m*nlogm*n) time,
    # O(m*n) space,
    # Approach: bfs, heap, djikstra 
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        return self.findMinRemovals((0, 0), grid)