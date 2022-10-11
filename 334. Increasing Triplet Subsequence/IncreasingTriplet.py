from typing import List


class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: greedy, 
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min, second_min = float('inf'), float('inf')
        
        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = min(second_min, num)
            else:
                return True
            
        return False