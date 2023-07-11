from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # O(N + E) time,
    # O(N) space,
    # Approach: bfs, 
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        
        queue = deque()
        queue.append(root)
        
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                nod = queue.popleft()
                if nod.left:
                    queue.append(nod.left)
                    parent[nod.left] = nod
                    
                if nod.right:
                    queue.append(nod.right)
                    parent[nod.right] = nod
                    
        queue = deque()
        queue.append(target)
        visited = set()
        visited.add(target.val)
        depth = 0
        
        while queue:
            queue_len = len(queue)
            if depth == k:  return [node.val for node in queue]
            for _ in range(queue_len):
                nod = queue.popleft()
                if nod.left and nod.left.val not in visited:
                    queue.append(nod.left)
                    visited.add(nod.left.val)
                
                if nod.right and nod.right.val not in visited:
                    queue.append(nod.right)
                    visited.add(nod.right.val)
                    
                if nod in parent and parent[nod].val not in visited:
                    queue.append(parent[nod])
                    visited.add(parent[nod].val)
                    
            depth += 1
            
        return []