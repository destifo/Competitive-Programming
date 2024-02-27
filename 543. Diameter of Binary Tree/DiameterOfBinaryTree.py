from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getDiameter(self, root: Optional[TreeNode]) -> Tuple[int, int]:

        if not root:
            return (0, 0)

        left_ans, left = self.getDiameter(root.left)
        right_ans, right = self.getDiameter(root.right)

        return (max(left + right, left_ans, right_ans), max(left, right) + 1)

    # O(n) time, n -> no of nodes
    # O(h) space, h -> height of the tree
    # Approach: dfs, tree
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.getDiameter(root)[0]
