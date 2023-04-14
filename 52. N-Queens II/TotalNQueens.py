from collections import defaultdict
from typing import List


class Solution:
    
    def isValidPlacement(self, row: int, col: int, cols: List[bool], diagonals1: List[int], diagonals2: List[bool]) -> bool:
        
        return not diagonals1[row+col] and not cols[col] and not diagonals2[(row-col)]
    
    
    def countPossiblePlacements(self, row: int, cols: List[bool], diagonals1: List[bool], diagonals2: List[bool]) -> None:
        
        if row == len(cols):
            return 1
        
        count = 0
        for col in range(len(cols)):
            if self.isValidPlacement(row, col, cols, diagonals1, diagonals2):
                cols[col] = True
                diagonals1[row+col] = True
                diagonals2[(row-col)] = True
                count += self.countPossiblePlacements(row+1, cols, diagonals1, diagonals2)
                cols[col] = False
                diagonals1[row+col] = False
                diagonals2[(row-col)] = False
                
        return count
                
    
    # O(n!) time,
    # O(n!) space,
    # Approach: backtracking, math
    def totalNQueens(self, n: int) -> List[List[str]]:
        cols = [False for _ in range(n)]
        diagonals1 = [False for _ in range(2*n-1)]
        diagonals2 = defaultdict(bool)
        
        return self.countPossiblePlacements(0, cols, diagonals1, diagonals2)