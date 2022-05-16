from collections import deque


class Solution:
    # naive solution, traveses the matrix one time and the graph one other time
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        edges = dict()
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0 or (i == n - 1 and j == n - 1):
                    continue
                key = ""
                key += str(i)
                key += str(j)
                edges[key] = []
                if i - 1 >= 0 and not grid[i - 1][j]:
                    edges[key].append(str(i - 1) + str(j))
                if i + 1 < n and not grid[i + 1][j]:
                    edges[key].append(str(i + 1) + str(j))
                if j - 1 >= 0 and i - 1 >= 0 and not grid[i - 1][j - 1]:
                    edges[key].append(str(i - 1) + str(j - 1))
                if i + 1 < n and j + 1 < n and not grid[i + 1][j + 1]:
                    edges[key].append(str(i + 1) + str(j + 1))
                if j + 1 < n and not grid[i][j + 1]:
                    edges[key].append(str(i) + str(j + 1))
                if j - 1 >= 0 and not grid[i][j - 1]:
                    edges[key].append(str(i) + str(j - 1))
                if j + 1 < n and i - 1 >= 0 and grid[i - 1][j + 1] == 0:
                    edges[key].append(str(i - 1) + str(j + 1))
                if i + 1 < n and j - 1 >= 0 and not grid[i + 1][j - 1]:
                    edges[key].append(str(i + 1) + str(j - 1))

        qu = deque()
        qu.append("00")
        if "00" not in edges.keys():
            return -1
        visited = set()
        final_str = str(n - 1) + str(n - 1)

        def bfs(dist):
            if not qu:
                return -1
            
            n = len(qu)
            for i in range(n):
                node = qu.popleft()
                visited.add(node)
                for nod in edges[node]:
                    if nod == final_str:
                        return dist + 1
                    if nod not in visited:
                        qu.append(nod)

            return bfs(dist + 1)

        print(edges)
        return bfs(1)

    # only traverses the matrix one time
    def shortestPathBinaryMatrix2(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        qu = deque()
        qu.append([0, 0, 1])

        while qu:
            m = len(qu)
            for ind in range(m):
                cell = qu.popleft()
                i, j = cell[0], cell[1]
                currDist = cell[2]
                if i == (n - 1) and j == (n - 1):
                    return currDist

                grid[i][j] = 1
                if i - 1 >= 0 and not grid[i - 1][j]:
                    qu.append([i - 1, j, currDist + 1])
                    grid[i - 1][j] = 1
                if i + 1 < n and not grid[i + 1][j]:
                    qu.append([i + 1, j, currDist + 1])
                    grid[i + 1][j] = 1
                if j - 1 >= 0 and i - 1 >= 0 and not grid[i - 1][j - 1]:
                    grid[i - 1][j - 1] = 1
                    qu.append([i - 1, j - 1, currDist + 1])
                if i + 1 < n and j + 1 < n and not grid[i + 1][j + 1]:
                    grid[i + 1][j + 1] = 1
                    qu.append([i + 1, j + 1, currDist + 1])
                if j + 1 < n and not grid[i][j + 1]:
                    qu.append([i, j + 1, currDist + 1])
                    grid[i][j + 1] = 1
                if j - 1 >= 0 and not grid[i][j - 1]:
                    qu.append([i, j - 1, currDist + 1])
                    grid[i][j - 1] = 1
                if j + 1 < n and i - 1 >= 0 and grid[i - 1][j + 1] == 0:
                    qu.append([i - 1, j + 1, currDist + 1])
                    grid[i - 1][j + 1] = 1
                if i + 1 < n and j - 1 >= 0 and not grid[i + 1][j - 1]:
                    qu.append([i + 1, j - 1, currDist + 1])
                    grid[i + 1][j - 1] = 1

        return -1

                


sol = Solution()
print(sol.shortestPathBinaryMatrix2([
[0,1,1,0,0,0],
[0,1,0,1,1,0],
[0,1,1,0,1,0],
[0,0,0,1,1,0],
[1,1,1,1,1,0],
[1,1,1,1,1,0]]))
