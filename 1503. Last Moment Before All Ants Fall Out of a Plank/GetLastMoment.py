from typing import List


class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: brainteaser,
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        
        for ant_pos in left:
            ans = max(ans, ant_pos)
            
        for ant_pos in right:
            ans = max(ans, n-ant_pos)
            
        return ans