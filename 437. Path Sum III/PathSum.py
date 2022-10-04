from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # O(nlogn) time,
    # O(logn) space,
    # Approach: dfs, backtracking, prefix sum
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        
        def findNumPaths(root: Optional[TreeNode], tot: int, parent_prefix_sum) -> int:
            
            for num in parent_prefix_sum:
                if (tot-num) == targetSum:
                    self.paths +=1
            
            parent_prefix_sum.append(parent_prefix_sum[-1] + root.val)
            
            left = root.left
            right = root.right
            
            if left:
                findNumPaths(left, tot+left.val, parent_prefix_sum)
            
            if right:
                findNumPaths(right, tot+right.val, parent_prefix_sum)
                
            parent_prefix_sum.pop()
        
        if root is None:    return 0
        
        findNumPaths(root, root.val, [0])
        return self.paths