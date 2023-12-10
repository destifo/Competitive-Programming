from typing import List


class Solution:
    def transpose(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        result = [[0] * m for i in range(n)]
        
        for i in range(m):
            for j in range(n):
                num = matrix[i][j]
                result[j][i] = num
                
        return result
    
    
    def rotate(self, matrix: List[List[int]]) -> None:
        
        for row in range(len(matrix)):
            for col in range(row+1, len(matrix)):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    
    
    # O(n*m) time,
    # O(n*m) space,
    # Approach: matrix, 
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        if ROWS == COLS:
            self.rotate(matrix)
            return matrix
        
        ans = [[0 for _ in range(ROWS)] for _ in range(COLS)]
        for row in range(ROWS):
            for col in range(COLS):
                ans[col][row] = matrix[row][col]
            
        return ans


sol = Solution()
print(sol.transpose([[1,2,3], [4,5,6]]))