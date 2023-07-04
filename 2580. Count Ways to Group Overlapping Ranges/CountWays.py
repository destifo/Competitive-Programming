from typing import List


class Solution:
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: math, sorting, 
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        groups = 1
        prev_max = ranges[0][1]
        
        for i in range(1, len(ranges)):
            curr_range = ranges[i]
            
            if prev_max < curr_range[0]:
                groups += 1
            prev_max = max(prev_max, curr_range[1])
        
        ans = 2**groups
        ans %= 10**9 + 7
        return ans