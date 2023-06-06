from typing import List


class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: sorting, math, 
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1]-arr[0]
        
        for i in range(1, len(arr)):
            if (arr[i] - arr[i-1]) != diff:
                return False
            
        return True