from typing import List


class Solution:
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: sorting, greedy
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        tot_cost = 0
        
        for i in range(len(cost)):
            if (len(cost)-i-1) % 3 == 2:
                continue
                
            tot_cost += cost[i]
            
        return tot_cost