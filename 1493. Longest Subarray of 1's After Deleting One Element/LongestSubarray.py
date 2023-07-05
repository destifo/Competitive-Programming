from typing import List


class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: sliding window, 
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        left, right = 0, 0
        k = 1
        
        while right < len(nums):
            if nums[right] == 0:
                if k > 0:
                    k -= 1
                    right += 1
                else:
                    ans = max(ans, right-left-1+k)
                    if nums[left] == 0:
                        k += 1
                    left += 1
            else:
                right += 1
                
        ans = max(ans, right-left-1+k)
        return min(ans, len(nums)-1)