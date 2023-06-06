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
    # Approach: looping, bst
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

            while root:
                if root.val == val: break
                elif root.val > val:    root = root.left
                else:   root = root.right
                    
            return root


    # O(n) time,
    # O(n) space,
    # Approach: recursion, dfs, 
    def searchBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def searchTargetNode(curr: Optional[TreeNode]) -> Optional[TreeNode]:
            
            if curr is None:    return None
            
            if curr.val == val: return curr
            
            left = curr.left
            right = curr.right
            
            if curr.val > val:
                return searchTargetNode(left)
            
            return searchTargetNode(right)
            
        return searchTargetNode(root)