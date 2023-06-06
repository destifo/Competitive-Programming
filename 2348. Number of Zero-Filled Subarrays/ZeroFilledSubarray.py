from typing import List


class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: counting, math, array
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                i += 1
                continue
                
            j = i+1
            
            while j < len(nums) and nums[j] == 0:
                j += 1
                
            size = j-i
            subarrays = (size*(size+1))//2
            ans += (subarrays)
            i = j
            
        return ans