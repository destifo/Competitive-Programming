from collections import Counter
import math
from typing import Dict, List


class Solution:
    
    def findOps(self, num: int, memo: Dict[int, int]) -> int:
        
        if num == 1:
            return float('inf')
        
        if num == 3 or num == 2:
            return 1
        
        if num in memo:
            return memo[num]
        
        ops = 1 + min(self.findOps(num-2, memo), self.findOps(num-3, memo))
        memo[num] = ops
        
        return ops
        
    
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: divide and conquer, top down dp
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        ans = 0
        memo = {}
        for cnt in count.values():
            curr = self.findOps(cnt, memo)
            if curr == float('inf'):
                return -1
            ans += curr
            
        return ans
    
    
    # O(n) time,
    # O(n) space,
    # Approach: counting, math
    def minOperations2(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        ans = 0
        for cnt in count.values():
            if cnt == 1:
                return -1
            ans += math.ceil(cnt/3)
            
        return ans