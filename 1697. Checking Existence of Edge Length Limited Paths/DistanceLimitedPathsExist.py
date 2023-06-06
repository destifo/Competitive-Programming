from typing import List


class Solution:
    
    def find(self, node: int, parent: List[int]) -> int:
        
        if node != parent[node]:
            parent[node] = self.find(parent[node], parent)
            
        return parent[node]
    
    
    def union(self, node1: int, node2: int, parent: List[int]) -> None:
        
        parent1 = self.find(node1, parent)
        parent2 = self.find(node2, parent)
        
        if parent1 < parent2:
            parent[parent2] = parent1
        else:
            parent[parent1] = parent2
    
    
    # O(len(edgeList)*log(len(edgeList)) + len(queries))*log(len(queries))) time,
    # O(len(queries) + O(n)) space,
    # Approach: union find, sorting
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        answer = [False for _ in range(len(queries))]
        parent = [i for i in range(n)]
        
        queries = [ (queries[i][0], queries[i][1], queries[i][2], i) for i in range(len(queries)) ]
        
        edgeList.sort(key=lambda x:x[2], reverse=True)
        queries.sort(key=lambda x:x[2], reverse=True)
        

        while queries:
            p, q, curr_limit, index = queries.pop()
            
            while edgeList and edgeList[-1][2] < curr_limit:
                u, v, _ = edgeList.pop() 
                self.union(u, v, parent)
            
            if self.find(p, parent) == self.find(q, parent):
                answer[index] = True
                
        return answer