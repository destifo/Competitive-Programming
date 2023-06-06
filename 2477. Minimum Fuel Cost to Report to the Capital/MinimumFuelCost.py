from collections import defaultdict
import math
from typing import List


class Solution:
    
    def minFuelToCapital(self, city, graph, parent):
        
        ppl = 1
        
        for nbr_city in graph[city]:
            if nbr_city != parent:
                ppl += self.minFuelToCapital(nbr_city, graph, city)
        
        if city != 0:
            self.fuel += math.ceil(ppl/self.seats)
        
        return ppl
    
    
    # O(n) time,
    # O(n) space,
    # Approach: dfs, math, 
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.seats = seats
        graph = defaultdict(list)
        for city1, city2 in roads:
            graph[city1].append(city2)
            graph[city2].append(city1)
            
        self.fuel = 0
        self.minFuelToCapital(0, graph, -1)
        
        return self.fuel