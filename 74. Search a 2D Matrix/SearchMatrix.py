'''
https://leetcode.com/problems/search-a-2d-matrix/
'''

from typing import List


class Solution:
    def searchMatrix(self, matrix, target: int):
        m = len(matrix)
        mid_row = m//2
        initial = 0
        ans_row = 0
        final = m - 1
        while final - initial >= 1:
            if matrix[mid_row][0] <= target and matrix[mid_row][-1] >= target:
                ans_row = mid_row
                break
            elif matrix[mid_row][0] > target:
                if (mid_row - 1 > 0) and matrix[mid_row - 1][0] <= target:
                    ans_row = mid_row - 1
                    break
                #elif (mid_row - 1) and matrix[mid_row - 1]
                else:
                    old_mid_row = mid_row
                    mid_row = (mid_row - initial)//2 + initial
                    final = old_mid_row
            else:
                if (mid_row + 1 < m) and matrix[mid_row + 1][0] > target:
                    ans_row = mid_row
                    break
                elif (mid_row + 1 < m) and matrix[mid_row + 1][-1] >= target:
                    ans_row = mid_row + 1
                    break
                else:
                    old_mid_row = mid_row
                    mid_row = (final - initial)//2 + mid_row
                    initial = old_mid_row
       
        print(ans_row)
        nums = matrix[ans_row]
        n = len(matrix[0])
        mid = n//2
        def binarySearch(initial, index, final):
            if final - initial <=1 and (nums[final] != target and nums[initial] != target):
                return False
            if nums[index] == target:
                return True
            elif nums[index] >= target:
                return binarySearch(initial, (index - initial)//2 + initial, index)
            else:
                return binarySearch(index, (final - initial)//2 + index, final)
                
        return binarySearch(0, mid, n - 1)
    
    
    # O(logm + logn) == O(log(m*n)) time
    # O(1) space,
    # Approach: binary search, matrix 
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix)-1
        row_index = len(matrix)
        
        # binary search the row, 
        while lo <= hi:
            mid = (lo+hi)//2
            if matrix[mid][0] > target:
                hi = mid-1
            elif matrix[mid][-1] < target:
                lo = mid+1
            else:
                row_index = mid
                break
        
        if row_index == len(matrix):
            return False

        # binary search the target from the row, 
        lo, hi = 0, len(matrix[row_index])-1
        while lo <= hi:
            mid = (lo+hi)//2
            if matrix[row_index][mid] == target:
                return True
            elif matrix[row_index][mid] > target:
                hi = mid-1
            else:
                lo = mid+1
                
        return False