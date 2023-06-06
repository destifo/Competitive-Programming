from typing import List


class Solution:
    
    def sign(self, num):
        return num//abs(num)
    
    
    # O(n) time,
    # O(n) space,
    # Approach: stack, 
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        
        for asteroid in asteroids:
            result.append(asteroid)
            
            while len(result) >= 2 and self.sign(result[-1]) != self.sign(result[-2]) and self.sign(result[-1]) < 0:
                positive, negative = result[-2], result[-1]
                tot = result.pop() + result.pop()
                if tot > 0:
                    result.append(positive)
                elif tot < 0:
                    result.append(negative)
                    
        return result