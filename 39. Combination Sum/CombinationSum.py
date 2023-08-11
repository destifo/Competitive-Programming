'''
https://leetcode.com/problems/combination-sum/
'''

from typing import List


class Solution:
    def combinationSum(self, candidates, target: int):
        # little bit slower Soln
        n = len(candidates)
        ans = []

        def dfs(i, currlst, tot):
            if i >= n or tot > target:
                return
            if tot == target:
                ans.append(currlst)

            dfs(i + 1, currlst.copy(), tot)
            currlst.append(candidates[i])
            tot += candidates[i]
            dfs(i, currlst.copy(), tot)

        dfs(0, [], 0)

        return ans


    def combinationSum2(self, candidates, target: int):
        n = len(candidates)
        ans = []

        def dfs(i, currlst, tot):
            if i >= n or tot > target:
                return
            if tot == target:
                ans.append(currlst)

            currlst.append(candidates[i])
            dfs(i, currlst, tot + candidates[i])
            currlst.pop()
            dfs(i + 1, currlst, tot)

        dfs(0, [], 0)

        return ans
    
    
    def findCombs(self, index: int, rem: int, cands: List[int], comb: List[int], combs: List[List[int]]) -> None:
        
        if rem == 0:
            combs.append(comb[::])
            return
        
        if rem < 0 or index == len(cands):
            return
        
        if cands[index] <= rem:
            comb.append(cands[index])
            self.findCombs(index, rem-cands[index], cands, comb, combs)
            comb.pop()
            
        self.findCombs(index+1, rem, cands, comb, combs)
    
    
    # O(2^target) time,
    # O(n+target) space,
    # Approach: backtracking, 
    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        self.findCombs(0, target, candidates, [], combs)
        return combs    


sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))