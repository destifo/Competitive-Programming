class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: string, 
    def largestOddNumber(self, num: str) -> str:
        index = 0
        
        for i, digit in enumerate(num):
            digit = int(digit)
            if digit % 2 == 1:
                index = i+1
                
        return num[:index]