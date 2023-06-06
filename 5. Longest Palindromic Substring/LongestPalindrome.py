'''
https://leetcode.com/problems/longest-palindromic-substring/
'''

class Solution:
        def longestPalindrome(self, s: str):
            n = len(s)
            if n == 1:  return s
            dp = [1] * n
            dp[0], dp[n - 1] = 2 if s[0] == s[1] else 1, 1
            long_pal_str_index = 0
            if n == 2:
                return s[0:dp[0]]

            def findPalindromLenOdd(index: int):
                l, r = index - 1, index + 1
                tot_len = 1
                while l >=0 and r < n:
                    if s[l] != s[r]:    return tot_len
                    tot_len = r - l + 1
                    l -=1
                    r +=1

                return tot_len

            def findPalindromLenEven(index:int):
                l, r = index, index + 1
                tot_len = 0
                while l >= 0 and r < n:
                    if s[l] != s[r]:    return tot_len
                    tot_len = r -l + 1
                    l -=1
                    r +=1

                return tot_len
                    

            for i in range(1, n-1):
                dp[i] = max(findPalindromLenOdd(i), findPalindromLenEven(i))
                long_pal_str_index = i if dp[i] > dp[long_pal_str_index] else long_pal_str_index

            i = long_pal_str_index
            if dp[i] % 2 == 1:  pal_sub_str = s[i - (dp[i] // 2): i + (dp[i]//2)+1]
            else:   pal_sub_str = s[i - (dp[i] // 2) + 1:i + (dp[i] // 2) + 1]
            return pal_sub_str


sol = Solution()
print(sol.longestPalindrome("aaaa"))