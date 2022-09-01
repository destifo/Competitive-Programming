'''
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
'''


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
    def goodNodes(self, root: TreeNode) -> int:
        ans = [0]
        
        
        def dfs(root: TreeNode, max_val: int) -> None:
            if root == None:    return
            
            if root.val >= max_val:
                ans[0] +=1
                max_val = root.val
            
            dfs(root.left, max_val)
            dfs(root.right, max_val)
            
        
        
        dfs(root, root.val)
        
        return ans[0]