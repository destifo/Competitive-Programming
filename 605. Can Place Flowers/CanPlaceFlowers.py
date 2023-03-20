from typing import List


class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: counting, 
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty_spots = 0
        
        for i in range(0, len(flowerbed)):
            if i > 0 and flowerbed[i-1]:
                continue
            if i < len(flowerbed)-1 and flowerbed[i+1]:
                continue
            
            empty_spots += (flowerbed[i]+1) % 2
            flowerbed[i] = 1
            
            if empty_spots >= n:
                return True
            
        return False