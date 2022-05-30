'''
https://leetcode.com/problems/subsets-ii/
'''

class Solution:
    def subsetsWithDup(self, nums):
        n = len(nums)
        nums.sort()
        ans = []
        def findSubset(index, curr_list):
            if index == n:
                ans.append(curr_list.copy())
                return
            curr_list.append(nums[index])
            findSubset(index + 1, curr_list)
            curr_list.pop()
            while index + 1 < n and nums[index] == nums[index + 1]:
                index += 1
                
            findSubset(index + 1, curr_list)
            
        findSubset(0, [])

        return ans