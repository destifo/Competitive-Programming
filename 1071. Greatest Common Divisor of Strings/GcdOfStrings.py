class Solution:
    
    def divides(self, divider: str, dividend: str) -> bool:
        
        n = len(divider)
        for i in range(0, len(dividend), n):
            if divider != dividend[i:i+n]:
                return False
        
        return True
    
    # O(n^2) time,
    # O(n^2) space,
    # Approach: string, 
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""
        
        larger, smaller = (str1, str2) if len(str1) >= len(str2) else (str2, str1)
        
        for i in range(len(smaller)):
            divider = smaller[:i+1]
            if self.divides(divider, smaller) and self.divides(divider, larger):
                gcd = divider
                
        return gcd