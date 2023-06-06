import math
from typing import List


class Solution:
    
    def calculateHour(self, dist: List[int], speed: int) -> int:
        hour_taken = 0
        
        for distance in dist:
            hour_taken = math.ceil(hour_taken)
            
            hour_taken += (distance/speed)
            
        return hour_taken
    
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: binary search, 
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:   
        lo, hi = 1, (10**7)
        ans = -1
        
        while lo <= hi:
            mid = (lo+hi)//2
            
            if self.calculateHour(dist, mid) <= hour:
                ans = mid
                hi = mid-1
            else:
                lo = mid+1

        return ans