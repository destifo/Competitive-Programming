from typing import Dict, List, Tuple


class Solution:
    
    def findLongest(self, index: int, last: int, pairs: List[List[int]], memo: Dict[Tuple[int], int]) -> int:
        
        if index == len(pairs):
            return 0
        
        state = (index, last)
        if state in memo:
            return memo[state]
        
        take = -float('inf')
        pair = pairs[index]
        if pair[0] > last:
            take = 1 + self.findLongest(index+1, pair[1], pairs, memo)
            
        skip = self.findLongest(index+1, last, pairs, memo)
        memo[state] = max(skip, take)
        return memo[state]
    
    
    # O(n^2) time,
    # O(n^2) space,
    # Approach: top down dp, 
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        return self.findLongest(0, -float('inf'),  pairs, {})
    
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: sorting, greedy, 
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        longest = 0
        
        last = -float('inf')
        for left, right in pairs:
            if last >= left:
                continue
                
            last = right
            longest += 1
            
        return longest