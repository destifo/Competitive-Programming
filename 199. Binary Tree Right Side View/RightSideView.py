'''
https://leetcode.com/problems/binary-tree-right-side-view/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root):
        ans = []
        if not root:
            return ans
        qu = deque()
        qu.append(root)
        while qu:
            n = len(qu)
            curr = None
            for i in range(n):
                curr = qu.popleft()
                if curr and curr.left:
                    qu.append(curr.left)
                if curr and curr.right:
                    qu.append(curr.right)
            ans.append(curr.val)

        return ans