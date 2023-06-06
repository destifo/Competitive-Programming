

from typing import List
import math


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: prefix sum, array
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        
        prefix_sum = [0 for _ in range(n+1)] 
        tot = 0
        
        for index, num in enumerate(nums):
            tot += num
            prefix_sum[index+1] = tot
        
        answer = n
        min_diff = math.inf
        
        for i in range(n):
            left_avg = prefix_sum[i+1] // (i+1)
            right_avg = (prefix_sum[n] - prefix_sum[i+1]) // (n-i-1) if i != n-1 else 0
            
            diff = abs(right_avg-left_avg)
            if diff < min_diff:
                min_diff = diff
                answer = i
                
        return answer