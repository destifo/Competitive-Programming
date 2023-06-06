'''
https://leetcode.com/problems/number-of-islands/
'''


from typing import *


class Solution:
    # O(m*n) time,
    # O(m*n) space,
    # Approach: DFS, hashmap
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        unvstd_land = set()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    unvstd_land.add((i, j))
        
        
        def getNeighbours(land: Tuple) -> List[Tuple]:
            n = len(grid)
            m = len(grid[0])
            neighbours = []
            i, j = land
            
            # print((x, y) in unvstd_land)
            
            if i < n-1:
                if grid[i+1][j] == '1' and (i+1, j) in unvstd_land:
                    neighbours.append((i+1, j))   
            if i > 0:
                if grid[i-1][j] == '1' and (i-1, j) in unvstd_land:
                    neighbours.append((i-1, j))
            if j > 0:
                if grid[i][j-1] == '1' and (i, j-1) in unvstd_land:
                    neighbours.append((i, j-1))
            if j < m-1:
                if grid[i][j+1] == '1' and (i, j+1) in unvstd_land:
                    neighbours.append((i, j+1))
            
            return neighbours
                    
        
        def removeConnectedLands(land: Tuple) -> None:
            if land not in unvstd_land:
                return
            
            unvstd_land.remove(land)
            
            neighbours = getNeighbours(land)
            # print(neighbours)
            if not neighbours:
                return
            
            for neighbour in neighbours:
                removeConnectedLands(neighbour)
        
        islands = 0
        while unvstd_land:
            islands +=1
            for land in unvstd_land:
                break
            removeConnectedLands(land)
    
        return islands