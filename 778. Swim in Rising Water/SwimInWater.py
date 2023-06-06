'''
https://leetcode.com/problems/swim-in-rising-water/
'''


from collections import deque
import heapq
from typing import *


class Solution:
    # O(max(n^2, m)) time, h --> the highest elevation in the grid
    # O(n^2) space,
    # Approach: BFS, Priority queue
    # I wld advise to do task scheduler question, it's pretty similar
    # except that u apply bfs to traverse the grid 4 directionally
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0
        
        def getNeighbours(coord: Tuple) -> List[Tuple]:
            i, j = coord
            n = len(grid)
            neighbours = []
            
            if i < n-1:
                neighbours.append((i+1, j))
            if i > 0:
                neighbours.append((i-1, j))
            if j < n-1:
                neighbours.append((i, j+1))
            if j > 0:
                neighbours.append((i, j-1))
                
            return neighbours
        
        qu = deque()
        waiting_qu = []
        vstd = set()
        waiting_qu.append([grid[0][0], (0, 0)])
        vstd.add((0, 0))
        time = 0
        
        while waiting_qu:
            time +=1
            while waiting_qu and waiting_qu[0][0] <= time:
                qu.append(heapq.heappop(waiting_qu)[1])
            
            while qu:
                cell = qu.popleft()
                if cell == (n-1, n-1):
                    return time
                nbrs = getNeighbours(cell)
                for nb in nbrs:
                    if nb in vstd:  continue
                    x, y = nb
                    elevation = grid[x][y]
                    vstd.add(nb)
                    if elevation > time:
                        heapq.heappush(waiting_qu, [elevation, nb])
                    else:
                        qu.append(nb)
        
        return -1