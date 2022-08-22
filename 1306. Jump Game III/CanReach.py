'''
https://leetcode.com/problems/jump-game-iii/
'''


from collections import deque
from typing import List


class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: BFS, 
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        
        def getNeighbours(i:int) -> List[int]:
            n = len(arr)
            neighbours = []
            
            # print(i)
            if (i + arr[i]) < n:
                neighbours.append(i + arr[i])
            if (i - arr[i]) > -1:
                neighbours.append(i - arr[i])
            
            return neighbours
        
        qu = deque()
        qu.append(start)
        vstd = set()
        vstd.add(start)
        
        while qu:
            m = len(qu)
            for i in range(m):
                nod = qu.popleft()
                
                if arr[nod] == 0:
                    return True
                
                nbrs = getNeighbours(nod)
                for nb in nbrs:
                    if nb in vstd:  continue
                    vstd.add(nb)
                    qu.append(nb)
                    
        return False