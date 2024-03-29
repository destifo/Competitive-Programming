from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.tot = 0
        
        def postOrderTraversal(root: TreeNode) -> None:
            if root is None:    return
        
            left = root.left
            right = root.right
            
            if right:
                postOrderTraversal(right)
            
            val = root.val
            root.val += self.tot
            self.tot +=val

            left_ans = 0
            if left:
                postOrderTraversal(left)
        
        postOrderTraversal(root)
        return root