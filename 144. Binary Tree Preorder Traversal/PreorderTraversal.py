

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def traverse(self, node, lst) -> None:
        
        if not node:
            return
        
        lst.append(node.val)
        
        self.traverse(node.left, lst)
        self.traverse(node.right, lst)
    
    
    # O(n) time,
    # O(n) space,
    # Approach: recursion, dfs 
    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        
        pre_traversal = []
        
        self.traverse(root, pre_traversal)
        
        return pre_traversal

    
    # O(n) time,
    # O(n) space,
    # Approac: stack, dfs
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        preorder_traversal = []
        
        if root:
            stack.append(root)
            
        while stack:
            
            node = stack.pop()
            
            preorder_traversal.append(node.val)
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
                
        return preorder_traversal