from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: graph, counting
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = [0 for _ in range(n)]
        for edge in edges:
            incoming[edge[1]] += 1
        
        ans = []
        for node in range(n):
            if incoming[node] == 0:
                ans.append(node)
                
        return ans