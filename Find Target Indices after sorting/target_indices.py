"""
https://leetcode.com/problems/find-target-indices-after-sorting-array/
"""
#most peculiar solution that came to me and worked the first time

class Solution:
    def targetIndices(self, nums, target: int):
        target_indices = list()
        total_index = 0
        count_sort_list = [0] * 101
        for i in range(len(nums)):
            count_sort_list[nums[i]] +=1
        for i in range(target):
            total_index += count_sort_list[i]
        for i in range(count_sort_list[target]):
            target_indices.append(total_index + i)
        return target_indices

sol = Solution()
print(sol.targetIndices([1,2,5,2,3], 5))