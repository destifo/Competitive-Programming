from typing import List


class Solution:
    
    def findMaxCoefficient(self, index, time, satisfaction, memo):
        if index == len(satisfaction):
            return 0
        
        if (index, time) in memo:
            return memo[(index, time)]
        
        choose = time*satisfaction[index] + self.findMaxCoefficient(index+1, time+1, satisfaction, memo)
        skip = self.findMaxCoefficient(index+1, time, satisfaction, memo)
        
        memo[(index, time)] = max(choose, skip)
        return max(choose, skip)
    
    
    # O(len(satisfaction)*max(time)) time,
    # O(len(satisfaction)*max(time)) space,
    # Approach: top down dp, 
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        return self.findMaxCoefficient(0, 1, satisfaction, {})
    

    # O(n) time,
    # O(1) space,
    # Approach: greedy, 
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        tot = 0
        positive_sum = 0
        positive_prefix = 0
        negative_sum = 0
        negative_prefix = 0
    
        for i in range(len(satisfaction)-1, -1, -1):
            curr_sat = satisfaction[i]
            next_tot = positive_sum + negative_sum + curr_sat
            if next_tot < tot:
                return tot
            
            tot = next_tot
            if curr_sat >= 0:
                positive_sum += curr_sat
                positive_prefix += curr_sat
            else:
                positive_sum += curr_sat
                negative_prefix += curr_sat
            positive_sum += positive_prefix
            negative_sum += negative_prefix
            
        return tot