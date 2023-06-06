'''
https://leetcode.com/problems/binary-tree-inorder-traversal/
'''


from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: DFS, recursion
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def inOrderTraverse(root: Optional[TreeNode]) -> None:
            if not root:    return
            
            inOrderTraverse(root.left)
            ans.append(root.val)
            inOrderTraverse(root.right)
            
        inOrderTraverse(root)
        return ans