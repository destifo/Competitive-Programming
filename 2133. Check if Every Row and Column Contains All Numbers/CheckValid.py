'''
https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/
'''


class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = len(matrix)
        row = [set() for i in range(n)]
        col = [set() for i in range(n)]
        
        for i in range(n):
            for j in range(n):
                cell = matrix[i][j]
                row[i].add(cell)
                col[j].add(cell)
            if len(row[i]) < n: return False
        for i in range(n):
            if len(col[i]) < n: return False
        
        return True