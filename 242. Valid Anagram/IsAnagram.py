'''
https://leetcode.com/problems/valid-anagram/
'''

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        charMap = dict()
        for ch in s:
            charMap[ch] = charMap.get(ch, 0) + 1

        for ch in t:
            if ch not in charMap:
                return False

            freq = charMap.get(ch)
            if freq == 1:
                charMap.pop(ch)
            else:
                charMap[ch] = freq - 1

        return False if charMap else True

    def isAnagram2(self, s: str, t: str):
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    def isAnagram3(self, s: str, t: str):
        if len(s) != len(t):
            return False
            
        return Counter(s) == Counter(t)