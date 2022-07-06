'''
https://leetcode.com/problems/power-of-two/
'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        while n > 2:
            if n % 2 != 0:  return False
            n //=2
        
        return True if n > 0 else False