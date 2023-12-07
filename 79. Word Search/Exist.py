'''
https://leetcode.com/problems/word-search/
'''


from typing import *


class Solution:
    # O(4*n) time,  n --> len(word)
    # O(n) space, 
    # Approach: DFS, backtracking, hashtable, 
    def exist(self, board: List[List[str]], word: str) -> bool:
        vstd = set()
        m = len(board)
        n = len(board[0])
        
        def getNeighbours(coord: Tuple) -> List[Tuple]:
            neighbours = []
            m = len(board)
            n = len(board[0])
            
            i, j = coord
            
            if i < m-1:
                neighbours.append((i+1, j))
            if i > 0:
                neighbours.append((i-1, j))
            if j < n-1:
                neighbours.append((i, j+1))
            if j > 0:
                neighbours.append((i, j-1))
        
            return neighbours
        
        
        def dfs(index: int, cell: Tuple) -> bool:
            if index == len(word):
                return True
            
            vstd.add(cell)
            neighbours = getNeighbours(cell)
            
            for nb in neighbours:
                if nb in vstd:  continue
                x, y = nb
                if board[x][y] == word[index]:
                    if dfs(index+1, nb):
                        return True
                    
            vstd.remove(cell)
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(1, (i, j)):
                        return True
                    vstd = set()
                    
        return False
    
    
    def inBounds(self, row: int, col: int, board: List[List[str]]) -> bool:
        if row < 0 or row >= len(board):
            return False
        
        if col < 0 or col >= len(board[0]):
            return False
        
        return True
    
    
    def getNeighbors(self, row: int, col: int, board: List[List[str]]) -> List[Tuple[int]]:
        
        nbrs = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for x, y in directions:
            new_row, new_col = row+x, col+y
            if self.inBounds(new_row, new_col, board) and board[new_row][new_col] != 0:
                nbrs.append((new_row, new_col))
                
        return nbrs
    
    
    def findWord(self, row: int, col: int, index: int, word: str, board: List[List[str]]) -> bool:
        if board[row][col] != word[index]:
            return False
        index +=1 
        if index == len(word):
            return True
        
        board[row][col] = 0
        for nbr_row, nbr_col in self.getNeighbors(row, col, board):
            if self.findWord(nbr_row, nbr_col, index, word, board):
                return True
            
        board[row][col] = word[index-1]
        return False
    
    
    # O((n*m)^2) time,
    # O((n*m)^2) space,
    # Approach: dfs, backtracking,  
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0] and self.findWord(row, col, 0, word, board):
                    return True
                    
        return False

sol = Solution()
print(sol.exist([["C","A","A"],["A","A","A"],["B","C","D"]]
,"AAB"))