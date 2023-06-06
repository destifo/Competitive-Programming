'''
https://leetcode.com/problems/missing-number/
'''


class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            if i != nums[i]:
                return i
            
        return n
