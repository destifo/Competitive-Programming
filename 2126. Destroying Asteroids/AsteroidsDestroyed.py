from typing import List


class Solution:
    
    # O(nlogn) time,
    # O(1) space,
    # Appraoch: sorting, greedy
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        
        for asteroid in asteroids:
            if mass < asteroid:
                return False
            
            mass += asteroid
            
        return True