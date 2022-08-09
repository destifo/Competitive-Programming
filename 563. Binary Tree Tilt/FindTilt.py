'''
https://leetcode.com/problems/binary-tree-tilt/
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
    def findTilt(self, root: Optional[TreeNode]) -> int:
        result = [0]
        
        def dfs(root):
            if root == None:
                return 0
            
            val = root.val
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            result[0] +=abs(left_sum-right_sum)
            return val + left_sum + right_sum
        
        dfs(root)
        return result[0]