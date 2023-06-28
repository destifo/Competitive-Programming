from collections import defaultdict, deque
from typing import List


class Solution:
    
    # O(n*len(edges)) time,
    # O(n + len(edges)) space,
    # Approach: djikstra, 
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        probability = [0 for _ in range(n)]
        
        graph = defaultdict(list)
        for i in range(len(edges)):
            node1, node2 = edges[i]
            prob = succProb[i]
            graph[node1].append((node2, prob))
            graph[node2].append((node1, prob))
            
        queue = deque()
        queue.append((start, 1))
        
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                curr_node, curr_prob = queue.popleft()
                for nbr, prob in graph[curr_node]:
                    if curr_prob * prob > probability[nbr]:
                        probability[nbr] = curr_prob*prob
                        queue.append((nbr, curr_prob*prob))
        
        return probability[end]