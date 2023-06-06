from typing import List


class Solution:
    
    def canWin(self, remaining: int, nums: List[int], memo) -> bool:
        
        if nums[-1] >= remaining:
            return True
            
        scenario_key = tuple(nums)
        if scenario_key in memo:
            return memo[scenario_key]
        
        win = False
        for i in range(len(nums)):
            
            num = nums[i]
            
            if not self.canWin(remaining-num, nums[:i]+nums[i+1:], memo):
                win = True
                break
                
        memo[scenario_key] = win
        return win              
    
    
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:  
        summation = (maxChoosableInteger * (maxChoosableInteger+1))/2
        
        if summation < desiredTotal:
            return False
        
        if summation == desiredTotal: 
            return maxChoosableInteger%2 == 1
        
        return self.canWin(desiredTotal, list(range(1, maxChoosableInteger+1)), {})
    