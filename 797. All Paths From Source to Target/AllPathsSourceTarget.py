'''
https://leetcode.com/problems/all-paths-from-source-to-target/
'''


from typing import List


class Solution:
    # O(n^2) time,
    # O(n^2) space,
    # Approach: DFS
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        
        def dfs(root:int, path: List[int]) -> None:
            if root == n-1:
                paths.append(path[::])
                
            children = graph[root]
            
            for child in children:
                path.append(child)
                dfs(child, path)
                path.pop()
                
        dfs(0, [0])
        
        return paths