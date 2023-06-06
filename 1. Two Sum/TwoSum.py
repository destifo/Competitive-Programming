from collections import Counter


class Solution:
    def twoSum(self, nums, target: int):
        n = len(nums)
        nums_dict = dict()
        for i in range(n):
            nums_dict[nums[i]] = i
        
        for i in range(n):
            value = target - nums[i]
            if value in nums_dict.keys() and nums_dict[value] != i:
                result = [i, nums_dict[value]]
                return result

    def twoSum2(self, nums, target: int):
        # optimal
        n = len(nums)
        nums_dict = dict()
        for i in range(n):
            num = nums[i]
            value = target - num
            if value in nums_dict.keys():
                return ([nums_dict[value], i])
            nums_dict[nums[i]] = i


sol = Solution()
print(sol.twoSum([2,5,5,11],10))