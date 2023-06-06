from typing import List


class Solution:
    # O(nlogm) time, n --> number of rows, m --> the longest col
    # O(1) space,
    # Approach: binary search,
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tot = 0
        
        
        def findFirstNegativeIndex(start, end, lst) -> int:
            mid = (start + end)//2
            num = lst[mid]
            
            if num < 0 and (mid == 0 or lst[mid-1] >= 0):
                return mid
            if start >= end-1:
                if lst[end] < 0:
                    return end
                return end+1
            if num >= 0:
                return findFirstNegativeIndex(mid, end, lst)
            else:
                return findFirstNegativeIndex(start, mid, lst)
                
        
        for rowNum in range(n):
            row = grid[rowNum]
            m = len(row)
            index = findFirstNegativeIndex(0, m-1, row)
            tot += (m-index)
            
        return tot