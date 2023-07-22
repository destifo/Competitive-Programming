from typing import List, Tuple


class Solution:
    
    def inBound(self, coord: Tuple[int], dimension: int) -> bool:
        row, col = coord
        if row < 0 or row >= dimension:
            return False
        
        if col < 0 or col >= dimension:
            return False
        
        return True
    
    
    def getNeighbors(self, n: int, coord: Tuple[int]) -> List[Tuple[int]]:
        nbrs = []
        directions = [(-2, 1), (-2, -1), (-1, -2), (1, -2),
                     (2, 1), (2, -1), (-1, 2), (1, 2)]
        row, col = coord
        
        for x, y in directions:
            nbr_row, nbr_col = row+x, col+y
            if self.inBound((nbr_row, nbr_col), n):
                nbrs.append((nbr_row, nbr_col))
            
        return nbrs
    
    
    # O(n^2*k) time,
    # O(n^2*k) space,
    # Approach: bottom-up dp, 
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k+1)]
        
        dp[0][row][column] = 1
        
        for move in range(1, k+1):
            for row in range(n):
                for col in range(n):
                    for nbr_row, nbr_col in self.getNeighbors(n, (row, col)):
                        dp[move][row][col] += 1/8 * dp[move-1][nbr_row][nbr_col]
        
        prob = 0
        for row in range(n):
            for col in range(n):
                prob += dp[k][row][col]

        return prob