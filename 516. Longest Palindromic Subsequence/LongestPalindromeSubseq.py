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