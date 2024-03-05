class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: two pointers, 
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s)-1
        removed = 0
        
        while left < right and s[left] == s[right]:
            curr_char = s[left]
            while left <= right and s[left] == curr_char:
                removed += 1
                left += 1
                
            while right >= left and s[right] == curr_char:
                removed += 1
                right -= 1
                
        return len(s)-removed