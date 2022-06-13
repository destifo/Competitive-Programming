'''
https://leetcode.com/problems/decoded-string-at-index/
'''


class Solution:
    def decodeAtIndex(self, s: str, k: int):
        decoded_size = 0
        n = len(s)

        for char in s:
            if char.isdigit():
                decoded_size *=int(char)
            else:
                decoded_size +=1
        
        for i in range(n-1, -1, -1):
            char = s[i]
            k %=decoded_size
            if char.isalpha():
                if k == 0:  return char
                decoded_size -=1
            else:
                decoded_size //=int(char)

        return -1
            