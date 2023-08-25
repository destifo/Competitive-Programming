from typing import Dict, Tuple


class Solution:
    
    def check(self, i: int, j: int, k: int, s1: str, s2: str, s3: str, turn: bool, memo: Dict[Tuple[int], bool]) -> bool:
        n, m = len(s1), len(s2)
        if k == len(s3):
            return True
        
        state = (i, j, turn)
        if state in memo:
            return memo[state]

        if turn:
            for r in range(i+1, n+1):
                diff = r-i
                if s1[i:r] == s3[k:k+diff]:
                    if self.check(r, j, k+diff, s1, s2, s3, not turn, memo):
                        return True
        else:
            for r in range(j+1, m+1):
                diff = r-j
                if s2[j:r] == s3[k:k+diff]:
                    if self.check(i, r, k+diff, s1, s2, s3, not turn, memo):
                        return True
        
        memo[state] = False
        return False
        
    
    # O(n*m) time,
    # O(n*m) space,
    # Approach: string, backtracking, 
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if len(s3) != n + m:
            return False
        
        return self.check(0, 0, 0, s1, s2, s3, True, {}) or self.check(0, 0, 0, s1, s2, s3, False, {})