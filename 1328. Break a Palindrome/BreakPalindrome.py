'''
https://leetcode.com/problems/break-a-palindrome/
'''


class Solution:
    # O(n) time, n//2 to be precise
    # O(n) space, for the new str we create
    # Approach: greedy,
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ''
        
        mid = n // 2
        for i in range(mid):
            if palindrome[i] == 'a':    continue
            res = palindrome[:i] + 'a' + palindrome[i+1:n]
            return res
        
        res = palindrome[:n-1] + 'b'
        return res