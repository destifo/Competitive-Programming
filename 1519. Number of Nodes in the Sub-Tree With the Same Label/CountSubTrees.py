from collections import defaultdict
from typing import List


class Solution:
    
    def copyCount(self, count1, count2):
        for char, cnt in count2.items():
            count1[char] += cnt
    
    
    def countNodesWithSameLevel(self, node, graph, labels, ans, parent):
        
        char_count = defaultdict(int)
        char_count[labels[node]] = 1
        for nbr in graph[node]:
            if nbr == parent:   continue
            nbr_char_count = self.countNodesWithSameLevel(nbr, graph, labels, ans, node)
            self.copyCount(char_count, nbr_char_count)
        
        ans[node] = char_count[labels[node]]
        return char_count
    
    
    # O(n + len(edges)) time, n --> nodes,
    # O(n + len(edges)) space,
    # Approach: dfs, hashmap, 
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0 for _ in range(n)]
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        self.countNodesWithSameLevel(0, graph, labels, ans, -1)
        return ans