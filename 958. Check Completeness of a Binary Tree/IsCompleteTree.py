from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def checkComplete(self, queue):
        
        for i in range(len(queue)-1):
            if queue[i] == None and queue[i+1] != None:
                return False
            
        return True
    
    
    # O(n) time,
    # O(h) space,
    # Approach: bfs, tree
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
                
        queue = deque()
        queue.append(root)
        uncomplete_level_found = False
        
        while queue:
            queue_len = len(queue)
            
            for _ in range(queue_len):
                nod = queue.popleft()
                
                if uncomplete_level_found and nod is not None:
                    return False
                
                if nod is None:
                    uncomplete_level_found = True
                    continue
                
                queue.append(nod.left)
                queue.append(nod.right)
                
            if not self.checkComplete(queue):
                return False
            
        return True