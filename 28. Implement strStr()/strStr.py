'''
https://leetcode.com/problems/implement-strstr/
'''


class Solution:
    # O(n) time complexity as we are going through the string only one time
    # O(1) space, we just used 4 variables to store some data(pointer and int)
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        m = len(haystack)

        if n == 0:  return 0
        
        l, r = 0, n
        while r <= m:
            if haystack[l:r] == needle:
                return l
            l +=1
            r +=1
        
        return -1