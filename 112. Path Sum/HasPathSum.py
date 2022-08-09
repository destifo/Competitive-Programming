'''
https://leetcode.com/problems/path-sum/
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
    # Approach: DFS,
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def isLeaf(node) -> bool:
            return not node.left and not node.right
        
        def dfs(root, length):
            
            if root == None:
                return False
            
            if isLeaf(root):
                if length + root.val == targetSum:
                    return True
                return False
            return dfs(root.left, length+root.val) or dfs(root.right, length+root.val)
        
        return dfs(root, 0)