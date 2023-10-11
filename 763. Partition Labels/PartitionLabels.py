from collections import Counter
from typing import Dict, List, Set


class Solution:
    
    def isValidPartition(self, chosen: Set[str], remaining: Dict[str, int]) -> bool:
        
        for letter in chosen:
            if remaining[letter] > 0:
                return False
            
        return True
    
    
    # O(n) time,
    # O(1) space,
    # Approach: hash table, 
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        count = Counter(s)
        
        curr_size = 0
        chosen = set()
        for ch in s:
            chosen.add(ch)
            curr_size += 1
            count[ch] -= 1
            if self.isValidPartition(chosen, count):
                ans.append(curr_size)
                chosen = set()
                curr_size = 0
        
        return ans