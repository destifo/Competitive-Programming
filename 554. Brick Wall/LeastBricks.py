from collections import defaultdict
from typing import List


class Solution:
    
    # O(n*m) time,
    # O(sum(row)) space,
    # Approach: reverse engineering, 
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        edges = defaultdict(int)
        max_edges = 0
        
        for row in wall:
            last_pos = 0
            for i in range(len(row)-1):
                brick = row[i]
                last_pos += brick
                edges[last_pos] += 1
                max_edges = max(max_edges, edges[last_pos])
        
        return len(wall) - max_edges