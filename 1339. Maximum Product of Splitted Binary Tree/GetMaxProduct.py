

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def getNodesSum(self, node) -> int:
        
        if not node:
            return 0
        
        return self.getNodesSum(node.left) + node.val + self.getNodesSum(node.right)
    
    
    def getMaxProduct(self, node, tot_sum) -> int:
        
        if not node:
            return 0
        
        left_sum = self.getMaxProduct(node.left, tot_sum)
        right_sum = self.getMaxProduct(node.right, tot_sum)
        
        self.max_prod = max(self.max_prod, left_sum*(tot_sum-left_sum))
        self.max_prod = max(self.max_prod, right_sum*(tot_sum-right_sum))
        
        return left_sum + node.val + right_sum
        
    
    # O(n) time, 
    # O(n) space, for the call stack space
    # Approach: dfs, recursion, brainteaser, tree
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = (10**9) + 7
        self.max_prod = 0
        self.getMaxProduct(root, self.getNodesSum(root))
        
        return self.max_prod % MOD