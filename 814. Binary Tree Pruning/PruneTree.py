'''
https://leetcode.com/problems/binary-tree-pruning/
'''


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: dfs, recursion,
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root: Optional[TreeNode]) -> bool:
            
            if root == None:
                return False
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if not left:
                root.left = None
            if not right:
                root.right = None
                
            return root.val or left or right
        
        if not dfs(root):   return None
        
        return root