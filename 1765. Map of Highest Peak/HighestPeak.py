from collections import deque
from typing import List


class Solution:
    
    def inBound(self, row: int, col: int, grid: List[List[int]]) -> bool:
        
        if row < 0 or row >= len(grid):
            return False
        
        if col < 0 or col >= len(grid[0]):
            return False
        
        return True
    
    
    def getNeighbors(self, row: int, col: int, isWater: List[List[int]]) -> int:
        
        nbrs = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for x, y in directions:
            if self.inBound(row+x, col+y, isWater) and isWater[row+x][col+y] == -1:
                nbrs.append((row+x, col+y))
                
        return nbrs
    
    
    # O(n*m) time,
    # O(1) space,
    # Approach: bfs, 
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        
        for row in range(len(isWater)):
            for col in range(len(isWater[0])):
                if isWater[row][col]:
                    queue.append((row, col))
                isWater[row][col] = -1
                
        height = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                row, col = queue.popleft()
                if isWater[row][col] != -1:
                    continue
                    
                isWater[row][col] = height
                for nbr in self.getNeighbors(row, col, isWater):
                    queue.append(nbr)
                    
            height += 1
        
        return isWater