from collections import defaultdict
from typing import Dict, Tuple


class Solution:
    
    def countLetters(self, window: Dict[str, int]) -> Tuple[int]:
        sorted_window = sorted(window.items(), key=lambda x:x[1], reverse=True)

        return sorted_window[0][1], sum(pair[1] for pair in sorted_window[1:])
    
    
    # O(n) time,
    # O(1) space,
    # Approach: sliding window, hashtable 
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        left, right = 0, 0
        ans = 1
        
        while right < len(s):
            window[s[right]] += 1
            
            unique_count, nonunique_count = self.countLetters(window)            
            while nonunique_count > k:
                window[s[left]] -= 1
                left += 1
                unique_count, nonunique_count = self.countLetters(window)
            else:
                ans = max(ans, (right-left)+1)
                right += 1
                
        return ans
    
    
    def isValidForm(self, window: Dict[str, int], k: int) -> bool:
        sortd = sorted(window.values())
        sortd.pop()
        
        return sum(sortd) <= k
    
     
    # O(n) time,
    # O(1) space,
    # Approach: sliding window, sorting, counting
    def characterReplacement2(self, s: str, k: int) -> int:
        left, right = 0, 0
        window = {}
        ans = 0
        
        while right < len(s):
            window[s[right]] = window.get(s[right], 0) + 1
            
            while not self.isValidForm(window, k):
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    window.pop(s[left])
                left += 1
                
            ans = max(ans, right-left+1)
            right += 1
            
        return ans