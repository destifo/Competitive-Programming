from typing import List


class Solution:
    
    # O(n^2 * m) time,
    # O(n*m) space,
    # Approach: prefix sum, hashmap
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        prefix = [[0 for _ in range(COLS+1)] for _ in range(ROWS+1)]
        
        for row in range(1, ROWS+1):
            for col in range(1, COLS+1):
                prefix[row][col] = matrix[row-1][col-1] + prefix[row-1][col] + prefix[row][col-1] - prefix[row-1][col-1]
                
        
        def getSubMatrixSum(r1: int, r2: int, c1: int, c2: int) -> int:
            return prefix[r2][c2] - prefix[r2][c1-1] - prefix[r1-1][c2] + prefix[r1-1][c1-1]
        
        ans = 0
        for r1 in range(1, ROWS+1):
            for r2 in range(r1, ROWS+1):
                cache = {0: 1}
                
                for c in range(1, COLS+1):
                    curr = getSubMatrixSum(r1, r2, 1, c)
                    ans += cache.get(curr-target, 0)
                    cache[curr] = cache.get(curr, 0) + 1
            
        return ans