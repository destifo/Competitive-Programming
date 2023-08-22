from typing import List


class Solution:
    
    # O(n^2) time,
    # O(n) space,
    # Approach: array, greedy, 
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        nums = set()
        for i in range(n):
            nums.add(fronts[i])
            nums.add(backs[i])
            
        nums = list(nums)
        nums.sort()
        
        for num in nums:
            flippable = False
            for i in range(n):
                flippable = True
                if fronts[i] == num == backs[i]:
                    flippable = False
                    break
                    
            if flippable:
                return num
            
        return 0