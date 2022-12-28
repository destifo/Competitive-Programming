from typing import List


class Solution:
    
    def compare(self, word1, word2, mapping):
        
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            if mapping[word1[i]] > mapping[word2[i]]:
                return False
            elif mapping[word1[i]] < mapping[word2[i]]:
                return True
            
        return len(word2) >= len(word1)
        
    
    # O(n^2 * m) time, n--> len(words), m --> len(words[i])
    # O(n) space,
    # Approach: hashmap, 
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_order = {}
        for i, char in enumerate(order):
            char_order[char] = i
            
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not self.compare(words[i], words[j], char_order):
                    return False
        
        return True