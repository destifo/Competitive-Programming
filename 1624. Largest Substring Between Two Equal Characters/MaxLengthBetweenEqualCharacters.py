class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: hash map, 
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_seen = {}
        ans = -1
        
        for i, ch in enumerate(s):
            if ch not in first_seen:
                first_seen[ch] = i
            else:
                curr = i-first_seen[ch]-1
                ans = max(ans, curr)
        
        return ans