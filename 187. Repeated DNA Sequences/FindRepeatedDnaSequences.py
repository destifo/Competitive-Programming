from collections import defaultdict
from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: sliding window, two pointers, 
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        count = defaultdict(int)
        ans = []
        
        left, right = 0, 10
        while right <= len(s):
            count[s[left:right]] += 1
            left += 1
            right += 1
        
        for seq, cnt in count.items():
            if cnt > 1:
                ans.append(seq)
                
        return ans