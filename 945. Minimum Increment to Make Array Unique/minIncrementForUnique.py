'''
https://leetcode.com/problems/minimum-increment-to-make-array-unique/
'''

from collections import Counter


class Solution:
    def minIncrementForUnique(self, nums):
        if not nums:
            return 0

        nums.sort()
        moves = 0
        pre = nums[0]

        for i in range(1, len(nums)):
            cur = nums[i]
            if cur <= pre:
                moves += pre - cur + 1
                cur = pre + 1
            
            pre = cur
        
        return moves        
    

sol = Solution()
print(sol.minIncrementForUnique([3,2,1,2,1,7]))

