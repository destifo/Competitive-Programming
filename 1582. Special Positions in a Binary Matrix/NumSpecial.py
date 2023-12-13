from collections import Counter, defaultdict
from typing import List


class Solution:    
    
    
    # O(n*m) time,
    # O(n*m) space,
    # Approach: hash map, couting
    def numSpecial(self, mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        rows = [defaultdict(int) for _ in range(ROWS)]
        cols = [defaultdict(int) for _ in range(COLS)]
        
        for i in range(ROWS):
            rows[i] = Counter(mat[i])
            for j in range(COLS):
                val = mat[i][j]
                cols[j][val] += 1
        
        ans = 0
        for i in range(ROWS):
            for j in range(COLS):
                val = mat[i][j]
                if rows[i][val] == 1 and cols[j][val] == 1:
                    ans += 1
                    
        return ans