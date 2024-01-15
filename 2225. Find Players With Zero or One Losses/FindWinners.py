from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: hash map, 
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost = {}
        
        for winner, loser in matches:
            lost[winner] = lost.get(winner, 0)
            lost[loser] = lost.get(loser, 0) + 1
        
        ans = [[], []]
        for p, losses in lost.items():
            if losses == 0:
                ans[0].append(p)
                
            if losses == 1:
                ans[1].append(p)
        
        ans[0].sort()
        ans[1].sort()
        
        return ans