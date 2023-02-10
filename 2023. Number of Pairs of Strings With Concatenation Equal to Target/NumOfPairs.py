from typing import List


class Solution:    
    
    # O(len(nums)^2) time,
    # O(len(nums)^2) space,
    # Approach: string, 
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ans = 0
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                if nums[i] + nums[j] == target:
                    ans += 1
                    
        return ans