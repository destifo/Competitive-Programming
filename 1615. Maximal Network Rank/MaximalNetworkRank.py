from collections import defaultdict
from typing import List


class Solution:
    
    # O(n^2 + e) time,
    # O(n) space,
    # Approach: graph, 
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        edges_count = defaultdict(int)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
            edges_count[a] += 1
            edges_count[b] += 1
        
        sorted_count = sorted(edges_count.items(), key=lambda x:x[1])
        ans = 0
        for i in range(len(sorted_count)):
            a, e1 = sorted_count[i]
            for j in range(i+1, len(sorted_count)):
                b, e2 = sorted_count[j]
                rank = e1 + e2
                if b in graph[a]:
                    rank -= 1
                    
                ans = max(ans, rank)
                
        return ans