from typing import List


class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: greedy, 
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)-1):
            if i % 2 == 0 and nums[i+1] < nums[i] or i % 2 == 1 and nums[i+1] > nums[i]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        