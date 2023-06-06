from collections import defaultdict
from typing import List


class Solution:
    
    def find(self, node, parent):
        
        if node != parent[node]:
            parent[node] = self.find(parent[node], parent)
            
        return parent[node]
    
    
    def union(self, node1, node2, parent):
        parent1 = parent[node1]
        parent2 = parent[node2]
        
        if parent1 < parent2:
            parent[parent2] = parent1
        else:
            parent[parent1] = parent2
    
    
    # O(nodes + edges) time,
    # O(nodes) space,
    # Approach: union find, 
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        
        for edge in edges:
            nod1, nod2 = edge
            if self.find(nod1, parent) != self.find(nod2, parent):
                self.union(nod1, nod2, parent)
                
        parent_count = defaultdict(int)
        for i in range(n):
            parent_count[self.find(i, parent)] += 1
            
        answer = 0
        values = list(parent_count.values())
        for i in range(len(values)):
            val1 = values[i]
            disconnected_nodes = n - val1
            
            answer += (val1 * disconnected_nodes)
                
        return answer//2