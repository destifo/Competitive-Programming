from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # O(n) time,
    # O(m) space, max number of nodes at any level
    # Approach: BFS, queue, deque
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node
        
        curr_depth = 1
        qu = deque()
        qu.append(root)
        
        while qu:
            if curr_depth == depth-1:
                break
                
            n = len(qu)
            for i in range(n):
                nod = qu.popleft()
                left = nod.left
                right = nod.right
                if left:
                    qu.append(left)
                if right:
                    qu.append(right)
                    
            curr_depth +=1
                
        while len(qu):
            nod = qu.popleft()
            left = nod.left
            right = nod.right
            new_node1 = TreeNode(val)
            new_node2 = TreeNode(val)
            new_node1.left = left
            new_node2.right = right
            nod.left = new_node1
            nod.right = new_node2
        
        return root