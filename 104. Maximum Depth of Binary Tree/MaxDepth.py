'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # O(2^n) time,
    # O(1) space,
    # Approach: DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root: Optional[TreeNode], depth:int) -> int:
            if root == None:
                return depth
            
            return max(dfs(root.left, depth+1), dfs(root.right, depth+1))
        
        return dfs(root, 0)