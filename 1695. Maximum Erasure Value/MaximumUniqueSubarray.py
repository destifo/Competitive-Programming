'''
https://leetcode.com/problems/maximum-erasure-value/
'''


class Solution:
    def maximumUniqueSubarray(self, nums:list):
        n = len(nums)
        if n == 1:
            return nums[0]

        l, r = 0, 1
        subarray = set()
        subarray.add(nums[0])
        curr_tot = nums[0]
        max_tot = 0
        while r < n:
            num = nums[r]
            while num in subarray:
                curr_tot -=nums[l]
                subarray.remove(nums[l])
                l +=1
            
            curr_tot +=num
            subarray.add(num)
            r +=1
            max_tot = max(max_tot, curr_tot)

        return max_tot