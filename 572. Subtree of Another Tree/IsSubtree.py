'''
https://leetcode.com/problems/subtree-of-another-tree/
'''


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subroot_val = subRoot.val
        
        def dfs(root):
            if root == None:    return False
            
            left = root.left
            right = root.right
            
            if root.val == subroot_val:
                return checkSubroot(root, subRoot) or dfs(left) or dfs(right)
            
            return dfs(left) or dfs(right)
        
        def checkSubroot(root, subroot):
            if root == None and subroot == None:
                return True
            
            if root == None:
                return False
            
            if subroot == None:
                return False
            
            if root.val != subroot.val:
                return False
            
            return checkSubroot(root.left, subroot.left) and checkSubroot(root.right, subroot.right)
        
        return dfs(root)