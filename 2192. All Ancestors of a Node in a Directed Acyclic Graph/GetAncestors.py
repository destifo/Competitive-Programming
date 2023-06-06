from typing import List


class Solution:
    
    # O(n^2) time,
    # O(n) space,
    # Approach: topological sort, topological dfs, dfs, stack
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = [[] for _ in range(n)]
        incomings = [0 for _ in range(n)]
        for edge in edges:  
            nod1, nod2 = edge
            graph[nod1].append(nod2)
            incomings[nod2] += 1
            
        
        stack = []
        answer = [ set() for _ in range(n) ]
        
        for node in range(n):
            if incomings[node] == 0:
                stack.append(node)
                
        while stack:
            node = stack.pop()
            
            for child in graph[node]: 
                incomings[child] -= 1
                
                for parent_ancestor in answer[node]:
                    answer[child].add(parent_ancestor)
                    
                answer[child].add(node)
                if incomings[child] == 0:
                    stack.append(child)
        
        for node, ancestors in enumerate(answer):
            answer[node] = list(ancestors)
            answer[node].sort()
        
        return answer