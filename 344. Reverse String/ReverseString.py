'''
https://leetcode.com/problems/reverse-string/
'''


class Solution:
    def reverseString(self, s: list[str]) -> None:
        n = len(s)
        l, r = 0, n-1
        
        while l < r:
            if s[l] != s[r]:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
            l +=1
            r -=1