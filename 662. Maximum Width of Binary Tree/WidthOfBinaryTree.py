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
    # O(n) space,
    # Approach: bfs, binary tree
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_width = 1
        queue = deque()
        queue.append((root, 0))
        
        while queue:
            queue_len = len(queue)
            first_col, last_col = float('inf'), 0
            for _ in range(queue_len):
                node, col = queue.popleft()
                first_col = min(first_col, col)
                last_col = max(last_col, col)
                if node.left:
                    queue.append((node.left, 2*col+1))
                if node.right:
                    queue.append((node.right, 2*col+2))
            curr_width = (last_col-first_col) + 1
            max_width = max(max_width, curr_width)
        
        return max_width