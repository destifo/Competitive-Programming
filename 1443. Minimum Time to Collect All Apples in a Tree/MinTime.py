from collections import defaultdict
from typing import List


class Solution:
    
    def getTime(self, node, graph, hasApple, parent):
        
        tot_time = 0
        for nbr in graph[node]:
            if nbr == parent:   continue
            tot_time += self.getTime(nbr, graph, hasApple, node)
        
        if node != 0 and (tot_time > 0 or hasApple[node]):
            tot_time += 2
        
        return tot_time
    
    
    # O(n) time,
    # O(n) space,
    # Approach: dfs, recursion, 
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        # build graph
        graph = defaultdict(list)
        for edge in edges:
            nod1, nod2 = edge
            graph[nod1].append(nod2)
            graph[nod2].append(nod1)
        
        return self.getTime(0, graph, hasApple, -1)