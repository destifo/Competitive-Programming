from typing import Dict, List, Tuple


class Solution:
    
    def findMin(self, index: int, rem: int, nums: List[int], memo: Dict[Tuple[int], int]) -> int:
        
        if index == len(nums) and rem == 0:
            return 0
        
        if index == len(nums) or rem == 0:
            return float('inf')
        
        state = (index, rem)
        if state in memo:
            return memo[state]
        
        maxx = float('-inf')
        minn = float('inf')
        
        for i in range(index, len(nums)):
            maxx = max(maxx, nums[i])
            score = maxx + self.findMin(i+1, rem-1, nums, memo)
            minn = min(minn, score)
        
        memo[state] = minn
        return minn
            
    
    
    # O(n*n*d) time,
    # O(n*n*d) space,
    # Approach: top down dp, 
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        ans = self.findMin(0, d, jobDifficulty, {})
        return ans if ans != float('inf') else -1
    
    
    # O(n*n*d) time,
    # O(n*d) space,
    # Approach: bottom up dp, 
    def minDifficulty2(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        dp = [[float('inf') for _ in range(d+1)] for _ in range(n+1)]
        dp[n][d] = 0
        
        for i in range(n-1, -1, -1):
            for j in range(d):
                maxx = float('-inf')
                for k in range(i, n):
                    maxx = max(maxx, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], maxx + dp[k+1][j+1])

        return dp[0][0] if dp[0][0] != float('inf') else -1