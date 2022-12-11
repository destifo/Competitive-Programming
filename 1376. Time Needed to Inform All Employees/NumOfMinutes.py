from collections import defaultdict
from typing import List


class Solution:
    
    def findTimeNeeded(self, node, graph, time) -> int:
        
        max_time = 0
        
        for emp in graph[node]:
            max_time = max(max_time, self.findTimeNeeded(emp, graph, time))
            
        return time[node] + max_time
    
    
    # O(n) time,
    # O(n) space,
    # Approach: dfs, recursion, 
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        
        for emp, boss in enumerate(manager):
            
            if boss == -1:
                continue
                
            graph[boss].append(emp)
            
        return self.findTimeNeeded(headID, graph, informTime)