'''
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
'''

class Solution:
    def numberOfSubstrings(self, s: str):
        n = len(s)
        ans = 0
        if n < 3:
            return ans
        
        abcList = ['a', 'b', 'c']
        charmap = dict()
        for i in range(3):
            if s[i] in abcList:
                charmap[s[i]] = 1
        l, r = 0, 2
        while l < n - 2:
            isAllPresent = True
            for char in abcList:
                if charmap[char] < 1:
                    isAllPresent = False
                    break

            if not isAllPresent:
                r +=1
                if r == n:  break
                ch = s[r]
                if ch in abcList:
                    charmap[ch] = charmap.get(ch, 0) + 1
                continue

            currSum = n - r
            ans += currSum
            ch = s[l]
            if ch in abcList:
                charmap[ch] = charmap[ch] - 1
            l +=1

        return ans


    # O(n) time,
    # O(1) space,
    # Approach: two pointers, hashable
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        window = {}
        l, r = 0, 0
        
        while len(window) < 3 and r < n:
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1
            r +=1
            
        ans = 0
        
        while r <= n:
            if len(window) == 3:
                ans += (n-r+1)
                ch = s[l]
                window[ch] -=1
                if window[ch] == 0:
                    window.pop(ch)
                l +=1
            else:
                if r == n: break
                ch = s[r]
                window[ch] = window.get(ch, 0) + 1
                r +=1
                
        return ans

                
sol = Solution()
print(sol.numberOfSubstrings("abcabc"))  