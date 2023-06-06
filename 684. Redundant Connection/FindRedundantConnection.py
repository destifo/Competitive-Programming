from typing import List


class Solution:
    
    def find(self, parent: List[int], node: int) -> int:
        if node != parent[node]:
            parent[node] = self.find(parent, parent[node])
        return parent[node]
    
    
    def union(self, parent:List[int], node1: int, node2: int, size: List[int]) -> None:
        if size[parent[node1]] >= size[parent[node2]]:
            parent[parent[node2]] = parent[node1]
            size[parent[node1]] +=1
        else:
            parent[parent[node1]] = parent[node2]
            size[parent[node2]] += 1
    
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        parent = [ num for num in range(n+1) ]
        size = [ 0 for _ in range(n+1) ]
        
        for edge in edges:
            nod1, nod2 = edge
            
            if self.find(parent, nod1) == self.find(parent, nod2):
                return edge
            
            self.union(parent, nod1, nod2, size)
        
        print(parent)

        return []

    
sol = Solution()
print(sol.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]))