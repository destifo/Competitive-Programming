'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:   return
        l, r = 0, 1
        
        while r < n:
            if nums[l] == nums[r]:
                r +=1
            elif nums[l] != nums[r]:
                nums[l+1] = nums[r]
                l +=1
        
        return l+1