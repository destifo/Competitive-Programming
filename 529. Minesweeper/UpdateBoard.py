'''
https://leetcode.com/problems/minesweeper/
'''


from typing import *


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: DFS, hashset
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n = len(board)
        m = len(board[0])
        
        def getNeighbours(coord):
            i, j = coord
            neighbours = []
            
            if i > 0:
                neighbours.append((i-1, j))
                if j > 0:
                    neighbours.append((i-1, j-1))
                if j < m-1:
                    neighbours.append((i-1, j+1))
                    
            if i < n-1:
                neighbours.append((i+1, j))
                if j > 0:
                    neighbours.append((i+1, j-1))
                if j < m-1:
                    neighbours.append((i+1, j+1))
            
            if j > 0:
                neighbours.append((i, j-1))
            if j < m-1:
                neighbours.append((i, j+1))
            
            return neighbours
        
        def reveal(click: List[List[int]]) -> None:
            x, y = click
            if board[x][y] == 'M':
                board[x][y] = 'X'
                return
            
            stack = [(x, y)]
            vstd = set()
            
            while stack:
                cell = stack.pop()
                if cell in vstd:
                    continue
                vstd.add(cell)
                x, y = cell
                
                bomb_count = 0
                
                neighbours = getNeighbours(cell)
                for nb in neighbours:
                    i, j = nb
                    if board[i][j] == 'M':
                        bomb_count +=1
                
                if bomb_count > 0:
                    board[x][y] = str(bomb_count)
                else:
                    board[x][y] = 'B'
                    stack.extend(neighbours)
              
        reveal(click)
        return board