'''
https://leetcode.com/problems/valid-perfect-square/
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def binary_search(start, end):
            mid = (start + end) //2
            if square(mid) == num:    return True
            if start == mid and square(mid) != num:    return False
            if square(mid) < num:
                return binary_search(mid, end)
            else:
                return binary_search(start, mid)
            
        def square(x):
            return x * x
        
        return binary_search(0, num+1)