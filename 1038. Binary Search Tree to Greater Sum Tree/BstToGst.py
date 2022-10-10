

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: DFS, post order traversal, recursion
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.tot = 0
        
        def postOrderTraversal(root: TreeNode) -> None:
        
            left = root.left
            right = root.right
            
            if right:
                postOrderTraversal(right)
            
            val = root.val
            root.val += self.tot
            self.tot +=val

            if left:
                postOrderTraversal(left)
        
        postOrderTraversal(root)
        return root