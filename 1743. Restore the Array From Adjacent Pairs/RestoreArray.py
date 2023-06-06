from collections import defaultdict
from typing import List


class Solution:
    
    
    # O(n) time,
    # O(n) space,
    # Approach: dfs, graph, 
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for pair in adjacentPairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
            
        start = None
        for num, nbrs in graph.items():
            if len(nbrs) == 1:
                start = num
                break
                
        stack = []
        prev = -1
        stack.append(start)
        nums = []
        
        while stack:
            num = stack.pop()
            nums.append(num)
            
            for nbr in graph[num]:
                if nbr != prev:
                    stack.append(nbr)
            prev = num
                    
        return nums