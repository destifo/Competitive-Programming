'''
https://leetcode.com/problems/divide-two-integers/
'''

class Solution:
    # O(logn) time,
    # O(1) space,
    # Approach: bit manipulation
    def divide(self, dividend: int, divisor: int) -> int:
        
        quotient = 0
        
        sign = 1
        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
            sign = -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        while (dividend-divisor) >= 0:
            
            shift = 0
            while (dividend - (divisor <<1<<shift) >= 0):
                shift += 1
                
            quotient += 1<<shift
            dividend -= divisor<<shift
            
        if sign < 0:
            quotient = -quotient
        
        INT_MAX = (2**31) - 1
        INT_MIN = -(2**31)
        # print(INT_MAX)
        if quotient > INT_MAX:
            return INT_MAX
        
        if quotient < INT_MIN:
            return INT_MIN
            
        return quotient