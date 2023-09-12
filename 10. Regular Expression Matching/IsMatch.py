from typing import Tuple, Dict


class Solution:
    
    def matches(self, i: int, j: int, s: str, p: str, memo: Dict[Tuple[int], bool]) -> bool:
        
        if i == len(s) and j == len(p):
            return True
        
        if j == len(p):
            return False
        
        state = (i, j)
        if state in memo:
            return memo[state]
        
        if i < len(s) and s[i] == p[j] or p[j] == ".":
            if self.matches(i+1, j+1, s, p, memo):
                return True
            
        if p[j] == "*":
            if self.matches(i, j+1, s, p, memo):
                return True
            
        if j < len(p)-1 and p[j+1] == "*" and self.matches(i, j+2, s, p, memo):
            return True
        
        if i < len(s) and j < len(p)-1 and p[j+1] == "*":
            for k in range(i+1, len(s)+1):
                if p[j] != "." and s[i:k] != (p[j]*(k-i)):
                    break
                if self.matches(k, j+2, s, p, memo):
                    return True
        
        memo[state] = False
        return False
    
    
    # O(n^2) time,
    # O(n^2) space,
    # Approach: top down dp, 
    def isMatch(self, s: str, p: str) -> bool:
        return self.matches(0, 0, s, p, {})