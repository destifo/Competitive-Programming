'''
https://leetcode.com/problems/search-a-2d-matrix/
'''

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