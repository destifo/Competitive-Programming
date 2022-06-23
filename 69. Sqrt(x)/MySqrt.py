'''
https://leetcode.com/problems/sqrtx/
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        
        def binary_search(start, end):
            mid = (start + end) //2
            if square(mid) == x:    return mid
            if start == mid:    return mid
            if square(mid) < x:
                return binary_search(mid, end)
            else:
                return binary_search(start, mid)
            
        def square(x):
            return x * x
        
        return binary_search(0, x+1)