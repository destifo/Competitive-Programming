'''
https://leetcode.com/problems/longest-common-subsequence/
'''


class Solution:
    # O(m*n) time,
    # O(m*n) space,
    # Approach: dp, memoization
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        memo = {}
        
        def findCommonSubseq(end1: int, end2: int) -> int:
            if end1 == 0 or end2 == 0:
                return 0
            
            if end1 == 1 and end2 == 1:
                return 1 if text1[end1-1] == text2[end2-1] else 0
            
            if (end1, end2) in memo:
                return memo[(end1, end2)]
            
            if text1[end1-1] == text2[end2-1]:
                memo[(end1, end2)] = 1 + findCommonSubseq(end1-1, end2-1)
                return memo[(end1, end2)]
            
            memo[(end1, end2)] = max(findCommonSubseq(end1-1, end2), findCommonSubseq(end1, end2-1))
            return memo[(end1, end2)]
        
        return findCommonSubseq(n, m)


    # O(m*n) time,
    # O(m*n) space,
    # Approach: dp, tabulation
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        table = [[ 0 for i in range(m+1)] for j in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    table[i][j] = 1 + table[i-1][j-1]
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])
                    
        return table[n][m]