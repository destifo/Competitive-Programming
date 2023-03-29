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