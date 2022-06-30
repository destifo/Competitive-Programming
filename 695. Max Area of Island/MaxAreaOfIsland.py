'''
https://leetcode.com/problems/max-area-of-island/
'''


from collections import deque


class Solution:
    # a bfs inside a bfs, ;-}
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited = set()
        qu = deque()
        qu.append((0, 0))
        max_area = 0


        def get_land_neighbours(i, j):
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
        
        def get_neighbours(i, j):
            neighbours = []
            m = len(grid)
            k = len(grid[0])
            if j > 0:
                neighbours.append((i, j-1))
            if j < k-1:
                neighbours.append((i, j+1))
            if i > 0:
                neighbours.append((i-1, j))
            if i < m-1:
                neighbours.append((i+1, j))
                
            return neighbours

        vstd_land = set()
        def bfs(i, j):
            land_qu = deque()
            land_qu.append((i, j))
            area = 0

            while land_qu:
                n = len(land_qu)
                for i in range(n):
                    land_loc = land_qu.popleft()
                    if land_loc in vstd_land:   continue
                    area +=1
                    vstd_land.add(land_loc)
                    # visited.add(land_loc)
                    x, y = land_loc
                    neighbours = get_land_neighbours(x, y)
                    for neighbour in neighbours:
                        if neighbour in vstd_land:    continue
                        land_qu.append(neighbour)
            
            return area

        while qu:
            n = len(qu)
            for i in range(n):
                place_loc = qu.popleft()
                if place_loc in visited:   continue
                x, y = place_loc
                if grid[x][y] == 1 and place_loc not in vstd_land:
                    area = bfs(x, y)
                    max_area = max(max_area, area)
                else:
                    visited.add(place_loc)
                neighbours = get_neighbours(x, y)
                for neighbour in neighbours:
                    if neighbour in visited:    continue
                    qu.append(neighbour)

        return max_area


sol = Solution()
print(sol.maxAreaOfIsland([
[1,1,0,0,0],
[1,1,0,0,0],
[0,0,0,1,1],
[0,0,0,1,1]]))              