'''
https://leetcode.com/problems/deepest-leaves-sum/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root):
        if not root:
            return 0

        monostack = [] # [(depth, val)]

        def dfs(root, depth):
            if not root:
                return

            if not root.right and not root.left:
                n = len(monostack)
                if monostack and monostack[n - 1][0] < depth:
                    monostack.clear()
                    monostack.append((depth, root.val))
                elif not monostack or monostack[n - 1][0] == depth:
                    monostack.append((depth, root.val))

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        tot = 0
        for leaf in monostack:
            tot +=leaf[1]

        return tot