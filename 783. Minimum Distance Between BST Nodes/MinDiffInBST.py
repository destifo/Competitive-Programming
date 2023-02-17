from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: dfs
    def findMinDiff(self, node: Optional[TreeNode], curr_min: int, curr_max: int) -> int:
        
        if not node:
            return float('inf')
        
        min_diff = float('inf')
        if curr_min != float('inf'):
            min_diff = min(min_diff, abs(node.val-curr_min))
        if curr_max != float('-inf'):
            min_diff = min(min_diff, abs(curr_max-node.val))
        
        min_diff = min(min_diff, self.findMinDiff(node.left, min(curr_min, node.val), curr_max), self.findMinDiff(node.right, curr_min, curr_max = max(curr_max, node.val)))
        
        return min_diff
    
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        return self.findMinDiff(root, float('inf'), float('-inf'))