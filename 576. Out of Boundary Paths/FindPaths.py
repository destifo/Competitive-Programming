class Solution:
    
    # O(n*m*maxMove) time,
    # O(n*m*maxMove) space,
    # Approach: top down dp, 
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:        
        def outOfBounds(row: int, col: int) -> bool:
            
            if row < 0 or row >= m:
                return True
            
            if col < 0 or col >= n:
                return True
            
            return False
        
        def getNeighbors(row: int, col: int):
            nbrs = []
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for x, y in directions:
                nbrs.append((row+x, col+y))
                
            return nbrs
                
        memo = {}
        def countPaths(row: int, col: int, moves: int) -> int:
            
            if outOfBounds(row, col):
                return 1
            
            if moves == 0:
                return 0
            
            state = (row, col, moves)
            if state in memo:
                return memo[state]
            
            paths = 0
            for nbr_row, nbr_col in getNeighbors(row, col):
                paths += countPaths(nbr_row, nbr_col, moves-1)
                
            memo[state] = paths
            return paths
        
            
        MOD = 10**9 + 7
        return countPaths(startRow, startColumn, maxMove) % MOD