from collections import Counter
from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: couting, hash map
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ_count = Counter(Counter(arr).values())

        for val in occ_count.values():
            if val > 1:
                return False
            
        return True