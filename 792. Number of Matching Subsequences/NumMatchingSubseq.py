from collections import defaultdict
from typing import List


class Solution:
    
    # O(len(words)*len(word)+len(s)) time,
    # O(len(word)*len(words)) space,
    # Approach: hash map, 
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ch_to_word = defaultdict(list)
        for word in words:
            ch_to_word[word[0]].append(word)
        
        ans = 0
        for ch in s:
            new_entries = []
            while ch_to_word[ch]:
                word = ch_to_word[ch].pop()
                if len(word) == 1:
                    ans += 1
                else:
                    new_entries.append(word[1:])
                    
            for word in new_entries:
                ch_to_word[word[0]].append(word)
                    
        return ans