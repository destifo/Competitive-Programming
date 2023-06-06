'''
https://leetcode.com/problems/rotate-image/
'''


from typing import List


class Solution:
    # O(n^2) time,
    # O(1) space,
    # Approach: math, matrix
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        def rotateCells(offset: int, boundaries: List[int]) -> None:
            left = boundaries[0]
            right = boundaries[1]
            top = boundaries[2]
            botm = boundaries[3]
            
            temp = matrix[top+offset][right]
            matrix[top+offset][right] = matrix[top][left+offset]
            temp2 = matrix[botm][right-offset]
            matrix[botm][right-offset] = temp
            temp = matrix[botm-offset][left]
            matrix[botm-offset][left] = temp2
            matrix[top][left+offset] = temp
            
        
        top, left = 0, 0
        right, botm = n-1, n-1
        m = n
        while m > 1:
            for i in range(m-1):
                rotateCells(i, [left, right, top, botm])
            
            left +=1
            top +=1
            right -=1
            botm -=1
            m -=2
        

sol = Solution()
print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))