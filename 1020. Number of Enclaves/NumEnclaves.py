'''
https://leetcode.com/problems/number-of-enclaves/
'''


from typing import List


class Solution:
    # O(m*n) time,
    # O(1) space,
    # Approach: DFS, reverse thinking
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def getONeighbours(root):
            x, y = root
            neighbours = []
            
            if x > 0 and grid[x-1][y] == 1:
                neighbours.append((x-1, y))
            if x < n-1 and grid[x+1][y] == 1:
                neighbours.append((x+1, y))
            if y > 0 and grid[x][y-1] == 1:
                neighbours.append((x, y-1))
            if y < m-1 and grid[x][y+1] == 1:
                neighbours.append((x, y+1))
                
            return neighbours
            
        
        def markNonSurrounded(root):
            x, y = root
            if grid[x][y] == 'N':
                return
            grid[x][y] = 'N'
            
            neighbours = getONeighbours(root)
            for neighbour in neighbours:
                markNonSurrounded(neighbour)      
            
            
        xborders = [0, n-1]
        for i in range(m):
            for border in xborders:
                if grid[border][i] == 1:
                    markNonSurrounded((border, i))
        
        yborders = [0, m-1]
        for i in range(n):
            for border in yborders:
                if grid[i][border] == 1:
                    markNonSurrounded((i, border))
        
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count +=1
        
        return count