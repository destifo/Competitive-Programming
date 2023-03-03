'''
https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
'''


from typing import List


class Solution:
    # O(m^2) time,
    # O(m^2) space,
    # Approach: dp, memoization -- > gives TLE becuase it's python
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        memo = {}
        
        def calcMaxPoints(lo: int, hi: int, mult_index: int) -> int:
            
            if mult_index == m-1:
                return max(nums[lo] * multipliers[mult_index], nums[hi] * multipliers[mult_index])
            
            if (lo, hi) in memo:
                return memo[(lo, hi)]
            
            chose_left = nums[lo] * multipliers[mult_index] + calcMaxPoints(lo+1, hi, mult_index+1)
            chose_right = nums[hi] * multipliers[mult_index] + calcMaxPoints(lo, hi-1, mult_index+1)
            
            memo[(lo, hi)] = max(chose_left, chose_right)
            return max(chose_left, chose_right)
        
        return calcMaxPoints(0, len(nums)-1, 0)