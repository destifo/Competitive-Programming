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
    
    
    def findMaxLoot(self, root: Optional[TreeNode]) -> Tuple[int]:
        if not root:
            return 0, 0
        
        left = self.findMaxLoot(root.left)
        right = self.findMaxLoot(root.right)
        take = root.val + left[1] + right[1]
        skip = max(left) + max(right)
        
        return take, skip
    
    
    # O(n) time,
    # O(h) space, h --> height of the tree
    # Approach: tree, dfs, recursion
    def rob2(self, root: Optional[TreeNode]) -> int:
        return max(self.findMaxLoot(root))