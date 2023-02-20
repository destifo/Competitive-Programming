from typing import List


class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: array, math
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        curr_min = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            diff = num-curr_min
            if diff != 0:
                max_diff = max(max_diff, diff)
            curr_min = min(curr_min, num)
            
        return max_diff