from typing import List


class Solution:
    # O(rows*cols) time,
    # O(rows*cols) space,
    # Approach: dp, tabulation
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        if len(mines) == n**2:
            return 0
        
        rows, cols = n, n
        up = [[1 for i in range(cols)] for j in range(rows)]
        for col in range(cols):
            up[0][col] = 1
        down = [[1 for i in range(cols)] for j in range(rows)]
        for col in range(cols):
            down[-1][col] = 1
            
        left = [[1 for i in range(cols)] for j in range(rows)]
        for row in range(rows):
            left[row][0] = 1
        right = [[1 for i in range(cols)] for j in range(rows)]
        for row in range(rows):
            right[row][-1] = 1
            
        for coord in mines:
            row, col = coord
            up[row][col] = 0
            down[row][col] = 0
            left[row][col] = 0
            right[row][col] = 0
        
        max_order = 1
        for row in range(1, rows-1):
            for col in range(1, cols-1):
                if up[row][col] == 0:   continue
                
                up[row][col] += up[row-1][col]
                left[row][col] += left[row][col-1]
                
        for row in range(rows-2, 0, -1):
            for col in range(cols-2, 0, -1):
                if down[row][col] == 0:   continue
                
                down[row][col] += down[row+1][col]
                right[row][col] += right[row][col+1]
                max_order = max(max_order, min(up[row][col], down[row][col], left[row][col], right[row][col]))
            
        return max_order