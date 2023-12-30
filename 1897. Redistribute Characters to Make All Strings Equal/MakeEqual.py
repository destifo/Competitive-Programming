from collections import defaultdict
from typing import List


class Solution:
    
    # O(m) time, m -> sum(all_words)
    # O(1) space,
    # Approach: couting, hash map
    def makeEqual(self, words: List[str]) -> bool:
        count = defaultdict(int)
        
        for word in words:
            for ch in word:
                count[ch] += 1
                
        n = len(words)
        if n == 1:
            return True
        for cnt in count.values():
            if cnt % n != 0:
                return False
            
        return True