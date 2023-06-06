from collections import Counter
from typing import Dict


class Solution:
    # O(m + n) time,
    # O(m) space,
    # Approach: two pointers, sliding window
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        t_count = Counter(t) # O(1) space,
        
        # O(1) time,
        def areWindowsEqual(t_count: Dict[str: int], window: Dict[str: int]) -> bool:
            for key, val in t_count.items():
                if key in window and window[key] >= val:
                    continue
                return False
            
            return True
        
        
        if n > m:
            return ""
        
        min_len = float('inf')
        result = ''
        window = {} # O(1) space,
        l, r = 0, n
        
        for ch in s[l:r]:
            window[ch] = window.get(ch, 0) + 1
            
        if t_count == window:
            return s[l:r]
        
        while r <= m:
            areEqual = areWindowsEqual(t_count, window)
            if areEqual:
                if min_len > r - l:
                    min_len = (r - l)
                    result = s[l:r]
                window[s[l]] -=1
                l +=1
            else:
                if r == m:
                    break
                window[s[r]] = window.get(s[r], 0) + 1
                r +=1
                
        
        return result


sol = Solution()
print(sol.minWindow("ADOBECODEBANC"
,"ABC"))