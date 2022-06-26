'''
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
'''


import heapq


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        row, col = 0, 0
        
        while row < n:
            val = matrix[row][col]
            coord = (row, col)
            elt = (val, coord)
            heapq.heappush(min_heap, elt)
            row +=1
            
        result = None
        for i in range(k):
            result, coord = heapq.heappop(min_heap)
            row, col = coord
            if col < n -1:
                new_elt = (matrix[row][col+1], (row, col+1))
                heapq.heappush(min_heap, new_elt)
        
        return result