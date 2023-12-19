from typing import List, Tuple


class Solution:
    
    def inBound(self, row: int, col: int, grid: List[List[int]]) -> int:
        
        if row < 0 or row >= len(grid):
            return False
        
        if col < 0 or col >= len(grid[0]):
            return False
        
        return True
    
    
    def getNeighbors(self, row: int, col: int, grid: List[List[int]]) -> List[Tuple[int]]:
        
        nbrs = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for x, y in directions:
            new_row, new_col = x+row, y+col
            if self.inBound(new_row, new_col, grid):
                nbrs.append((new_row, new_col))
                
        return nbrs
    
    
    # O(n*m) time,
    # O(n*m) space,
    # Approach: matrix, 
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(img), len(img[0])
        smoothed = [[img[j][i] for i in range(COLS)] for j in range(ROWS)]
        
        for row in range(ROWS):
            for col in range(COLS):
                nbrs = self.getNeighbors(row, col, img)
                for nbr_row, nbr_col in nbrs:
                    smoothed[row][col] += img[nbr_row][nbr_col]
                smoothed[row][col] //= len(nbrs)+1
                
        return smoothed