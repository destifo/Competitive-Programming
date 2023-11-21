from collections import defaultdict
from typing import List


class Solution:
    
    def rev(self, num: int) -> int:
        num_str = str(num)
            
        return int(num_str[::-1])
    
    
    # O(n) time,
    # O(n) space,
    # Approach: hashmap, math
    def countNicePairs(self, nums: List[int]) -> int:
        '''
        
            x + rev(y) = y + rev(x)
            x - rev(x) = y - rev(y)
            
        '''
        MOD = 10**9 + 7
        ans = 0
        
        prev_agg = defaultdict(int)
        for i, num in enumerate(nums):
            agg = num - self.rev(num)
            ans += prev_agg[agg]
            prev_agg[agg] += 1
            
        return ans % MOD