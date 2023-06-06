'''
https://leetcode.com/problems/sort-the-matrix-diagonally/
'''


import heapq
from typing import List


class Solution:
    # O(n*m) time,
    # O(n*m) space,
    # Approach: heap, 
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        diagonals = {}
        
        for i in range(n):
            for j in range(m):
                diff = i-j
                if diff not in diagonals.keys():
                    diagonals[diff] = []
                heapq.heappush(diagonals[diff], mat[i][j])
                
        
        for i in range(n):
            for j in range(m):
                diff = i-j
                mat[i][j] = heapq.heappop(diagonals[diff])
                
        return mat