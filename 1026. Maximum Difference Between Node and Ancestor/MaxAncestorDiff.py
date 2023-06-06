

from collections import deque
import math
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    def findDiff(self, node, max_val, min_val) -> int:
        
        if not node:
            return -math.inf
        
        diff1 = abs(max_val-node.val)
        diff2 = abs(min_val-node.val)
        diff3 = self.findDiff(node.left, max(max_val, node.val), min(min_val, node.val))
        diff4 = self.findDiff(node.right, max(max_val, node.val), min(min_val, node.val))
        
        return max(diff1, diff2, diff3, diff4)
    

    # O(n) time,
    # O(n) space,
    # Approach: dfs, recursion
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.findDiff(root, root.val if root else None, root.val if root else None)

    
    # O(n) time,
    # O(n) space,
    # Approach: bfs, queue, iterative, 
    def maxAncestorDiff2(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        queue.append((root, root.val, root.val))
        answer = -math.inf
        
        while queue:
            
            queue_len = len(queue)
            for _ in range(queue_len):
                
                node, min_val, max_val = queue.popleft()
                diff1 = abs(node.val-min_val)
                diff2 = abs(node.val-max_val)
                answer = max(answer, diff1, diff2)
                
                if node.left:
                    queue.append((node.left, min(node.val, min_val), max(node.val, max_val)))
                    
                if node.right:
                    queue.append((node.right, min(node.val, min_val), max(node.val, max_val)))
                    
        return answer

sol = Solution()
tree = TreeNode(1)
tree.right = TreeNode(2)
right = tree.right
right.right = TreeNode(0)
right = right.right
right.left = TreeNode(3)
print(sol.maxAncestorDiff(tree))