'''
https://leetcode.com/problems/counting-bits/
'''

class Solution:
    def countBits(self, n: int):
        ans = [0] * (n+1)
        for i in range(n+1):
            curr = i
            while curr:
                ans[i] += (curr % 2)
                curr //=2
                
        return ans