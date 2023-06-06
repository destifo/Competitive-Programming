from collections import defaultdict
from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: hashtable, math
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        memo = defaultdict(int)
        ans = 0
        
        for t in time:
            t %= 60
            diff = 60-t
            diff %= 60
            ans += memo[diff]
            memo[t] += 1
            
        return ans