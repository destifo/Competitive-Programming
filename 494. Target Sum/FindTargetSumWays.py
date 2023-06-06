from typing import List


class Solution:
    # O(n*sum(nums)) time, it won't be 2^n cause there will be repeated tot that will be avoided by the memo
    # O(n*sum(nums)) space,
    # Approach: dp, memoization
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        
        def evalExpression(index, tot):
            if index == n:
                return 1 if tot == target else 0
            
            if (index, tot) in memo:
                return memo[(index, tot)]
                
            memo[(index, tot)] = evalExpression(index+1, tot+nums[index]) + evalExpression(index+1, tot-nums[index])
            return memo[(index, tot)]
            
        return evalExpression(0, 0)


sol = Solution()
print(sol.findTargetSumWays([1,1,1,1,1]
,3))