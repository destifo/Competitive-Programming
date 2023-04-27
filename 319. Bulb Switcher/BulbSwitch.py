from math import sqrt


class Solution:
    
    # O(1) time,
    # O(1) space,
    # Approach: math, 
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))