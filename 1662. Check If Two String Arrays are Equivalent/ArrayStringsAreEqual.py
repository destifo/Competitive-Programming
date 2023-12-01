from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: string, array
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)