import heapq
from typing import List


class Solution:
    # O(nlogn) time,
    # O(1) space,
    # Approach: sorting, greedy, 
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        
        inventory.sort(reverse=True)
        count = 1
        profit = 0
        MOD = (10**9) + 7
        
        for i in range(len(inventory)):
            
            if orders <= 0: break
            
            curr = inventory[i]
            prev = inventory[i+1] if (i+1) < len(inventory) else 0
            
            rounds = min(orders//count, curr-prev)
            orders -= (rounds * count)
            profit += ( ((curr+curr-rounds+1) * rounds)//2 ) * count
            profit %= MOD
            
            if (rounds < curr-prev):
                profit += (curr-rounds) * orders
                profit %= MOD
                break
                
            count += 1
                
        return profit