from typing import List


class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: array, 
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
                
        for i in range(len(nums)):
            num = nums[i]
            pos = abs(num)-1
            if pos >= len(nums) or num == 0:
                continue
            new_val = -abs(nums[pos])
            if new_val == 0:
                nums[pos] = -(pos+1)
            else:
                nums[pos] = new_val

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
            
        return len(nums)+1