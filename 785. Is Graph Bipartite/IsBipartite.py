from typing import List


class Solution:
    
    def isBipartiteColorable(self, node: int, curr_color: int, graph: List[List[int]], color: List[int]) -> bool:
        
        if color[node] != 2 and color[node] != curr_color:
            return False
        
        if color[node] == curr_color:
            return True
        
        color[node] = curr_color
        next_color = (curr_color + 1)%2
        
        for nbr in graph[node]:
            if not self.isBipartiteColorable(nbr, next_color, graph, color):
                return False
            
        return True
    

    # O(n) time,
    # O(n) space,
    # Approach: dfs coloring, 
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [2 for _ in range(len(graph))]
        
        for node in range(len(graph)):
            if color[node] == 2 and not self.isBipartiteColorable(node, 0,  graph, color):
                return False
            
        return True