from typing import List


class Solution:
    
    # O(n*m) time,
    # O(n*m) space,
    # Approach: bottom up dp, greedy
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        '''
            the key take here is to store the smallest negative number and largest positive value at each cell,
            then when we can make the smallest negative number a large positive number when multiplied by any negative number which we might return as the maximum positive value
        
        '''
        
        
        MOD = 10**9 + 7
        rows, cols = len(grid), len(grid[0])
        dp = [[[-1, -1] for _ in range(cols)] for _ in range(rows)]
        
        dp[-1][-1][0] = grid[-1][-1]
        dp[-1][-1][1] = grid[-1][-1]
            
        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                if (row, col) == (rows-1, cols-1):
                    continue
                
                max_pos = float('-inf')
                min_neg = float('inf')
                # downwards
                if row + 1 < rows:
                    max_pos = dp[row+1][col][0]
                    min_neg = dp[row+1][col][1]
                    
                # right
                if col + 1 < cols:
                    max_pos = max(max_pos, dp[row][col+1][0])
                    min_neg = min(min_neg, dp[row][col+1][1])
                
                curr_val = grid[row][col]
                if curr_val >= 0:
                    dp[row][col][0] = max_pos*curr_val
                    dp[row][col][1] = min_neg*curr_val
                else:
                    dp[row][col][0] = min_neg*curr_val
                    dp[row][col][1] = max_pos*curr_val

        sign = -1 if dp[0][0][0] < 0 else 1
        ans = abs(dp[0][0][0] if dp[0][0][0] >= 0 else -1) % MOD
        return ans * sign