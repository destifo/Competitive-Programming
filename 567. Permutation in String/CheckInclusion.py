'''
https://leetcode.com/problems/permutation-in-string/
'''


from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1_count = Counter(s1)
        l, r = 0, n-1
        while r < len(s2):
            if s1_count == Counter(s2[l:r+1]):
                return True
            l +=1
            r +=1 
        return False


sol = Solution()
print(sol.checkInclusion('ab', 'beac'))