'''
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(v) time,
    # O(1) space,
    # Approach: DFS,
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = [0]
        
        def dfs(root, p_val, gp_val):
            if not root:    return
            
            left = root.left
            right = root.right
            val = root.val
            
            if gp_val % 2 == 0:
                result[0] +=val
            
            dfs(left, val, p_val)
            dfs(right, val, p_val)
            
        dfs(root, 1, 1)
        return result[0]