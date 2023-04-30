from typing import List


class Solution:
    
    def find(self, node: int, parent: List[int]) -> int:
        
        if node != parent[node]:
            parent[node] = self.find(parent[node], parent)
            
        return parent[node]
    
    
    def union(self, node1: int, node2: int, parent: List[List[int]]) -> None:
        
        p1 = self.find(node1, parent)
        p2 = self.find(node2, parent)
        
        if p1 < p2:
            parent[p2] = p1
        else:
            parent[p1] = p2
    
    
    # O(n + mlogm) time, m --> len(edges)
    # O(n) space,
    # Approach: union find, sorting, 
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parent1 = [i for i in range(n+1)]
        parent2 = [i for i in range(n+1)]
        removed_edges = 0
        
        edges.sort()
        
        while edges:
            edge_type, u, v = edges.pop()
            
            if edge_type == 3:
                if self.find(u, parent1) != self.find(v, parent1):
                    self.union(u, v, parent1)
                    self.union(u, v, parent2)
                else:
                    removed_edges += 1
            elif edge_type == 1:
                if self.find(u, parent1) != self.find(v, parent1):
                    self.union(u, v, parent1)
                else:
                    removed_edges += 1
            else:
                if self.find(u, parent2) != self.find(v, parent2):
                    self.union(u, v, parent2)
                else:
                    removed_edges += 1
                    
        p1 = None
        for i in range(1, n+1):
            parent1[i] = self.find(i, parent1)
            if p1 == None:
                p1 = parent1[i]
            elif p1 != parent1[i]:
                return -1

        p2 = None
        for i in range(1, n+1):
            parent2[i] = self.find(i, parent2)
            if p2 == None:
                p2 = parent2[i]
            elif p2 != parent2[i]:
                return -1
            
        return removed_edges