'''
https://leetcode.com/problems/remove-palindromic-subsequences/
'''

class Solution:
    def removePalindromeSub(self, s: str):
        n = len(s)
        pali_count = []
        
        for i in range(n):
            l, r = i-1, i+1
            odd_len = 1
            while l >= 0 and r < n and s[l] == s[r]:
                odd_len +=2
                l -=1
                r +=1
                
            even_len = 0
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                even_len +=2
                l -=1
                r +=1
            
            max_len = max(odd_len, even_len)
            pali_count.append(max_len)
            
        pali_count.sort(reverse=True)
        rem_num = 0
        for count in pali_count:
            if n == 0:  return rem_num
            if count <= n:
                rem_num +=1
                n -=count

        return rem_num
            

sol = Solution()
print(sol.removePalindromeSub("ababbbaaba"))         