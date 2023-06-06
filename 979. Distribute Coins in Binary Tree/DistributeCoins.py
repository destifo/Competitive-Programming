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
    # Approach: dfs, 
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        
        def dfs(root: Optional[TreeNode], parent: Optional[TreeNode]) -> None:
            if root is None:    return
            
            left = root.left
            right = root.right
            
            if left:
                dfs(left, root)
                
            if right:
                dfs(right, root)
                
            if parent:
                if root.val == 1:   return
                if root.val < 1:
                    parent.val += (root.val-1)
                    self.moves += abs(root.val-1)
                    root.val = 1
                else:
                    parent.val += (root.val-1)
                    self.moves += abs(root.val-1)
                    root.val = 1
                    
        dfs(root, None)
        return self.moves