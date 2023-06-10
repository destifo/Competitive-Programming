class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: sliding window, 
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left, right = 0, 0
        ans = 1
        repeated_digit = ''
        prev = ""
          
        while right < len(s):
            if repeated_digit != "" and prev == s[right]:
                ans = max(ans, right-left)
                while s[left] != s[left+1]:
                    left += 1
                left += 1
            if prev == s[right]:
                repeated_digit = s[right]
            
            prev = s[right]
            right += 1
            
        ans = max(ans, right-left)
            
        return ans