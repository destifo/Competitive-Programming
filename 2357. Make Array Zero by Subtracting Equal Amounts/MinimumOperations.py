from typing import List


class Solution:
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: greedy, sorting, 
    def minimumOperations(self, nums: List[int]) -> int:
        total_substracted = 0
        nums.sort()
        ops = 0
        
        for num in nums:
            if num <= total_substracted:    continue
            
            total_substracted += (num-total_substracted)
            ops += 1
            
        return ops