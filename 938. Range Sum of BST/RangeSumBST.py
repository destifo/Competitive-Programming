

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def findRangeSum(self, node: Optional[TreeNode], low: int, high: int) -> int:
        
        if not node:
            return 0
        
        tot = 0 if (node.val < low or node.val > high) else node.val
        
        tot += self.findRangeSum(node.left, low, high)
        tot += self.findRangeSum(node.right, low, high)
        
        return tot
    
    
    # O(n) time,
    # O(logn) space,
    # Approach: dfs, recursion, intuitve
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        return self.findRangeSum(root, low, high)


    def findRangeSum2(self, node: Optional[TreeNode], low: int, high: int) -> int:
        
        if not node:
            return 0
        
        tot = 0 if (node.val < low or node.val > high) else node.val
        
        if node.val >= low:
            tot += self.findRangeSum2(node.left, low, high)
        if node.val <= high:
            tot += self.findRangeSum2(node.right, low, high)
        
        return tot
    
    
    # O(n) time,
    # O(logn) space,
    # Approach: dfs, recursion, improved using bst property
    def rangeSumBST2(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        return self.findRangeSum2(root, low, high)

    
    # O(n) time,
    # O(1) space,
    # Approach: dfs, iterative, 
    def rangeSumBST3(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        stack = []
        stack.append(root)
        
        tot = 0
        
        while stack:
            
            node = stack.pop()
            if not node:
                continue
                
            val = node.val
            
            if val >= low and val <= high:
                tot += val
                
            if val < high:
                stack.append(node.right)
                
            if val > low:
                stack.append(node.left)
                
        return tot
    
    
    # O(n) time,
    # O(h) space, h -> height of the tree
    # Approach: bst, recursion
    def rangeSumBST4(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        tot = root.val if low <= root.val <= high else 0
        if root.val >= low:
            tot += self.rangeSumBST(root.left, low, high)
        
        if root.val <= high:
            tot += self.rangeSumBST(root.right, low, high)
            
        return tot