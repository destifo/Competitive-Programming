'''
https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/
'''


"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

from typing import List


class Solution:
    # O(nlogn) time, where n is the domain width
    # O(m) space, where m is the length of.
    # Approach: binary search,
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        solutionSet = []
        x_limit = 1000
        y_limit = 1000
        
        def findPossibleYGivenX(start, end, x) -> None:
            mid = (start + end)//2
            output = customfunction.f(x, mid)
            if output == z:
                solutionSet.append([x, mid])
                curr = mid - 1
                while customfunction.f(x, curr) == z:
                    solutionSet.append([x, curr])
                    curr -=1
                
                curr = mid + 1
                while customfunction.f(x, curr) == z:
                    solutionSet.append([x, curr])
                    curr +=1
                return
            elif start == end-1:
                if customfunction.f(x, end) != z:
                    return
                solutionSet.append([x, end])
            elif output < z:
                findPossibleYGivenX(mid, end, x)
            elif output > z:
                findPossibleYGivenX(start, mid, x)
                
        
        for x in range(1, x_limit+1):
            findPossibleYGivenX(1, y_limit, x)
            
        return solutionSet