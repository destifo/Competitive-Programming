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
    
    
    # O(n) time,
    # O(n) space,
    # Approach: array, hashmap, 
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        unusable = set()
        for i in range(n):
            if fronts[i] == backs[i]:
                unusable.add(fronts[i])
        
        ans = float('inf')
        for i in range(n):
            if fronts[i] not in unusable:
                ans = min(ans, fronts[i])
            if backs[i] not in unusable:
                ans = min(ans, backs[i])
                
        return ans if ans != float('inf') else 0