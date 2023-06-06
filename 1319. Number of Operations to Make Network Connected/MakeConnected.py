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
    
    
    # O(connections + n) time,
    # O(n) space,
    # Approach: union find, graph
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        
        parent = [i for i in range(n)]
        for connection in connections:
            pc1, pc2 = connection
            if self.find(pc1, parent) != self.find(pc2, parent):
                self.union(pc1, pc2, parent)
                
        networks = set()
        for i in range(n):
            networks.add(self.find(i, parent))
            
        return len(networks)-1