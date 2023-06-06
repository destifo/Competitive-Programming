'''
https://leetcode.com/problems/consecutive-characters/
'''


class Solution:
    # O(n) time,
    # O(1) space,
    # approach: two pointer, sliding window
    def maxPower(self, s: str) -> int:
        n = len(s)
        power = 0
        
        l, r = 0, 0
        curr_pow = 0
        while r < n:
            if s[l] == s[r]:
                curr_pow +=1
            else:
                l = r
                curr_pow = 1
            
            power = max(curr_pow, power)
            r +=1
            
        return power


sol = Solution()
print(sol.maxPower("ccbccbb"))