from typing import List


class Solution:
    # O(n*m) time, n--> len(s), m --> len(words[i])
    # O(1) space,
    # Approach: two pointers, 
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def isExpressive(word1: str, word2: str) -> bool:
            ch_count1, ch_count2 = 0, 0
            i, j = 0, 0
            first_time = True
            
            while i < len(word1) and j < len(word2):
                if word1[i] != word2[j]:    return False
                
                while first_time or (i < len(word1) and word1[i] == word1[i-1]):
                    i +=1
                    ch_count1 +=1
                    first_time = False
                    
                first_time = True
                while first_time or (j < len(word2) and word2[j] == word2[j-1]):
                    j +=1
                    ch_count2 +=1
                    first_time = False
                
                if ch_count1 != ch_count2 and (ch_count2) < 3 or ch_count2 < ch_count1:
                    return False
                
                first_time = True
                ch_count1, ch_count2 = 0, 0
            
            if i != len(word1) or j != len(word2):
                return False
            
            return True
        
        ans = 0
        for word in words:
            if isExpressive(word, s):
                ans +=1
                
        return ans