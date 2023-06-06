from typing import List


class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: math, 
    def minMoves(self, nums: List[int]) -> int:
        min_moves = 0
        
        min_val = min(nums)
        
        for num in nums:
            min_moves += num-min_val
            
        return min_moves

    
    # O(n) time,
    # O(1) space,
    # Approach: math, 
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - (min(nums)*len(nums))