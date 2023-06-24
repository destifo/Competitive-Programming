import copy
from typing import List


class Solution:
    
    # O(len(rods)*max(rods)) time,
    # O(len(rods)*max(rods)) space,
    # Approach: dp out of this world, 
    def tallestBillboard(self, rods: List[int]) -> int:
        
        dp = {0: 0}
        
        for rod in rods:
            new_dp = copy.copy(dp)
            for diff, taller in dp.items():
                shorter = taller-diff
                
                # add to shorter,
                new_diff = abs(diff-rod)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), shorter+rod, taller)
                
                # add to taller,
                new_dp[diff+rod] = max(new_dp.get(diff+rod, 0), taller+rod)
            dp = new_dp
            
        return dp[0]