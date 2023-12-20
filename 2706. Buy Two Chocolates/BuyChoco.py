from typing import List


class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: array, greedy 
    def buyChoco(self, prices: List[int], money: int) -> int:
        minn1, minn2 = float('inf'), float('inf')
        
        for p in prices:
            if p < minn1:
                minn2 = minn1
                minn1 = p
            elif p < minn2:
                minn2 = p
                
        min_sum = minn1 + minn2
        return money if money < min_sum else money-min_sum