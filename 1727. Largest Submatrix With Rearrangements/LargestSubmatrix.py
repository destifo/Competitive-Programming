from typing import List


class Solution:
    
    # O(n*mlogm) time,
    # O(n*m) space,
    # Approach: prefix, sorting
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        '''
        0 1 1       1 1 0
        0 0 1   =>  1 0 0
        0 1 0       0 1 0
        
        '''
        
        rows, cols = len(matrix), len(matrix[0])
        prefix = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for col in range(cols):
            tot = 0
            for row in range(rows):
                if matrix[row][col] == 1:
                    tot += 1
                else:
                    tot = 0
                prefix[row][col] = tot
        
        
        ans = 0
        for row in prefix:
            row.sort(reverse=True)
            for width, height in enumerate(row):
                if height == 0:
                    break
                area = (width+1)*height
                ans = max(ans, area)
            
        return ans