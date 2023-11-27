from typing import Dict, List, Tuple


class Solution:
    
    def inBound(self, row: int, col: int, grid: List[List[int]]) -> bool:
        
        if row < 0 or row >= len(grid):
            return False
        
        if col < 0 or col >= len(grid[0]):
            return False
        
        return True
    
    
    def getNeighbors(self, row: int, col: int, grid: List[List[int]]) -> List[Tuple[int]]:
        
        nbrs = []
        
        directions = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        for x, y in directions:
            new_row, new_col = row+x, col+y
            if self.inBound(new_row, new_col, grid) and grid[new_row][new_col] < 10:
                nbrs.append((new_row, new_col))
                
        return nbrs
    
    
    def findMovements(self, row: int, col: int, n: int, grid: List[List[int]], memo: Dict[int, int]) -> int:
        
        if n == 0:
            return 1
        
        val = grid[row][col]
        state = (val, n)
        if state in memo:
            return memo[state]
        
        tot = 0
        for nbr_row, nbr_col in self.getNeighbors(row, col, grid):
            tot += self.findMovements(nbr_row, nbr_col, n-1, grid, memo)
            
        memo[state] = tot
        return tot
    
    
    # O(n) time,
    # O(n) space,
    # Approach: top down dp, graph
    def knightDialer(self, n: int) -> int:
        
        '''
        
            (0, 0), (0, 1), (0, 2)
            (1, 0), (1, 1), (1, 2)
            (2, 0), (2, 1), (2, 2)
        
        '''
        
        MOD = 10**9 + 7
        ROWS, COLS = 3, 3
        grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
        for row in range(ROWS):
            for col in range(COLS):
                grid[row][col] = col+(row*3)+1
        grid.append([11, 0, 12])
        
        memo = {}
        ans = self.findMovements(3, 1, n-1, grid, memo)
        for row in range(ROWS):
            for col in range(COLS):
                ans += self.findMovements(row, col, n-1, grid, memo)
        
        return ans % MOD