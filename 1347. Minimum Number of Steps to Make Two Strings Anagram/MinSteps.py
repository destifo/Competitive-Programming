from collections import Counter
from typing import Dict


class Solution:
    
    def findSimilars(self, count1: Dict[str, int], count2: Dict[str, int]) -> int:
        
        similars = 0
        
        for ch, val1 in count1.items():
            val2 = count2.get(ch, 0)
            similars += min(val1, val2)
            
        return similars
    
    
    # O(n + m) time,
    # O(1) space,
    # Approach: string, 
    def minSteps(self, s: str, t: str) -> int:
        count1 = Counter(s)
        count2 = Counter(t)
        
        return len(s) - self.findSimilars(count1, count2)