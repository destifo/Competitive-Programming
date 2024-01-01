from typing import List


class Solution:
    
    # O(nlogn + mlogm) time,
    # O(1) space,
    # Approach: sorting, two pointers
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        p1, p2 = 0, 0
        ans = 0
        
        while p1 < len(g) and p2 < len(s):
            if s[p2] >= g[p1]:
                ans += 1
                p2 += 1
            p1 += 1
            
        return ans