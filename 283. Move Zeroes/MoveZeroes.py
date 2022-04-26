'''
https://leetcode.com/problems/move-zeroes/
'''
class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        l = 0
        for r in range(1, n):
            if l < n and nums[l] != 0:
                l +=1
                continue
            
            if nums[l] == 0 and nums[r] != 0:
                temp = nums[r]
                nums[r] = 0
                nums[l] = temp
                l +=1