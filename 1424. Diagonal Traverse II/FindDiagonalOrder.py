from collections import defaultdict
from typing import List


class Solution:
    
    # O(n*m) time,
    # O(n+m) space,
    # Approach: matrix, math
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        '''
        
        [(0, 0), (0, 1), (0, 2), (0, 3)]
        [(1, 0), (1, 1), (1, 2), (1, 3)]
        [(2, 0), (2, 1), (2, 2), (2, 3)]
        [(3, 0), (3, 1), (3, 2), (3, 3)]
        
        first, group by sum
        second, traverse
        
        '''
        
        n = len(nums)
        group = defaultdict(list)
        max_tot = 0
        
        for i in range(n):
            row = nums[i]
            for j in range(len(row)):
                group[i+j].append(nums[i][j])
                max_tot = max(max_tot, i+j)
        
        ans = []
        for i in range(max_tot+1):
            while group[i]:
                ans.append(group[i].pop())
                    
        return ans