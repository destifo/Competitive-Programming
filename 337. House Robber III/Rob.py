from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def findMaxLoot(self, root: Optional[TreeNode], memo) -> Tuple[int]:
        if not root:
            return 0
        
        if root in memo:
            return memo[root]
        
        take = root.val
        if root.left:
            take += self.findMaxLoot(root.left.left, memo) + self.findMaxLoot(root.left.right, memo)
            
        if root.right:
            take += self.findMaxLoot(root.right.left, memo) + self.findMaxLoot(root.right.right, memo)
            
        skip = self.findMaxLoot(root.left, memo) + self.findMaxLoot(root.right, memo)
        
        memo[root] = max(take, skip)
        return memo[root]
            
            
    
    
    # O(n) time,
    # O(h) space, h --> height of the tree
    # Approach: tree, dp, memoization
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.findMaxLoot(root, {})