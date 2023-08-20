from collections import defaultdict
from typing import List


class Solution:
    
    def find(self, u: int, parent: List[int]) -> int:
        
        if u != parent[u]:
            parent[u] = self.find(parent[u], parent)
            
        return parent[u]
    
    
    def union(self, u: int, v: int, parent: List[int]) -> None:
        
        p1, p2 = parent[u], parent[v]
        if p1 < p2:
            parent[p2] = parent[p1]
        else:
            parent[p1] = parent[p2]
    
    
    def findMSTWeight(self, skip_index: int, include: int, n: int, edges: List[List[int]]) -> int:
        
        tot_weight = 0
        parent = [i for i in range(n)]
        if include != -1:
            u, v, weight = edges[include]
            tot_weight += weight
            self.union(u, v, parent)
            
        for i in range(len(edges)):
            if i == skip_index:
                continue
                
            u, v, weight = edges[i]
            if self.find(u, parent) != self.find(v, parent):
                tot_weight += weight
                self.union(u, v, parent)
        
        return tot_weight
                
    
    # O(n^2) time,
    # O(n^2) space,
    # Approach: union find, graph, 
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        index_of = defaultdict(int)
        for i, edge in enumerate(edges):
            index_of[tuple(edge)] = i
            
        edges.sort(key=lambda x:x[2])
        mst_weight = self.findMSTWeight(-1, -1, n, edges)
        critical, pseudo_critical = [], []
        for i in range(len(edges)):
            edge = tuple(edges[i])
            curr_weight = self.findMSTWeight(i, -1, n, edges)
            if curr_weight != mst_weight:
                critical.append(index_of[edge])
                continue

            curr_weight = self.findMSTWeight(-1, i, n, edges)
            if curr_weight == mst_weight:
                pseudo_critical.append(index_of[edge])
                
        return [critical, pseudo_critical]