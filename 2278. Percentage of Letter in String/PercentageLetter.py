'''
https://leetcode.com/problems/percentage-of-letter-in-string/
'''

class Solution:
    def percentageLetter(self, s: str, letter: str):
        n = len(s)
        ans = 0
        
        for char in s:
            if char == letter:  ans+=1
        
        return (100 * ans) // n