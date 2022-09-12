class Solution:
    # O(n^2) time,
    # O(n) space,
    # Approach: dp, memoization
    def numTrees(self, n: int) -> int:
        memo = {}

        def findTotalTrees(m: int) -> int:
            if m < 3:
                return max(m, 1)

            if m in memo:
                return memo[m]
            
            tot = 0
            for i in range(m):
                left_side = m-i-1
                right_side = i
                tot += findTotalTrees(left_side) * findTotalTrees(right_side)
                
            memo[m] = tot
            return tot
        
        return findTotalTrees(n)

    
    # O(n^2) time,
    # O(n) space,
    # Approach: dp, tabulation
    def numTrees(self, n: int) -> int:
        if n < 3:
            return n
        
        dp = [0 for i in range(n+1)]
        dp[0], dp[1] = 1, 1
        dp[2] = 2
        
        for i in range(3, n+1):
            for j in range(i):
                left_side = i-j-1
                right_side = j
                dp[i] += dp[left_side] * dp[right_side]
                
        return dp[n]


sol = Solution()
print(sol.numTrees(3))