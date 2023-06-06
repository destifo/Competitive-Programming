from typing import List


class Solution:
    
    def findMaxValue(self, index: int, k: int, prefix_sum: List[List[int]], memo) -> int:
        
        if k == 0 or index == len(prefix_sum):
            return 0
        
        if (index, k) in memo:
            return memo[(index, k)]
        
        max_tot = 0
        for i in range(min(k+1, len(prefix_sum[index]))):
            curr_val = prefix_sum[index][i] + self.findMaxValue(index+1, k-i, prefix_sum, memo)
            max_tot = max(max_tot, curr_val)
            
        memo[(index, k)] = max_tot
        return max_tot
    
    
    # O(len(piles)*k) time,
    # O(len(piles)*k) space,
    # Approach: prefix sum, top down dp, 
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        prefix_sum = [[0] for _ in range(len(piles))]
        for i in range(len(piles)):
            tot = 0
            for coin in piles[i]:
                tot += coin
                prefix_sum[i].append(tot)
                
        return self.findMaxValue(0, k, prefix_sum, {})