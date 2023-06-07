class Solution:
    
    # O(ln(c)) time,
    # O(1) space,
    # Approach: bit manipulation, 
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        
        while a != 0 or b != 0 or c != 0:
            
            if c & 1 == 1 and (a & 1 == 0 and b & 1 == 0):
                flips += 1
            elif c & 1 == 0 and (a & 1 == 1 or b & 1 == 1):
                flips += (a & 1) + (b & 1)
            
            a >>= 1
            b >>= 1
            c >>= 1
            
        return flips