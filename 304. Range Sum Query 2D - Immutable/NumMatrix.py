'''
https://leetcode.com/problems/range-sum-query-2d-immutable/
'''

class NumMatrix:
    
    def __init__(self, matrix):
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

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
        regionSum = 0
        for row in range(row1, row2 + 1):
            colSum = self.prefixSum[row][col2 + 1] - self.prefixSum[row][col1]
            regionSum +=  colSum

        return regionSum


sol = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print()