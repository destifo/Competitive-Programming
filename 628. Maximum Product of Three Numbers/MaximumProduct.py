'''
https://leetcode.com/problems/maximum-product-of-three-numbers/
'''

import math


class Solution:
    # for +ve nums only
    def maximumProduct(self, nums):
        maxList = [float('-inf'), float('-inf'), float('-inf')]
    
        def appendMax(val):
            if val > maxList[0]:
                maxList[2] = maxList[1]
                maxList[1] = maxList[0]
                maxList[0] = val
                
            elif val > maxList[1]:
                maxList[2] = maxList[1]
                maxList[1] = val
                
            elif val > maxList[2]:
                maxList[2] = val
                
            
        for num in nums:
            appendMax(num)
            
        return math.prod(maxList)

    
    # both for +ves and negatives
    def maximumProduct2(self, nums):
        nums.sort()
        n = len(nums)
        
        return max(
            nums[0] * nums[1] * nums[n - 1],
            nums[n - 1] * nums[n - 2] * nums[n - 3]
        )