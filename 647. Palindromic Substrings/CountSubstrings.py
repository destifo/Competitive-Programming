'''
https://leetcode.com/problems/palindromic-substrings/
'''

class Solution:
    def countSubstrings(self, s: str):
        n = len(s)
        ans = 0

        # finding odd length palindromes
        for i in range(1, n - 1):
            l, r = i - 1, i + 1
            while l >= 0 and r < n:
                if s[l] != s[r]:    break
                ans +=1
                l -=1
                r +=1

        # finding even length palindromes
        for i in range(n-1):
            l, r = i, i + 1
            while l >= 0 and r < n:
                if s[l] != s[r]:    break
                ans +=1
                l -=1
                r +=1

        return ans + n # n -> each letter is a palindrome
        

sol = Solution()
print(sol.countSubstrings("baaaaad"))