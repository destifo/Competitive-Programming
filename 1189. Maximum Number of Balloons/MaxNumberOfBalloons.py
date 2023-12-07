from collections import Counter


class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: counting, hash map
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        ans = float('inf')
        
        for ch in "balon":
            if ch in "lo":
                ans = min(ans, count[ch]//2)
            else:
                ans = min(ans, count[ch])
            if ans == 0:
                return ans
                
        return ans