from operator import index
from turtle import left
from typing import List


class Solution:
    #failed
    def minSubArrayLen1(self, target: int, nums):
        index_largest = 0
        for i in range(len(nums)):
            if nums[i] > nums[index_largest]:
                index_largest = i
        
        if nums[index_largest] >= target:
            return 1
        
        tot = nums[index_largest]

        tot_len = 1

        right_index = index_largest
        left_index = index_largest

        while right_index < len(nums) or left_index >= 0:
            right_index += 1
            left_index -= 1
            if (right_index < len(nums) and left_index >= 0):
                tot_len += 1
                tot += max(nums[right_index], nums[left_index])
                if (nums[right_index] > nums[left_index]):
                    left_index -= 1
                else:
                    right_index -= 1

            elif (right_index < len(nums)):
                tot_len += 1
                tot += nums[right_index]
            
            elif (left_index >= 0):
                tot_len += 1
                tot += nums[left_index]

            if (tot >= target):
                return tot_len
            
        return 0
    

    def minSubArrayLen(self, target: int, nums):
        tot, left_index = 0, 0
        min_len = 0
        
        for r in range(len(nums)):
            tot += nums[r]
            while tot >= target:
                if min_len == 0:
                    min_len = r - left_index + 1
                else:    
                    min_len = min(r - left_index + 1, min_len)
                    tot -= nums[left_index]
                    left_index += 1

        return min_len
    
    
    # O(n) time,
    # O(1) space,
    # Approach: sliding window, 
    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        tot = 0
        ans = float('inf')
        
        while right < len(nums):
            tot += nums[right]
            right += 1
            while tot >= target:
                ans = min(ans, right-left)
                tot -= nums[left]
                left += 1
                
        return ans if ans != float('inf') else 0
            





sol = Solution()

print(sol.minSubArrayLen(7,
[2,3,1,2,4,3]))