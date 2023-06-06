'''
https://leetcode.com/problems/surrounded-regions/
'''


from typing import List


class Solution:
    # O(m*n) time, 
    # O(1) space, when storing the neighbours
    # Approach: DFS, reverse thinking
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        
        def getONeighbours(root):
            x, y = root
            neighbours = []
            
            if x > 0 and board[x-1][y] == 'O':
                neighbours.append((x-1, y))
            if x < n-1 and board[x+1][y] == 'O':
                neighbours.append((x+1, y))
            if y > 0 and board[x][y-1] == 'O':
                neighbours.append((x, y-1))
            if y < m-1 and board[x][y+1] == 'O':
                neighbours.append((x, y+1))
                
            return neighbours
            
        
        def markNonSurrounded(root):
            x, y = root
            if board[x][y] == 'N':
                return
            board[x][y] = 'N'
            
            neighbours = getONeighbours(root)
            for neighbour in neighbours:
                markNonSurrounded(neighbour)
                
            
            
        xborders = [0, n-1]
        for i in range(m):
            for border in xborders:
                if board[border][i] == 'O':
                    markNonSurrounded((border, i))
        
        yborders = [0, m-1]
        for i in range(n):
            for border in yborders:
                if board[i][border] == 'O':
                    markNonSurrounded((i, border))
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'N':
                    board[i][j] = 'O'