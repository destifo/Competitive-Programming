from typing import List


class Solution:
    
    def inBounds(self, x: int, y: int, ROWS: int, COLS: int) -> bool:
        
        if x < 0 or x >= ROWS:  return False
        
        if y < 0 or y >= COLS:  return False
        
        return True
    
    
    def getAliveNeighbors(self, row: int, col: int, board: List[List[int]]) -> int:
        
        ROWS, COLS = len(board), len(board[0])
        
        alive = 0
        
        directions = [ [0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1] ]
        for x, y in directions:
            
            if self.inBounds(row+x, col+y, ROWS, COLS) and board[row+x][col+y] == 1:
                alive += 1   
                
        return alive
    
    
    # O(ROWS*COLS) time,
    # O(ROWS*COLS) space,
    # Approach: matrix, simulation, hashset
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        change = []
        
        for row in range(ROWS):
            for col in range(COLS):
                alive = self.getAliveNeighbors(row, col, board)
                next_state = board[row][col]
                
                if alive < 2 or alive > 3:
                    next_state = 0
                elif alive == 2:
                    next_state = board[row][col]
                else:
                    next_state = 1
                    
                if next_state != board[row][col]:
                    change.append((row, col))
                    
        for row, col in change:
            board[row][col] = abs(board[row][col]-1)