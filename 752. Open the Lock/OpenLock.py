from collections import deque
from typing import List


class Solution:
    # O(d^4) time, no of digits in the lock
    # O(d^4) space,
    # Approach: BFS, hashset
    def openLock(self, deadends: List[str], target: str) -> int:
        nbrs = [(9, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9), (8, 0)]
        
        lockLen = 4
        start = '0000'
        dends = set(deadends)
        if start in dends:  return -1
        dends.add('0000')
        
        minCost = 0
        qu = deque()
        qu.append(start)
        
        while qu:
            n = len(qu)
            for i in range(n):
                currState = qu.popleft()
                if currState == target: return minCost
                
                for i in range(lockLen):
                    num = int(currState[i])
                    down, up = nbrs[num]
                    nbr1 = "".join(currState[:i]) + str(down) + "".join(currState[i+1:])
                    nbr2 = "".join(currState[:i]) + str(up) + "".join(currState[i+1:])
                    if nbr1 not in dends:
                        dends.add(nbr1)
                        qu.append(nbr1)
                    
                    if nbr2 not in dends:
                        dends.add(nbr2)
                        qu.append(nbr2)
            minCost +=1
        return -1