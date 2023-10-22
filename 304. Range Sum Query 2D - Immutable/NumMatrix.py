'''
https://leetcode.com/problems/range-sum-query-2d-immutable/
'''

from typing import List


class NumMatrix:
    # O(rows*cols) time,
    # O(rows*cols) space,
    # Approach: prefix sum
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        self.prefixSum = []

        for i in range(n):
            m = len(matrix[i])
            rowPrefix = [0] * (m + 1)
            currSum = 0
            for j in range(m):
                currSum += matrix[i][j]
                rowPrefix[j + 1] = currSum
            self.prefixSum.append(rowPrefix) 

    # O(row2-row1) time,
    # O(1) space,
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
        regionSum = 0
        for row in range(row1, row2 + 1):
            colSum = self.prefixSum[row][col2 + 1] - self.prefixSum[row][col1]
            regionSum +=  colSum

        return regionSum


class NumMatrix2:
    # O(rows*cols) time,
    # O(rows*cols) space,
    # Approach: prefix sum, 
    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefixSum = [ [ matrix[i][j] for j in range(cols)] for i in range(rows)]
        pfx = self.prefixSum
        # print(pfx)
                
        for row in range(1, rows):
            pfx[row][0] += pfx[row-1][0]
            
        for col in range(1, cols):
            pfx[0][col] += pfx[0][col-1]
            
        for row in range(1, rows):
            for col in range(1, cols):
                pfx[row][col] += (pfx[row][col-1] + pfx[row-1][col] - pfx[row-1][col-1]) 
        # print(pfx)

    
    # O(1) time,
    # O(1) space,
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
        pfx = self.prefixSum
        left = pfx[row2][col1-1] if col1 != 0 else 0
        top = pfx[row1-1][col2] if row1 != 0 else 0
        top_left = 0 if (row1 == 0 or col1 == 0) else pfx[row1-1][col1-1]
        region_sum = (pfx[row2][col2] - top - left + top_left) 
        return region_sum



sol = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print()


class NumMatrix2:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.pf_sum = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        pf_sum = self.pf_sum
        
        for row in range(ROWS):
            for col in range(COLS):
                pf_sum[row][col] += matrix[row][col]
                if row > 0:
                    pf_sum[row][col] += pf_sum[row-1][col]
                if col > 0:
                    pf_sum[row][col] += pf_sum[row][col-1]
                if row > 0 and col > 0:
                    pf_sum[row][col] -= pf_sum[row-1][col-1]
                    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pf_sum[row2][col2] + (self.pf_sum[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0) - (self.pf_sum[row1-1][col2] if row1 > 0 else 0) - (self.pf_sum[row2][col1-1] if col1 > 0 else 0)