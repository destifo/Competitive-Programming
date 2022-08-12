'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: DFS,
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = [None]
        
        def dfs(root):
            this = False
            if root == p or root == q:
                this = True
            
            if root == None:
                return False
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left and right or (this and (right or left)):
                ans[0] = root
                return False
                
            return left or right or this
        
        dfs(root)
        return ans[0]