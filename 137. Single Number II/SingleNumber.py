from collections import Counter
from typing import List


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: hashmap, 
    def singleNumber1(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        
        for num, count in count.items():
            if count == 1:
                return num
            
        return -1

    
    # O(n) time,
    # O(1) space,
    # Approach: bit manipulation, 
    def singleNumber(self, nums: List[int]) -> int:
        
        once, twice, thrice = 0, 0, 0
        
        for num in nums:
            
            twice |= num & once
            once ^= num
            thrice = once & twice
            once &= ~thrice
            twice &= ~thrice
            
        return once