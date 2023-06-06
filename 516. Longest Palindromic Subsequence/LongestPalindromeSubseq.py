class Solution:
    # O(n^2) time,
    # O(n^2) space,
    # Approach: dp, memoization, 
    # Intution: finding the longest common subsequence between a string and its reverse
    def longestPalindromeSubseq(self, s: str) -> int:
        rev_s = s[::-1]
        n = len(s)
        
        memo = {}
        memo[(n-1, n-1)] = 1 if s[-1] == rev_s[-1] else 0
        
        def findLongest(start1: int, start2: int) -> int:
            if start1 == n or start2 == n:
                return 0
            
            if (start1, start2) in memo:
                return memo[(start1, start2)]
            
            if s[start1] == rev_s[start2]:
                memo[(start1, start2)] = 1 + findLongest(start1+1, start2+1)
                return memo[(start1, start2)]
            else:
                right = findLongest(start1, start2+1)
                down = findLongest(start1+1, start2)
                
                memo[(start1, start2)] = max(right, down)
                return memo[(start1, start2)]
            
        return findLongest(0, 0)
    

    def findLongest(self, i: int, j: int, s: str, memo: dict[int]) -> int:
        
        if i >= j:
            return (j-i) + 1
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if s[i] == s[j]:
            memo[(i, j)] = 2 + self.findLongest(i+1, j-1, s, memo)
        else:
            memo[(i, j)] = max(self.findLongest(i+1, j, s, memo), self.findLongest(i, j-1, s, memo))
        
        return memo[(i, j)]
        
    # O(n^2) time,
    # O(n^2) space,
    # Approach: top down dp, memoization
    def longestPalindromeSubseq2(self, s: str) -> int:
        return self.findLongest(0, len(s)-1, s, {})
    

    # O(n^2) time,
    # O(n^2) space,
    # Approach: bottom-up dp, tabulation, 
    def longestPalindromeSubseq3(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
        return dp[0][len(s)-1]