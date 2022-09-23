'''
https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
'''


class Solution:
    # O(m) time, for m sum(len(bin(num))) for 0 < num <= n
    # O(m) space, 
    # Approach: brute force,
    def concatenatedBinary(self, n: int) -> int:
        multiplier = 1
        conctd_str = ""
        result = 0
        
        for num in range(1, n+1):
            conctd_str +=str(bin(num).replace('0b', ""))
        
        MOD = (10 ** 9) + 7
        return int(conctd_str, 2) % MOD