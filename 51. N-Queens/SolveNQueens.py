from collections import defaultdict
from typing import List


class Solution:
    
    def isValidPlacement(self, row: int, col: int, cols: List[bool], diagonals1: List[int], diagonals2: List[bool]) -> bool:
        
        return not diagonals1[row+col] and not cols[col] and not diagonals2[(row-col)]
    
    
    def placeQueens(self, row: int, board: List[List[str]], cols: List[bool], diagonals1: List[bool], diagonals2: List[bool], ans) -> None:
        
        if row == len(board):
            valid_board = ["".join(row) for row in board]
            ans.append(valid_board)
            return
        for col in range(len(board)):
            if self.isValidPlacement(row, col, cols, diagonals1, diagonals2):
                board[row][col] = "Q"
                cols[col] = True
                diagonals1[row+col] = True
                diagonals2[(row-col)] = True
                self.placeQueens(row+1, board, cols, diagonals1, diagonals2, ans)
                board[row][col] = "."
                cols[col] = False
                diagonals1[row+col] = False
                diagonals2[(row-col)] = False
                
    
    # O(n!) time,
    # O(n!) space,
    # Approach: backtracking, math
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = [False for _ in range(n)]
        diagonals1 = [False for _ in range(2*n-1)]
        diagonals2 = defaultdict(bool)
        ans = []
        
        self.placeQueens(0, board, cols, diagonals1, diagonals2, ans)
           
        return ans