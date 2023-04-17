from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: array, 
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        ans = [False for _ in range(len(candies))]
        
        for i, candy in enumerate(candies):
            if candy+extraCandies >= greatest:
                ans[i] = True
                
        return ans