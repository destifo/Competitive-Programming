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
    # Approach: DFS, recursion
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.tot = 0
        
        def sumLeftLeaves(curr: Optional[TreeNode], currIsLeft: bool) -> None:
            left = curr.left
            right = curr.right
            
            if left:
                sumLeftLeaves(left, True)
                
            if right:
                sumLeftLeaves(right, False)
                
            if not left and not right and currIsLeft:
                self.tot += curr.val
                
        sumLeftLeaves(root, False)
        return self.tot