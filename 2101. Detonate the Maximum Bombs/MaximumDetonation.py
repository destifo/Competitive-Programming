from collections import defaultdict, deque
from math import sqrt
from typing import Dict, List


class Solution:
    
    def countDetonatedBombs(self, index: int, graph: Dict[int, List[int]]) -> int:
        
        count = 1
        visited = set()
        queue = deque()
        visited.add(index)
        queue.append(index)
        
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                curr_index = queue.popleft()
                for i in graph[curr_index]:
                    if i in visited:
                        continue
                    count += 1
                    queue.append(i)
                    visited.add(i)
        
        return count
            
    
    # O(n^2) time,
    # O(n^2) space,
    # Approach: bfs, 
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        max_detonated = 1
        graph = defaultdict(list)
        for i in range(len(bombs)):
            x1, y1, radius1 = bombs[i]
            for j in range(i+1, len(bombs)):
                x2, y2, radius2 = bombs[j]
                dist = sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
                if dist <= radius1:
                    graph[i].append(j)
                if dist <= radius2:
                    graph[j].append(i)
                
        
        for i in range(len(bombs)):
            curr_detonated = self.countDetonatedBombs(i, graph)
            max_detonated = max(curr_detonated, max_detonated)
            
        return max_detonated