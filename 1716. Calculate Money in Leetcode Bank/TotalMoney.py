class Solution:
    
    def findSummation(self, start: int, end: int) -> int:
        
        return ((end-start+1) * (start+end))//2
    
    
    # O(n) time,
    # O(1) space,
    # Approach: math, 
    def totalMoney(self, n: int) -> int:
        week_days = 7
        qutnt = n // week_days
        mod = n % week_days
        
        ans = 0
        start = 1
        for _ in range(qutnt):
            ans += self.findSummation(start, start+week_days-1)
            start += 1
            
        ans += self.findSummation(start, start+mod-1)
        
        return ans
    
    
    # O(1) time,
    # O(1) space,
    # Approach: math, 
    def totalMoney2(self, n: int) -> int:
        week_days = 7
        k = n // week_days
        week1 = 28
        week_k = week1 + (k-1)*week_days if k >= 1 else 0
        full_week_sum = (k * (week1 + week_k))//2
        mod = n % week_days
        last_week_sum = (mod * ((k+1) + (k+mod)))//2
        ans = full_week_sum + last_week_sum
        
        return ans