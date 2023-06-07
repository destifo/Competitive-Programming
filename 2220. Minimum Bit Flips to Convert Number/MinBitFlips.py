class Solution:
    
    # O(ln(start)) time,
    # O(1) space,
    # Approach: bit manipulation, 
    def minBitFlips(self, start: int, goal: int) -> int:
        flips = 0
        
        while start != 0 or goal != 0:
            
            if (start & 1) != (goal & 1):
                flips += 1
                
            start >>= 1
            goal >>= 1
            
        return flips