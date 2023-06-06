from collections import defaultdict
from typing import List


class Solution:
    
    def findMinRoadDistance(self, city, graph, visited):
        
        if city in visited:
            return float('inf')
        
        min_score = float('inf')
        visited.add(city)
        for nbr_city, dist in graph[city]:
            min_score = min(min_score, dist, self.findMinRoadDistance(nbr_city, graph, visited))
            
        return min_score
    
    
    # O(n + len(roads)) time,
    # O(len(roads)) space,
    # Approach: dfs, graph, 
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for road in roads:
            src, dst, dist = road
            graph[src].append((dst, dist))
            graph[dst].append((src, dist))
            
        return self.findMinRoadDistance(1, graph, set())