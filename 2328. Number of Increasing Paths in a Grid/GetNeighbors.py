import heapq
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
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        row, col = coord
        for x, y in directions:
            new_row, new_col = x+row, y+col
            if self.inBound(new_row, new_col, grid) and grid[new_row][new_col] > grid[row][col]:
                nbrs.append((new_row, new_col))
                
        return nbrs
    
    
    # O(n*mlog(m*n)) time,
    # O(n*m) space,
    # Approach: bottom up dp, heap
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        max_heap = []
        dp = [[1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                val = grid[row][col]
                heapq.heappush(max_heap, (-val, (row, col)))
        
        ans = 0
        while max_heap:
            _, coord = heapq.heappop(max_heap)
            row, col = coord
            for nbr in self.getNeighbors(coord, grid):
                nbr_row, nbr_col = nbr
                dp[row][col] += dp[nbr_row][nbr_col]
            ans += dp[row][col]
            ans %= MOD
            
        return ans