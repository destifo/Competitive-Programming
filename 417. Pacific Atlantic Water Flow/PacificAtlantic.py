'''
https://leetcode.com/problems/pacific-atlantic-water-flow/
'''


from collections import deque
from typing import *


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: BFS, hashset, matrix
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        
        def bfs(qu: Deque) -> Set[int]:
            vstd = set()
            for cell in qu:
                vstd.add(cell)
            
            while qu:
                n = len(qu)
                for i in range(n):
                    cell = qu.popleft()
                    nbrs = getNeighbours(cell)
                    for nb in nbrs:
                        if nb in vstd:  continue
                        qu.append(nb)
                        vstd.add(nb)
            
            return vstd
            
            
        def getNeighbours(cell: List[int]) -> List[List[int]]:
            n = len(heights)
            m = len(heights[0])
            neighbours = []
            x, y = cell
            cell_height = heights[x][y]
            
            if x > 0 and heights[x-1][y] >= cell_height:
                neighbours.append((x-1, y))
            
            if y > 0 and heights[x][y-1] >= cell_height:
                neighbours.append((x, y-1))
            if x < n-1 and heights[x+1][y] >= cell_height:
                neighbours.append((x+1, y))
            if y < m-1 and heights[x][y+1] >= cell_height:
                neighbours.append((x, y+1))
                
            return neighbours
                
        
        pacific_borders = deque()
        for i in range(m):
            pacific_borders.append((0, i))
        for j in range(n):
            pacific_borders.append((j, 0))
            
        pacific_reachables = bfs(pacific_borders)
        
        atlantic_borders = deque()
        for i in range(m):
            atlantic_borders.append((n-1, i))
        for j in range(n):
            atlantic_borders.append((j, m-1))
        
        atlantic_reachables = bfs(atlantic_borders)
        
        result = []
        for cell in atlantic_reachables:
            if cell in pacific_reachables:
                result.append([cell[0], cell[1]])
                
        return result