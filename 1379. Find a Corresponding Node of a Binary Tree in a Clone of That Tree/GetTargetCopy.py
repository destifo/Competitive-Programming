'''
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from turtle import right


class Solution:
    def getTargetCopy(self, original, cloned, target):
        if not original:
            return cloned
        if original == target:
            return cloned
        qu1 = deque()
        qu1.append(original)
        qu2 = deque()
        qu2.append(cloned)

        while qu1:
            m = len(qu1)
            for i in range(m):
                nod1 = qu1.popleft()
                nod2 = qu2.popleft()

                left1 = nod1.left
                left2 = nod2.left
                if left1 == target:
                    return left2

                right1 = nod1.right
                right2 = nod2.right
                if right1 == target:
                    return right2

                if left1:   qu1.append(left1)
                if right1:   qu1.append(right1)
                if left2:   qu2.append(left2)
                if right2:   qu2.append(right2)

        

                
        