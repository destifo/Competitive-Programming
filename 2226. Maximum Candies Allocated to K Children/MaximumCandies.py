from typing import List


class Solution:
    
    
    def validDistribution(self, candy_count, candies, children):
        
        possible_distribution = 0
        
        for candy in candies:
            
            possible_distribution += int(candy/candy_count)
            if possible_distribution >= children:
                return True
            
        return possible_distribution >= children
    
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: binary search, 
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        lo, hi = 1, sum(candies)//k
        max_candy = 0
        
        while lo <= hi:
            mid = (lo+hi)//2
            
            if self.validDistribution(mid, candies, k):
                max_candy = mid
                lo = mid + 1
            else:
                hi = mid-1
                
        return max_candy