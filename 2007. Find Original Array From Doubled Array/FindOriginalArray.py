from typing import List
from prometheus_client import Counter


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 == 1:
            return []
        
        original = []
        changed.sort()
        count = Counter(changed)
        
        for num in changed:
            if num in count and count[num] <= 0:
                continue
            double_num = num*2
            if double_num not in count or count[double_num] <= 0:
                return []
            
            count[double_num] -= 1
            count[num] -= 1
            original.append(num)
            
        return original