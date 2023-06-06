'''
https://leetcode.com/problems/combination-sum-ii/
'''


from typing import List


class Solution:
    # O(n!/(r! (n-r)!)) time, r --> varies but lowest is 1
    # O(n!/(r! (n-r)!)) space,
    # Approach: DFS, backtracking
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        
        def findSolutions(index: int, lst: List[int], tot:int) -> None:
            n = len(candidates)
            if index == n or candidates[index] > target:
                return
            
            tot += candidates[index]
            if tot > target:    return
            
            lst.append(candidates[index])
            if tot == target:
                ans.append(lst[::])
                lst.pop()
                return
            
            findSolutions(index+1, lst, tot)
            lst.pop()
            tot -=candidates[index]
            while index < n-1 and candidates[index] == candidates[index+1]:
                index +=1
            findSolutions(index+1, lst, tot)
            
        
        findSolutions(0, [], 0)
        return ans


sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5]
,8))