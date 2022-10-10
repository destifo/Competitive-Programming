from collections import deque
from typing import List


class Solution:
    # O(E) time, E --> number of edges
    # O(E) space,
    # Approach: BFS, deque
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [set() for _ in range(n)]
        
        for parent, child in redEdges:
            graph[parent].add((child, 'R'))
            
        for parent, child in blueEdges:
            graph[parent].add((child, 'B'))
        
        answer = [-1 for _ in range(n)]
        
        root = 0
        qu = deque()
        qu.append((root, 'any'))
        vstd = set()
        depth = 0
        
        while qu:
            n = len(qu)
            
            for _ in range(n):
                nod, color = qu.popleft()
                if answer[nod] == -1:
                    answer[nod] = depth
                
                for nb, clr in graph[nod]:
                    if color == clr or (nod, nb, clr) in vstd: continue
                    vstd.add((nod, nb, clr))
                    qu.append((nb, clr))
            depth +=1
        
        return answer