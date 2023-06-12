from typing import List


class Solution:
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: brain teaser, prefix sum, 
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        for i, num in enumerate(nums):
            nums[i] += (-1 if s[i] == 'L' else 1) * d
            
        nums.sort()
        ans = 0
        prefix = 0
        MOD = 10**9 + 7
        for i, num in enumerate(nums):
            diff = i*num-prefix
            ans += diff
            ans %= MOD
            prefix += num
            
        return ans