from collections import defaultdict
from typing import List


class Solution:
    
    def find(self, node, parent):
        if node != parent[node]:
            parent[node] = self.find(parent[node], parent)
            
        return parent[node]
    
    
    def union(self, nod1, nod2, parent):
        
        if parent[nod1] == parent[nod2]:
            return
        
        if parent[nod1] < parent[nod2]:
            parent[parent[nod2]] = parent[nod1]
        else:
            parent[parent[nod1]] = parent[nod2]
    
    
    # O(nlogn) time, 
    # O(n) space,
    # Approach: union find, 
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        
        val_to_nodes = defaultdict(list)
        for node, val in enumerate(vals):
            val_to_nodes[val].append(node)
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        values = sorted(val_to_nodes.keys())
        
        parent = [ i for i in range(len(vals)) ]
        good_pathes = 0
        for val in values:
            groups = defaultdict(int)
            for node in val_to_nodes[val]:
                for nbr in graph[node]:
                    if vals[node] >= vals[nbr]:
                        self.union(node, nbr, parent)
                groups[self.find(node, parent)] += 1
            
            for group, size in groups.items():
                good_pathes += (size*(size+1))//2
                
        return good_pathes