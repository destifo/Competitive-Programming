from collections import deque
import copy
from typing import List


class Solution:
    
    def inBounds(self, row: int, col: int, board: List[List[int]]) -> bool:
        
        if row < 0 or row >= len(board):
            return False
        
        if col < 0 or col >= len(board[0]):
            return False
        
        return True
    
    
    def getNeighbors(self, board: List[List[int]]) -> List[List[List[int]]]:
        nbrs = []
        zero_coord = None
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 0:
                    zero_coord = (row, col)
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for x, y in directions:
            new_row, new_col = x+zero_coord[0], y+zero_coord[1]
            if self.inBounds(new_row, new_col, board):
                duplicate_board = copy.deepcopy(board)
                duplicate_board[zero_coord[0]][zero_coord[1]], duplicate_board[new_row][new_col] = duplicate_board[new_row][new_col], duplicate_board[zero_coord[0]][zero_coord[1]]
                nbrs.append(duplicate_board)

        return nbrs
    
    
    def getState(self, board: List[List[int]]) -> str:
        state = []
        
        for row in board:
            for num in row:
                state.append(str(num))
                
        return "".join(state)
        
    
    # O((m*n)!) time,
    # O((m*n)!) space,
    # Approach: bfs, matrix
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        queue = deque()
        start_state = self.getState(board)
        queue.append((board, start_state))
        visited = set()
        visited.add(start_state)
        final_state = "123450"
        moves = 0
        
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                curr_board, curr_state = queue.popleft()
                if curr_state == final_state:
                    return moves
                
                for nbr in self.getNeighbors(curr_board):
                    nbr_state = self.getState(nbr)
                    if nbr_state in visited:
                        continue
                    visited.add(nbr_state)
                    queue.append((nbr, nbr_state))
            moves += 1
            
        return -1