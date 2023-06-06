'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
'''
class Solution:
    # typical sliding window
    def lengthOfLongestSubstring(self, s: str):
        visitedChar = set()
        visitedChar.add(s[0])
        l = 0
        n = len(s)
        maxSubStr = 1
        for r in range(1, n):
            while s[r] in visitedChar:
                visitedChar.remove(s[l])
                l +=1
            
            if s[r] not in visitedChar:
                visitedChar.add(s[r])

            maxSubStr = max(maxSubStr, r - l + 1)

        return maxSubStr
        
        