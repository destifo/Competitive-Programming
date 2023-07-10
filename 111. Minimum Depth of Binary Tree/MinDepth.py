from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isLeaf(self, node: TreeNode) -> bool:
        return not (node.left or node.right)

    # O(n) time, but finds the nearest leaf fast
    # O(n) space,
    # Approach: bfs,
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        queue = deque()
        if not root:
            return depth
        queue.append(root)

        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                if self.isLeaf(node):
                    return depth + 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1

        return -1
