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


sol = Solution()
print(sol.numDecodings("12"))