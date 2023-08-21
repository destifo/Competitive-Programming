class Solution:
    
    # O(n*(factor_of(n))) time,
    # O(n) space,
    # Approach: string, 
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n//2):
            m = i+1
            if n % m != 0:
                continue
            substr = s[:m]
            exists = True
            for j in range(0, n, m):
                if s[j:j+m] != substr:
                    exists = False
                    break
            if exists:  return True
            
        return False