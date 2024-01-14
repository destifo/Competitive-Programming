from collections import Counter, defaultdict


class Solution:
    
    def check(self, word_count1, word_count2) -> bool:
        count1, count2 = defaultdict(int), defaultdict(int)
        
        for cnt in word_count1.values():
            count1[cnt] += 1
            
        for cnt in word_count2.values():
            count2[cnt] += 1
            
        for cnt in count1:
            if count1[cnt] != count2[cnt]:
                return False
            
        for cnt in count2:
            if count1[cnt] != count2[cnt]:
                return False
            
        return True
        
    
    # O(n) time,
    # O(1) space,
    # Approach: hashmap, 
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_count = Counter(word1)
        word2_count = Counter(word2)
        
        return self.check(word1_count, word2_count) and set(word1) == set(word2)
    
    
    # O(n + m) time,
    # O(1) space,
    # Approach: counting, hash map
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())