from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        result = [[0 for i in range(n)] for j in range(m)]
        qu = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    qu.append((i, j))
                    
                
        def get_neighbours(i, j):
            clr = 1
            neighbours = []
            m = len(mat)
            k = len(mat[0])
            if j > 0 and mat[i][j-1] == clr:
                neighbours.append((i, j-1))
            if j < k-1 and mat[i][j+1] == clr:
                neighbours.append((i, j+1))
            if i > 0 and mat[i-1][j] == clr:
                neighbours.append((i-1, j))
            if i < m-1 and mat[i+1][j] == clr:
                neighbours.append((i+1, j))
                
            return neighbours
        
        
        def bfs():
            dist = -1
            while qu:
                k = len(qu)
                dist +=1
                for i in range(k):
                    coord = qu.popleft()
                    x, y = coord
                    cell = mat[x][y]
                    if cell != 0 and result[x][y] == 0:
                        result[x][y] = dist
                    neighbours = get_neighbours(x, y)
                    for neighbour in neighbours:
                        x, y = neighbour
                        if result[x][y] == 0:
                            qu.append(neighbour)
        bfs()
        
        return result
            

sol = Solution()
val = sol.updateMatrix([
[0,1,1,0,0],
[0,1,1,0,0],
[0,1,0,0,1],
[1,1,1,1,0],
[1,0,0,1,0]])
for row in val:
    print(row)