class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
    
    
    # O(n) time,
    # O(n) space,
    # Approach: two pointers, 
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        variances = []
        
        while left < right:
            if s[left] != s[right]:
                variant1 = s[:left] + s[left+1:]
                variant2 = s[:right] + s[right+1:]
                variances.append(variant1)
                variances.append(variant2)
                break
            
            left += 1
            right -= 1
            
        if variances:
            return self.isPalindrome(variances[0]) or self.isPalindrome(variances[1])
        
        return True