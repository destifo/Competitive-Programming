from collections import defaultdict, deque
from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: topological bfs, 
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        ppl = len(quiet)
        answer = [person for person in range(ppl)]
        
        for a, b in richer:
            graph[a].append(b)
        
        queue = deque()
        for p in range(ppl):
            queue.append(p)

        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                person = queue.popleft()
                
                for nbr in graph[person]:
                    if quiet[answer[person]] < quiet[answer[nbr]]:
                        answer[nbr] = answer[person]
                        queue.append(nbr)
                    
        return answer