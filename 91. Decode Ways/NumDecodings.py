'''
https://leetcode.com/problems/decode-ways/
'''


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: dp,
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range(len(s)+1)]
        dp[len(s)] = 1
        
        def findDecodes(index: int) -> int:
            if dp[index]:
                return dp[index]
            
            if s[index] == '0':
                return 0
            
            tot = findDecodes(index+1)
            if index < len(s) - 1 and int(s[index:index+2]) < 27:
                tot +=findDecodes(index+2)
            dp[index] = tot
            return tot
            
        dp[0] = findDecodes(0)
        
        return dp[0]

    
    # O(n) time,
    # O(n) space,
    # Approach: dp top-down, memoization
    def numDecodings2(self, s: str) -> int:
        n = len(s)
        memo = {}
        
        def findDecodings(index: int) -> int:
            if s[index] == '0':
                return 0
            
            if index in memo:
                return memo[index]
            
            if index == n-1:
                return 1
            
            if index == n-2:
                memo[index] = (1 if int(s[index:]) < 27 else 0) + findDecodings(index+1)
                return memo[index]
            
            memo[index] = findDecodings(index+1) + (findDecodings(index+2) if int(s[index:index+2]) < 27 else 0)
            return memo[index]
        
        return findDecodings(0)

    
    # O(n) time,
    # O(n) space,
    # Approach: dp bottom-up, tabulation
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if len(s) == 1:
            return 1 if s[0] != '0' else 0
        
        table = [0 for i in range(n)]
        table[n-1] = 1 if s[n-1] != '0' else 0
        table[n-2] = (table[n-1] + (1 if int(s[n-2:]) < 27 else 0)) if s[n-2] != '0' else 0
        
        for i in range(n-3, -1, -1):
            one_jump = 0 if s[i] == '0' else table[i+1]
            two_jump = table[i+2] if int(s[i:i+2]) < 27 and s[i] != '0' else 0
            table[i] = one_jump + two_jump
            
        return table[0]


sol = Solution()
print(sol.numDecodings("12"))