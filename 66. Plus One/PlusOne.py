from typing import List


class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: array, 
    def plusOne(self, digits: List[int]) -> List[int]:
        
        left_over = True
        
        for i in range(len(digits)-1, -1, -1):
            if not left_over:
                break
            
            left_over = (digits[i] == 9)
            digits[i] = 0 if digits[i] == 9 else digits[i] + 1
        
        return ([1] + digits) if left_over else digits