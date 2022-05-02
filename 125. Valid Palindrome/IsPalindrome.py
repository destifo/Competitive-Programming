'''
https://leetcode.com/problems/valid-palindrome/
'''

class Solution:
    def isPalindrome(self, s: str):
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if not s[r].isalnum():
                r -=1
                continue
            if not s[l].isalnum():
                l +=1
                continue
            if s[l] != s[r]:
                return False
            l +=1
            r -=1

        return True

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))