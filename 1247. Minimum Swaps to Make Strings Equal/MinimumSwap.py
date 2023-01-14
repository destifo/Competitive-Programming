from collections import Counter


class Solution:
    
    # O(len(s1)) time,
    # O(len(s1)) space,
    # Approach: greedy, 
    def minimumSwap(self, s1: str, s2: str) -> int:
        s1_count = Counter(s1)
        s2_count = Counter(s2)
        x_count = s1_count['x'] + s2_count['x']
        y_count = s1_count['y'] + s2_count['y']
        
        if x_count % 2 == 1 or y_count % 2 == 1:
            return -1
        
        unequal_x = 0
        unequal_y = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':    unequal_x += 1
                else:   unequal_y += 1
        
        swaps = unequal_x//2 + unequal_y//2 + (unequal_x%2)*2
        
        return swaps