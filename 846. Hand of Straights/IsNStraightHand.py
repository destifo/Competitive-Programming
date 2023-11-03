from collections import defaultdict
from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: hashmap, greedy
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        nums_count = defaultdict(int)
        for num in hand:
            nums_count[num] += 1
            
        sorted_keys = sorted(nums_count.keys())
        for num in sorted_keys:
            while nums_count[num] > 0:
                for i in range(groupSize):
                    if nums_count[num+i] <= 0:
                        return False
                for i in range(groupSize):
                    nums_count[num+i] -= 1
                
        return True