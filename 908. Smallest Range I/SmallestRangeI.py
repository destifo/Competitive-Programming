'''
https://leetcode.com/problems/smallest-range-i/
'''


from typing import List


class Solution:
    # O(n) time, 
    # O(1) space,
    # Approach: math, array
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_val = nums[0]
        max_val = nums[0]
        
        for num in nums:
            min_val = min(min_val, num)
            max_val = max(max_val, num)
            
        if min_val +k >= max_val -k:
            return 0
        return (max_val - k) - (min_val + k)