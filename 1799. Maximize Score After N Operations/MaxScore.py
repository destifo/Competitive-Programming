from typing import Dict, List, Tuple


class Solution:
    
    def gcd(self, x: int, y: int) -> int:
        while y != 0:
            temp = y
            y = (x%y)
            x = temp
            
        return x
    
    
    def findMaxScore(self, operation: int, nums: List[int], selected: List[bool], memo: Dict[Tuple[int], int]) -> int:
        
        if operation > len(nums)//2:
            return 0
        
        unselected_nums = []
        for i in range(len(nums)):
            if not selected[i]:
                unselected_nums.append(nums[i])
                
        unselected_nums.sort()
        
        state = tuple(unselected_nums)
        if state in memo:
            return memo[state]
        
        max_score = 0
        for i in range(len(nums)):
            if selected[i]: continue
            selected[i] = True
            for j in range(len(nums)):
                if selected[j]: continue
                selected[j] = True
                
                curr_score = (operation * self.gcd(nums[i], nums[j])) + self.findMaxScore(operation+1, nums, selected, memo)
                max_score = max(max_score, curr_score)
                selected[j] = False
            selected[i] = False
                
        memo[state] = max_score
        return max_score
    
    
    # O(2^2n) time,
    # O(2^2n) space,
    # Approach: top down dp, math
    def maxScore(self, nums: List[int]) -> int:
        selected = [False for _ in range(len(nums))]

        return self.findMaxScore(1, nums, selected, {})