from typing import List, Tuple


class Solution:
    
    def inRange(self, num: int, ranges: List[Tuple[int]]) -> bool:
        low, hi = 0, len(ranges)-1

        while low <= hi:
            mid = (low+hi)//2
            start, end = ranges[mid]
            if start <= num <= end:
                return True
            elif start > num:
                hi = mid-1
            else:
                low = mid+1

        return False
    
    
    def isValidRadius(self, radius: int, houses: List[int], heaters: List[int]) -> bool:
        
        ranges = []
        for heater in heaters:
            ranges.append((max(1, heater-radius), heater+radius))
        
        ranges.sort()
        for house in houses:
            if not self.inRange(house, ranges):
                return False
            
        return True
    
    
    # O(nlogn^2) time,
    # O(nlogn) space,
    # Approach: binary search, sorting, 
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        low, hi = 0, max(max(houses), max(heaters))
        smallest_radius = hi
        
        while low <= hi:
            mid = (low+hi)//2
            if self.isValidRadius(mid, houses, heaters):
                smallest_radius = mid
                hi = mid-1
            else:
                low = mid+1
                
        return smallest_radius