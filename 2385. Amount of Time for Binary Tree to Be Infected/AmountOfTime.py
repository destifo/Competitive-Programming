from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    # O(N + E) time,
    # O(N) space,
    # Approach: bfs, 
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        parent = {}
        queue = deque()
        if not root:    return 0
        queue.append(root)
        start_node = None
        
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                nod = queue.popleft()
                if nod.val == start:
                    start_node = nod
                if nod.left:
                    parent[nod.left.val] = nod
                    queue.append(nod.left)
                    
                if nod.right:
                    parent[nod.right.val] = nod
                    queue.append(nod.right)
                    
        time = -1
        queue = deque()
        queue.append(start_node)
        visited = set()
        visited.add(start)
        
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                nod = queue.popleft()
                if nod.left and nod.left.val not in visited:
                    queue.append(nod.left)
                    visited.add(nod.left.val)
                    
                if nod.right and nod.right.val not in visited:
                    queue.append(nod.right)
                    visited.add(nod.right.val)
                    
                if nod.val in parent and parent[nod.val].val not in visited:
                    queue.append(parent[nod.val])
                    visited.add(parent[nod.val].val)
                    
            time += 1
            
        return time