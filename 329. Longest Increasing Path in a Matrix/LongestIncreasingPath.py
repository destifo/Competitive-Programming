import heapq
from typing import List, Tuple


class Solution:
    
    def inBounds(self, row: int, col: int, matrix: List[List[int]]) -> bool:
        
        if row < 0 or row >= len(matrix):
            return False
        
        if col < 0 or col >= len(matrix[0]):
            return False
        
        return True
    
    
    def getNeighbors(self, row: int, col: int, matrix: List[List[int]]) -> List[Tuple[int]]:
        
        nbrs = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for x, y in directions:
            new_row, new_col = row+x, col+y
            if self.inBounds(new_row, new_col, matrix) and matrix[new_row][new_col] > matrix[row][col]:
                nbrs.append((new_row, new_col))
                
        return nbrs
    
    
    # O(m*nlogm*n) time,
    # O(m*n) space,
    # Approach: heap, dp, graph, matrix
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
        heap = []
        for row in range(ROWS):
            for col in range(COLS):
                heapq.heappush(heap, (-matrix[row][col], row, col))
                
        ans = 0
        while heap:
            _, row, col = heapq.heappop(heap)
            max_dist = 0
            for nbr_row, nbr_col in self.getNeighbors(row, col, matrix):
                max_dist = max(max_dist, dp[nbr_row][nbr_col])
            
            dp[row][col] = max_dist + 1
            ans = max(ans, max_dist+1)
            
        return ans