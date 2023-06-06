from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: stack, iterative dfs
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []
        
        stack = []
        
        if root:
            stack.append(root)
        
        # do a curr_node -> right -> left traversal, then reverse
        while stack:
            
            node = stack.pop()
            
            answer.append(node.val)
            
            if node.left:
                stack.append(node.left)
                
            if node.right:
                stack.append(node.right)
        
        answer.reverse()
        return answer