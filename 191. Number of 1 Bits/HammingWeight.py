'''
https://leetcode.com/problems/number-of-1-bits/
'''

class Solution:
    # by shifting bits to the right once at a time a modding them to find out if it's one or 0
    def hammingWeight(self, n: int):
        count = 0
        while n != 0:
            if n % 2 == 1:  count +=1 # or count += n % 2
            n //=2 # or n = n >> 1 shift to the right once

        return count 


    # we only iterate to the number of ones in the binary string, by using logical % with one of the one bits removed from the string each time
    def hammingWeight2(self, n: int):
        count = 0
        while n:
            n = n & (n - 1)
            count +=1

        return count