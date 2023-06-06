'''
https://leetcode.com/problems/merge-two-binary-trees/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) ->TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        qu1 = deque()
        qu1.append(root1)
        qu2 = deque()
        qu2.append(root2)
        
        def bfs():
            while qu1 and qu2:
                n = len(qu1)
                for i in range(n):
                    nod1 = qu1.popleft()
                    nod2 = qu2.popleft()
                    
                    nod1.val +=nod2.val
                    l1 = nod1.left
                    l2 = nod2.left
                    if l1 and l2:
                        qu1.append(l1)
                        qu2.append(l2)
                    if not l1 and l2:
                        nod1.left = l2
                        
                    r1 = nod1.right
                    r2 = nod2.right
                    if r1 and r2:
                        qu1.append(r1)
                        qu2.append(r2)
                    if not r1 and r2:
                        nod1.right = r2
            
        bfs()
        return root1