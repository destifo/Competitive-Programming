'''
https://leetcode.com/problems/is-subsequence/
'''


class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: two pointers, 
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        
        i, j = 0, 0
        
        if n > m:
            return False
        
        while i < n and j < m:
            if s[i] == t[j]:
                i +=1
                
            j +=1
            
        if i < n:
            return False
        
        return True