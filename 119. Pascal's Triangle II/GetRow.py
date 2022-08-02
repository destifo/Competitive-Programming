'''
https://leetcode.com/problems/pascals-triangle-ii/
'''


from typing import List


class Solution:
    # O(rowIndex) time,
    # O(rowIndex ^ 2) space, 
    # Approach: Top down dp,
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [[1 for i in range(j+1)] for j in range(rowIndex+1)]
        
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                rows[i][j] = rows[i-1][j-1] + rows[i-1][j]
                        
        return rows[rowIndex]