'''
https://leetcode.com/problems/pascals-triangle/
'''


from typing import List


class Solution:
    # O(rowIndex) time,
    # O(rowIndex ^2) space, specifically rowIndex/2 * (rowIndex + 1),
    # Approach: top down dp,
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1 for i in range(j+1)] for j in range(numRows)]
        
        for i in range(2, numRows):
            for j in range(1, i):
                rows[i][j] = rows[i-1][j-1] + rows[i-1][j]
                
        return rows