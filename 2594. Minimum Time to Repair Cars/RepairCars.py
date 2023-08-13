from math import sqrt
from typing import List


class Solution:
    
    def carsRepaired(self, rank: int, time: int) -> int:
        return int(sqrt(time/rank))
    
    
    def validTime(self, time: int, ranks: List[int], cars: int) -> bool:
        tot_repaired = 0
        for rank in ranks:
            tot_repaired += self.carsRepaired(rank, time)
            
        return tot_repaired >= cars
    
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: binary search, math
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()
        lo, hi = 1, ranks[0]*cars*cars
        ans = hi
        
        while lo <= hi:
            mid = (lo+hi)//2
            if self.validTime(mid, ranks, cars):
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
                
        return ans