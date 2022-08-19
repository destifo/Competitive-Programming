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

sol = Solution()
print(sol.exist([["C","A","A"],["A","A","A"],["B","C","D"]]
,"AAB"))