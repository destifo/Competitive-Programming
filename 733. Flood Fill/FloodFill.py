'''
https://leetcode.com/problems/flood-fill/
'''


from collections import deque


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        visited = set()
        qu = deque()
        qu.append((sr, sc))
        
        def get_neighbours(i, j, clr):
            neighbours = []
            m = len(image)
            k = len(image[0])
            if j > 0 and image[i][j-1] == clr:
                neighbours.append((i, j-1))
            if j < k-1 and image[i][j+1] == clr:
                neighbours.append((i, j+1))
            if i > 0 and image[i-1][j] == clr:
                neighbours.append((i-1, j))
            if i < m-1 and image[i+1][j] == clr:
                neighbours.append((i+1, j))
                
            return neighbours
        
        prev_clr = image[sr][sc]
        while qu:
            n = len(qu)
            for i in range(n):
                pix_loc = qu.popleft()
                visited.add(pix_loc)
                x, y = pix_loc
                image[x][y] = color
                neighbours = get_neighbours(x, y, prev_clr)
                for neighbour in neighbours:
                    if neighbour in visited:    continue
                    qu.append(neighbour)
        
        return image


sol = Solution()
print(sol.floodFill([[0,0,0],[0,0,0]]
,1
,0
,2))