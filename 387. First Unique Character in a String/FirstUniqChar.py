'''
https://leetcode.com/problems/first-unique-character-in-a-string/
'''


from collections import Counter


class Solution:
    def firstUniqChar(self, s: str):
        char_count = Counter(s)
        
        for index, ch in enumerate(s):
            if char_count[ch] == 1: return index
            
        return -1