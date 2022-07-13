'''
https://leetcode.com/problems/sum-of-subarray-ranges/
'''


class Solution:
    # O(n^2) time,
    # O(1) space
    def subArrayRanges(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        
        for i in range(n):
            minm = nums[i]
            maxm = nums[i]
            for j in range(i, n):
                minm = min(minm, nums[j])
                maxm = max(maxm, nums[j])
                ans +=(maxm-minm)
                
        return ans