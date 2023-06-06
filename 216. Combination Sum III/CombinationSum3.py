'''
https://leetcode.com/problems/combination-sum-iii/
'''

class Solution:
    def combinationSum3(self, k: int, n: int):
        # gotta give it to Neetcode, one example from him and u can do the other realted questions
        ans = []

        def dfs(currNum, currlst, tot, visited):
            if tot == n and len(currlst) == k:
                ans.append(currlst.copy())
                return

            if tot > n or currNum > n or currNum > 9:
                return

            if currNum not in visited.keys():
                currlst.append(currNum)
                visited[currNum] = 1
                dfs(currNum, currlst, tot + currNum, visited)
                currlst.pop()
                visited.pop(currNum)

            dfs(currNum + 1, currlst, tot, visited)

        dfs(1, [], 0, {})

        return ans