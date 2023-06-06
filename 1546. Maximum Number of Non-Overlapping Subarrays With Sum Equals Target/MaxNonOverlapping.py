from collections import defaultdict
from typing import List


class Solution:
    
    
    # O(n) time,
    # O(n) space,
    # Approach: prefix sum, hashtable, 
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix_sum = defaultdict(list)
        prefix_sum[0].append(-1)
        last_used = -1
        tot = 0
        ans = 0
        
        for i, num in enumerate(nums):
            tot += num
            value = tot-target
            
            if value in prefix_sum and prefix_sum[value]:
                index = prefix_sum[value].pop()
                if index < last_used:
                    prefix_sum[value] = []
                else:
                    ans += 1
                    last_used = i
            
            prefix_sum[tot].append(i)
        return ans