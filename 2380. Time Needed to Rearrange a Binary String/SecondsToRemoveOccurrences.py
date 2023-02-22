from typing import List


class Solution:
    
    
    def remove(self, s: List[int]) -> int:
        
        to_remove = []
        i = 0
        
        while i < len(s)-1:
            if s[i] == 0 and s[i+1] == 1:
                to_remove.append(i)
                i += 2
            else:
                i += 1
                
        for i in to_remove:
            s[i] = 1
            s[i+1] = 0
            
        return len(to_remove)
    
    
    # O(n^2) time,
    # O(n) space,
    # Approach: simulation, 
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s = [int(ch) for ch in s]
        time = 0
        
        while self.remove(s) > 0:
            time += 1
            
        return time