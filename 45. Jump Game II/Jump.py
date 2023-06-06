'''
https://leetcode.com/problems/jump-game-ii/
'''


from typing import List


class Solution:
    # O(n*m) time, m--> the biggest jump in the nums
    # O(1) space,
    # Approach: DP, top bottom,
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        jumps = 0
        
        while i < n-1:
            jump = nums[i]
            jumps +=1
            if i + nums[i] > n-2:
                break
            max_jump_index = i+1
            for j in range(i+2, i+jump+1):
                if nums[j] == 0:    continue
                if j + nums[j] > max_jump_index + nums[max_jump_index]:
                    # print(j)
                    max_jump_index = j
                    
            i = max_jump_index
            
        return jumps