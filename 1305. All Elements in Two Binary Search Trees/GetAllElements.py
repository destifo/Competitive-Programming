from collections import deque
from typing import List
from pyparsing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, node: Optional[TreeNode], l: List[int]) -> None:
        if not node:
            return

        self.flatten(node.left, l)
        l.append(node.val)
        self.flatten(node.right, l)

    # O(n+m) time,
    # O(n+m) space,
    # Approach: dfs,
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = deque()
        self.flatten(root1, list1)

        list2 = deque()
        self.flatten(root2, list2)

        ans = []
        while list1 and list2:
            if list1[0] < list2[0]:
                ans.append(list1.popleft())
            else:
                ans.append(list2.popleft())

        while list1:
            ans.append(list1.popleft())

        while list2:
            ans.append(list2.popleft())

        return ans
