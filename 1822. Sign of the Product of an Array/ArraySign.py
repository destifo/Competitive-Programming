from typing import List


class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: math, counting
    def arraySign(self, nums: List[int]) -> int:
        negative_count = 0
        
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                negative_count += 1
                
        return 1 if negative_count % 2 == 0 else -1