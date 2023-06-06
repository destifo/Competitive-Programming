'''
https://leetcode.com/problems/rotting-oranges/
'''


from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return -1 if grid[0][0] == 1 else 0
        qu = deque()
        vstd = set()
        emty_num = 0
        
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell == 0:
                    emty_num +=1
                elif cell == 2:
                    qu.append((i, j))
                    vstd.add((i, j))
                    
        if emty_num == (m*n):   return 0
                    
        def get_neighbours(i, j):
            clr = 1
            neighbours = []
            m = len(grid)
            k = len(grid[0])
            if j > 0 and grid[i][j-1] == clr:
                neighbours.append((i, j-1))
            if j < k-1 and grid[i][j+1] == clr:
                neighbours.append((i, j+1))
            if i > 0 and grid[i-1][j] == clr:
                neighbours.append((i-1, j))
            if i < m-1 and grid[i+1][j] == clr:
                neighbours.append((i+1, j))
                
            return neighbours
                    
        time = -1
        while qu:
            k = len(qu)
            time +=1
            for i in range(k):
                coord = qu.popleft()
                # if coord in vstd:   continue
                vstd.add(coord)
                x, y = coord
                cell = grid[x][y]
                neighbours = get_neighbours(x, y)
                for neighbour in neighbours:
                    if neighbour in vstd:   continue
                    qu.append(neighbour)
                    vstd.add(neighbour)
                grid[x][y] = 2
                
        return time if (emty_num + len(vstd) == (m*n)) else -1 