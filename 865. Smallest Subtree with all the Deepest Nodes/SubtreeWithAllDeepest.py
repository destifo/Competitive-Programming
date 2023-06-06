'''
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
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
	# Approach: DFS, recursion
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        depth = [0]
        ancestor = [root]
        
        def findDepth(root, length):
            if root == None:
                return
            depth[0] = max(depth[0], length)
            findDepth(root.left, length+1)
            findDepth(root.right, length+1)
            
        
        def isDeepLeaf(node, l):
            return not node.left and not node.right and l == depth[0]
        
        def dfs(root, length):
            if isDeepLeaf(root, length):
                ancestor[0] = root
                return True
            
            left = False
            right = False
            if root.left:
                left = dfs(root.left, length+1)
            if root.right:
                right = dfs(root.right, length+1)
            
            if left and right:
                ancestor[0] = root
                return True
            if left or right:
                return True
            return False
        
        
        findDepth(root, 0)
        dfs(root, 0)
            
        return ancestor[0]