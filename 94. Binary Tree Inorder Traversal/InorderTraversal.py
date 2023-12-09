'''
https://leetcode.com/problems/binary-tree-inorder-traversal/
'''


from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: DFS, recursion
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def inOrderTraverse(root: Optional[TreeNode]) -> None:
            if not root:    return
            
            inOrderTraverse(root.left)
            ans.append(root.val)
            inOrderTraverse(root.right)
            
        inOrderTraverse(root)
        return ans
    
    
    # O(n) time,
    # O(n^2) space,
    # Approach: recursion, 
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        
        return left + [root.val] + right
    
    
    def findPredecessor(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not node.right:
            return node
        
        return self.findPredecessor(node.right)
    
    
    def inorder(self, root: Optional[TreeNode], ans: List[int]) -> None:
        if not root:
            return
        
        if not root.left:
            ans.append(root.val)
            return self.inorder(root.right, ans)
        
        pred = self.findPredecessor(root.left)
        lefty = root.left
        root.left = None
        pred.right = root
        self.inorder(lefty, ans)
        
        
    
    
    # O(n) time,
    # O(1) space,
    # Approach: recursion, Morris traversal
    def inorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.inorder(root, ans)
        
        return ans