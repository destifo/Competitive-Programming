from typing import List


class Solution:
    # O(m*n) time,
    # O(m*n) space,
    # Approach: dp, memoization
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        memo = [ [-1 for i in range(m)] for j in range(n)]
        max_square = [0]
        
        def findLargestSquare(x: int, y:int) -> int:
            if memo[x][y] != -1:
                return memo[x][y]
            
            down = 0
            if x+1 < n:
                down = findLargestSquare(x+1, y)
                
            right = 0
            if y+1 < m:
                right = findLargestSquare(x, y+1)
                
            botm_right = 0
            if x+1 < n and y+1 < m:
                botm_right = findLargestSquare(x+1, y+1)
                
            memo[x][y] = min(down, right, botm_right) + 1
            if matrix[x][y] == '0':
                memo[x][y] = 0
            max_square[0] = max(max_square[0], (memo[x][y])**2)
            return memo[x][y]
        
        findLargestSquare(0, 0)
        return max_square[0]


    # O(m*n) time,
    # O(m*n) space,
    # Approach: dp, tabulation
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        max_area = 0
        
        table = [ [-1 for i in range(m)] for j in range(n)]
        
        for row in range(n-1, -1, -1):
            for col in range(m-1, -1, -1):
                down = 0
                if row+1 < n:
                    down = table[row+1][col]
                    
                right = 0
                if col+1 < m:
                    right = table[row][col+1]

                botm_right = 0
                if row+1 < n and col+1 < m:
                    botm_right = table[row+1][col+1]
                
                table[row][col] = 0 if matrix[row][col] == '0' else min(down, right, botm_right) + 1
                max_area = max(max_area, (table[row][col])**2)
        
        
        return max_area


