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

    
    # the same implementation, slightly different
    def moveZeroes2(self, nums: list[int]) -> None:
        n = len(nums)
        l, r = 0, 1
        
        while r < n:
            if nums[l] != 0:
                l +=1
            else:
                if nums[r] != 0:
                    nums[l] = nums[r]
                    nums[r] = 0
                    l +=1
            r +=1