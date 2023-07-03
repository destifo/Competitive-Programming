from typing import Counter


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: greedy, simulation
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal): return False
        
        for i in range(len(s)):
            if goal[i] == s[i]: continue
                
            if i == len(s)-1:   return False
            are_buddy = False
            looped = False
            for j in range(i+1, len(s)):
                looped = True
                if goal[j] == s[j]: continue
                
                s = list(s)
                s[i], s[j] = s[j], s[i]
                if "".join(s) == goal:
                    are_buddy = True
                break
            
            if looped:  return are_buddy
        
        count = Counter(s)
        max_freq = max(count.values())
        
        return True if max_freq >= 2 else False