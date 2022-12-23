from typing import List
from collections import Counter


class Solution:
    
    def getPairs(self, val, count) -> int:
        
        answer = 0;
        for i in range(0, 22):
            power_of_two = 2**i
            target = power_of_two-val
            if target in count:
                answer += (count[target]-1) if target == val else count[target]
        
        return answer
        
    
    # O(n) time,
    # O(n) space,
    # Approach: hashtable, math
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = (10**9)+7
        answer = 0
        nums_count = Counter(deliciousness)
        for val in deliciousness:
            answer += self.getPairs(val, nums_count)
            
        answer //= 2
        answer %= MOD
        return answer