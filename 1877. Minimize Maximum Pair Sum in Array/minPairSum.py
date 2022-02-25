'''
https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
'''

class Solution:
    #on a roll today, 3 streaks of success on the 1st try
    def minPairSum(self, nums) -> int:
        nums.sort()
        max_pair_sum = 0

        while len(nums) > 0:
            max_pair_sum = max(max_pair_sum, nums[0] + nums[-1])
            nums.pop(0)
            nums.pop(-1)
        
        return max_pair_sum


sol = Solution()
print(sol.minPairSum([3,5,4,2,4,6]))
