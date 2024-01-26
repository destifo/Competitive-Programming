from collections import deque
import math
from typing import List


class Solution:
    
    # O(m+n) time,
    # O(n) space,
    # Approach: greedy, array, simulation
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        missing_tot = mean*(n+m)-sum(rolls)
        missing_avg = missing_tot/n
        
        '''
            n numbers with a sum of missing_tot
            
            
        '''
        lower_bound, upper_bound = n*1, n*6
        if not (lower_bound <= missing_tot <= upper_bound):
            return []
        
        missing_mean = math.ceil(missing_tot/n)
        qtnt, rem = missing_tot//missing_mean, missing_tot % missing_mean
        ans = deque([missing_mean for _ in range(qtnt)])
        if rem != 0:
            ans.appendleft(rem)

        # disassemble larger numbers to small if the length is short
        while len(ans) < n:
            last = ans.pop()
            p1, p2 = math.floor(last/2), math.ceil(last/2)
            if p1 and p2:
                ans.appendleft(p1)
                ans.appendleft(p2)

        return ans