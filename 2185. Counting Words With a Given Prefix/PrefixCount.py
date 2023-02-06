from typing import List


class Solution:
    
    def isPrefix(self, prefix, word):
        
        for i in range(len(prefix)):
            if prefix[i] != word[i]:
                return False
            
        return True
    
    # O(len(word)*len(pref)) time,
    # O(1) space,
    # Approach: string, 
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefixes = 0
        
        for word in words:
            if len(word) >= len(pref) and self.isPrefix(pref, word):
                prefixes += 1
        
        return prefixes