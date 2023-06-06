class Solution:
    
    # O(1) time,
    # O(1) space,
    # Approach: math, 
    def countOdds(self, low: int, high: int) -> int:
        return (high-low+1)//2 + (1 if (high-low+1) % 2 == 1 and low % 2 == 1 else 0)