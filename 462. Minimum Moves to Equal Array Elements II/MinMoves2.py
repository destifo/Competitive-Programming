from typing import List


class Solution:
    # O(n) time,
    # O(1) space, 
    # Approach: array, sorting, math --> change all the nums to the median
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        
        mid = len(nums) // 2
        median = nums[mid]
        moves = 0
        
        for num in nums:
            moves += abs(num-median)
            
        return moves