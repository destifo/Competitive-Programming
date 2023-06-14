# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def findMinDifference(self, node: Optional[TreeNode]) -> None:
        if not node:
            return

        self.findMinDifference(node.left)
        if self.prev != None:
            self.min_diff = min(self.min_diff, abs(node.val - self.prev))
        self.prev = node.val
        self.findMinDifference(node.right)

    # O(n) time,
    # O(n) space,
    # Approach: dfs, bst,
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float("inf")

        self.findMinDifference(root)
        return self.min_diff

    # O(n) time,
    # O(1) space,
    # Approach: dfs, stack, bst,
    def getMinimumDifference2(self, root: Optional[TreeNode]) -> int:
        stack = []
        stack.append((root, root.val, root.val))
        ans = float("inf")

        while stack:
            node, right_prev, left_prev = stack.pop()
            left = node.left
            if left:
                curr_diff = abs(node.val - left.val)
                ans = min(ans, curr_diff)
                ans = min(ans, abs(left.val - left_prev))
                stack.append((left, node.val, left_prev))

            right = node.right
            if right:
                curr_diff = abs(node.val - right.val)
                ans = min(ans, curr_diff)
                ans = min(ans, abs(right.val - right_prev))
                stack.append((right, right_prev, node.val))

        return ans
