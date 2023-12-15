from collections import defaultdict
from typing import List


class Solution:
    
    # O(n) time,
    # O(n) time,
    # Approach: graph, hash map
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = defaultdict(int)
        
        for city1, city2 in paths:
            outgoing[city1] += 1
            outgoing[city2] = outgoing[city2]
            
        for city, outgoing_road in outgoing.items():
            if outgoing_road == 0:
                return city
            
        return ""