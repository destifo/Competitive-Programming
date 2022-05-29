'''
https://leetcode.com/problems/subsets/
'''

class Solution:
    def subsets(self, nums):
        n = len(nums)
        ans = []
        def findSubset(index, curr_list):
            if index == n:
                return
            if len(curr_list) == n:
                ans.append(curr_list.copy())
                return

            findSubset(index + 1, curr_list.copy())
            curr_list.append(nums[index])
            ans.append(curr_list.copy())
            findSubset(index + 1, curr_list)
            
        findSubset(0, [])

        return ans

    
    # space efficent
    def subsets2(self, nums):
        ans = []
        n = len(nums)
        
        def dfs(index, curr_list):
            if index >= n:
                ans.append(curr_list.copy())
                return

            curr_list.append(nums[index])
            dfs(index + 1, curr_list)

            curr_list.pop()
            dfs(index + 1, curr_list)

        dfs(0, [])

        return ans
            
            