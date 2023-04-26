class Solution:
    
    # O(1) time,
    # O(1) space,
    # Approach: math, 
    def addDigits(self, num: int) -> int:
        if num % 9 == 0 and num != 0:
            return 9
        return num % 9