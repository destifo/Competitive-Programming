class Solution:
    
    def isComplete(self, row: int, coins: int) -> bool:
        
        needed_coins = (row * (row+1))//2
        return needed_coins <= coins
    
    
    # O(logn) time,
    # O(1) space,
    # Approach: binary search, math, 
    def arrangeCoins(self, n: int) -> int:
        low, hi = 0, n
        ans = 0
        
        while low <= hi:
            mid = (low+hi)//2
            if self.isComplete(mid, n):
                ans = mid
                low = mid+1
            else:
                hi = mid-1
                
        return ans