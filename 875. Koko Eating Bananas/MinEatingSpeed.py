'''
https://leetcode.com/problems/koko-eating-bananas/
'''


from typing import List


class Solution:
    # O(nlogn) time,
    # O(1) space,
    # Approach: binary search,
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        big_pile = max(piles)
        if n == h:
            return big_pile
        
        def timeFunc(speed:int) -> int:
            tot_hr = 0
            for pile in piles:
                bananas = pile
                hr = bananas // speed
                if bananas % speed != 0:
                    hr +=1
                tot_hr += hr
                
            return tot_hr
        
        ans = float('inf')
        l, r = 1, big_pile
        
        while l <= r:
            mid = (l + r) // 2
            hr = timeFunc(mid)
            
            if hr <= h:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        
            
        return ans