from typing import List


class Solution:
    
    def binarySearch(self, row: List[int], target: int) -> int:
        lo, hi = 0, len(row)-1
        
        while lo <= hi:
            mid = (lo+hi)//2
            if row[mid] == target:
                return mid
            elif row[mid] > target:
                hi = mid-1
            else:
                lo = mid+1
        
        return -1
    
    
    # O(nlogm) time,
    # O(1) space,
    # Approach: binary search, 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        
        for row in range(n):
            for col in range(m):
                if matrix[row][0] > target or matrix[row][-1] < target:
                    continue
                if self.binarySearch(matrix[row], target) != -1:
                    return True
        
        return False
    
    
    # O(n+m) time,
    # O(1) space,
    # Approach: two pointers, 
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        i, j = 0, m-1
        
        while i < n and j >= 0:
            if matrix[i][j] == target:
                return True
            elif j-1 >= 0 and matrix[i][j-1] < target:
                i += 1
            else:
                if j-1 < 0:
                    i += 1
                else:
                    j -= 1
        
        return False
    

    # O(n+m) time,
    # O(1) space,
    # Approach: binary search, 
    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        row, col = 0, m-1
        
        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        
        return False