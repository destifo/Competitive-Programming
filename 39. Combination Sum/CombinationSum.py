'''
https://leetcode.com/problems/combination-sum/
'''

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


sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))