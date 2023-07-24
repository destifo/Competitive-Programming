from typing import Dict, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def isTreeBalanced(self, node: TreeNode, height: Dict[TreeNode, int]) -> bool:

        if node.left and not self.isTreeBalanced(node.left, height):
            return False

        if node.right and not self.isTreeBalanced(node.right, height):
            return False

        left_height = height[node.left] if node.left else 0
        right_height = height[node.right] if node.right else 0
        diff = abs(left_height-right_height)
        height[node] = max(left_height, right_height) + 1

        return True if diff < 2 else False


    # O(n) time,
    # O(h) space,
    # Approach: dfs, 
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.isTreeBalanced(root, {}) if root else True