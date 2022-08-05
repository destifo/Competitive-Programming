'''
https://leetcode.com/problems/combination-sum-iv/
'''


from typing import List


class Solution:
    # O(n * target) time,
    # O(target) space,
    # Approach: top down memoization, dp
    def combinationSum4(self, nums: List[int], target: int) -> int:
        result = [0]
        cache = {}
        
        def dfs(tot):
            if tot == target:
                result[0]+=1
                return
            if tot > target:    return
            for num in nums:
                rslt = result[0]
                if (tot+num) in cache.keys():
                    result[0] += cache[tot+num]
                    continue
                dfs(tot+num)
                cache[tot+num] = result[0] - rslt
                
        dfs(0)
        return result[0]