from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def findMostLeft(self, node):
        while node.left:
            node = node.left
            
        return node.val
    
    
    # O(height) time,
    # O(height) space,
    # Approach: binary search tree, tree
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:
            if root.right:
                root.val = self.findMostLeft(root.right)
                root.right = self.deleteNode(root.right, root.val)
            else:
                return root.left
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
            
        return root