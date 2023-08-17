from collections import deque
from typing import List, Tuple


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
    
    
    def inBound(self, row: int, col: int, mat: List[List[int]]) -> bool:
        
        if row < 0 or row >= len(mat):
            return False
        
        if col < 0 or col >= len(mat[0]):
            return False
        
        return True
    
    
    def getNeighbors(self, row: int, col: int, mat: List[List[int]]) -> List[Tuple[int]]:
        nbrs = []
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for x, y in directions:
            new_row, new_col = x+row, y+col
            if self.inBound(new_row, new_col, mat) and mat[new_row][new_col] == 1:
                nbrs.append((new_row, new_col))
                
        return nbrs
    
    
    # O(n*m) time,
    # O(n*m) space,
    # Approach: bfs, graph, 
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        n, m = len(mat), len(mat[0])
        
        for row in range(n):
            for col in range(m):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    
        ans = [[0 for _ in range(m)] for _ in range(n)]
        dist = 0
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                row, col = queue.popleft()
                nbrs = self.getNeighbors(row, col, mat)
                ans[row][col] = dist
                for nbr in nbrs:
                    mat[nbr[0]][nbr[1]] = 0
                    queue.append(nbr)
                
            dist += 1
            
        return ans
            

sol = Solution()
val = sol.updateMatrix([
[0,1,1,0,0],
[0,1,1,0,0],
[0,1,0,0,1],
[1,1,1,1,0],
[1,0,0,1,0]])
for row in val:
    print(row)