from collections import deque
from typing import List


class Solution:
    
    def inBound(self, row, col, maze):
        
        return not (row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]))
    
    
    def isBorder(self, coord, maze):
        
        return coord[0] == 0 or coord[0] == len(maze)-1 or coord[1] == 0 or coord[1] == len(maze[0])-1
    
    
    def getNeighbors(self, coord, maze):
        
        nbrs = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for direction in directions:
            nbr_row, nbr_col = direction[0]+coord[0], direction[1]+coord[1]
            if self.inBound(nbr_row, nbr_col, maze) and maze[nbr_row][nbr_col] == '.':
                nbrs.append((nbr_row, nbr_col))
                
        return nbrs
    
    
    # O(m*n) time,
    # O(1) space,
    # Approach: bfs, 
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int: 
        queue = deque()
        queue.append((entrance[0], entrance[1]))
        short_dist = 0
        
        while queue:
            n = len(queue)
            for _ in range(n):
                coord = queue.popleft()
                if maze[coord[0]][coord[1]] != ".":
                    continue
                
                maze[coord[0]][coord[1]] = "+"
                if short_dist > 0 and self.isBorder(coord, maze):
                    return short_dist
                
                for nbr in self.getNeighbors(coord, maze):
                    queue.append(nbr)    
            short_dist += 1
            
        return -1