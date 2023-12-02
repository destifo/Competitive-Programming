from collections import Counter
from typing import Dict, List


class Solution:
    
    def isEqual(self, word_count: Dict[str, int], char_count: Dict[str, int]) -> bool:
        
        for ch, cnt in word_count.items():
            if char_count[ch] < cnt:
                return False
            
        return True
    
    
    # O(n*m) time, n --> len(words), m --> len(word)
    # O(n*m) space,
    # Approach: couting, hash maps
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        ans = 0
        
        for word in words:
            if self.isEqual(Counter(word), char_count):
                ans += len(word)
                
        return ans