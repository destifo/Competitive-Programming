from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # O(n) time, n -> no of nodes,
    # O(n) space,
    # Approach: bfs,
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = 0

        queue = deque()
        queue.append(root)

        while queue:
            queue_len = len(queue)
            curr_left = None
            for _ in range(queue_len):
                node = queue.popleft()
                if curr_left is None:
                    curr_left = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if curr_left is not None:
                ans = curr_left

        return ans
