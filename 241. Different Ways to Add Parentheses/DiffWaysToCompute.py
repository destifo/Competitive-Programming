from typing import List


class Solution:
    
    def findWays(self, curr_exp, memo) -> List[str]:
        
        if len(curr_exp) == 1:
            return [curr_exp[0]]
        
        if curr_exp in memo:
            return memo[curr_exp]
        
        evals = []
        for i in range(len(curr_exp)):
            
            if not curr_exp[i].isdigit():
                
                left = self.findWays(curr_exp[:i], memo)
                right = self.findWays(curr_exp[i+1:], memo)
                
                for val1 in left:
                    for val2 in right:
                        evals.append(str(eval(val1+curr_exp[i]+val2)))
        
        if not evals:
            evals.append(curr_exp)
        
        memo[curr_exp] = evals
        return evals
        
    
    # O(n) time,
    # O(n) space,
    # Approach: divide and conquer, recursion, top down dp, memoization
    def diffWaysToCompute(self, expression: str) -> List[int]:
        answer = self.findWays(expression, {})
        
        return [int(num) for num in answer]