'''
https://leetcode.com/problems/min-max-game/
'''


import math
from typing import List


class Solution:
    # O(logn) time,
    # O(logn) space,
    # Approach: iteration, simulation
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        while len(nums) > 1:
            new_len = len(nums)//2
            new_lst = [0 for i in range(new_len)]
            for i in range(new_len):
                if i % 2 == 0:
                    new_lst[i] = min(nums[2*i], nums[2*i + 1])
                else:
                    new_lst[i] = max(nums[2*i], nums[2*i + 1])
                    
            nums = new_lst
            
        return nums[0]


    # O(logn) time,
    # O(1) space,
    # Approach: iterative, simulation
    def minMaxGame2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        m = int(math.log(n, 2))
        
        interval = 1
        for j in range(m):
            count = 0
            for i in range(0, n, 2 * interval):
                if count % 2 == 0:
                    nums[i] = min(nums[i], nums[i + interval])
                else:
                    nums[i] = max(nums[i], nums[i + interval])
                count +=1
            interval *=2
            # n //=2
        
              
        return nums[0]