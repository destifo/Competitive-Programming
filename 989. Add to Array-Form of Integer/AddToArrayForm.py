from collections import deque
from typing import List


class Solution:
    
    def toArrayForm(self, num: int) -> List[int]:
        queue = deque()
        
        while num:
            queue.appendleft(num%10)
            num //= 10
            
        return queue
    
    
    def toInteger(self, digits: List[int]) -> int:
        num = 0
        power = 0
        
        while digits:
            digit = digits.pop()
            num += (digit * (10**power))
            power += 1
        
        return num
    
    
    # O(digits) time,
    # O(digits) space,
    # Approach: math, array
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        k += self.toInteger(num)
        return self.toArrayForm(k)
        