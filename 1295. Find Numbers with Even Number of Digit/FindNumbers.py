from typing import List


class Solution:
    
    def isEven(self, num: int) -> int:
        
        if (num >= 10 and num <= 99) or (num >= 1000 and num <= 9999) or num == 100000:
            return True
        
        return False
    
    
    # O(n) time,
    # O(1) space,
    # Approach: array, 
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if self.isEven(num):
                count += 1
                
        return count