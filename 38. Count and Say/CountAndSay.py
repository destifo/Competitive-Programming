class Solution:
    # O(n^2) time,
    # O(n^2) space,
    # Approach: recursion, hashtable
    def countAndSay(self, n: int) -> str:
        
        def _countAndSay(digits: str, depth: int) -> str:
            if depth == 1:  return digits
            
            new_digits = ""
            l, r = 0, 0
            
            while r < len(digits):
                while r < len(digits) and digits[l] == digits[r]:
                    r +=1
                    
                new_digits += str(r-l)
                new_digits += digits[l]
                l = r
                
            return _countAndSay(new_digits, depth-1)
        
        return _countAndSay('1', n)