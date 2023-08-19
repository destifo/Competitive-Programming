from typing import List


class Solution:
    
    def validTastiness(self, p: int, price: List[int], k: int) -> int:
        
        nums = [price[0]]
        for i in range(len(price)):
            if price[i]-nums[-1] >= p:
                nums.append(price[i])
            if len(nums) == k:
                return True
                
        return False
    
    
    # O(n^2logn) time,
    # O(n^2logn) space,
    # Approach: binary search, greedy, 
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        lo, hi = 0, price[-1]
        ans = 0
        
        while lo <= hi:
            mid = (lo+hi)//2
            if self.validTastiness(mid, price, k):
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
                
        return ans