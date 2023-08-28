from typing import Dict, List


class Solution:
    
    def maxJumps(self, i: int, nums: List[int], target: int, memo: Dict[int, int]) -> int:
        
        if i == len(nums)-1:
            return 0
        
        if i in memo:
            return memo[i]
        
        max_jumps = -1
        for j in range(i+1, len(nums)):
            if abs(nums[i]-nums[j]) <= target:
                jumps = self.maxJumps(j, nums, target, memo)
                if jumps != -1:
                    max_jumps = max(max_jumps, jumps+1)
        
        memo[i] = max_jumps
        return max_jumps
    
    
    # O(n^2) time,
    # O(n) space,
    # Approach: top down dp, 
    def maximumJumps(self, nums: List[int], target: int) -> int:
        return self.maxJumps(0, nums, target, {})