class Solution:
    def findMinMoney(self, lo, hi, memo) -> int:
        
        if lo >= hi:
            return 0
        
        if (lo, hi) in memo:
            return memo[(lo, hi)]
        
        min_money = float('inf')
        mid = (lo+hi)//2
        
        for num in range(lo, hi+1):
            
            money = num + max(self.findMinMoney(lo, num-1, memo), self.findMinMoney(num+1, hi, memo))
            min_money = min(min_money, money)
        
        memo[(lo, hi)] = min_money
        return int(min_money)
    
    
    def getMoneyAmount(self, n: int) -> int:
        
        return self.findMinMoney(1, n, {})


sol = Solution()
print(sol.getMoneyAmount(10))