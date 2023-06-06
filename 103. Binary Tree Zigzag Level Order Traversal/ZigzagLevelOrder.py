'''
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
'''


from collections import deque
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # O(n * 2^(depth-1)) time, depth < 7
    # O(n) space,
    # Approach: BFS,
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        zigzag = []
        if not root:
            return zigzag
        
        qu = deque()
        qu.append(root)
        reverse = False
        
        while qu:
            n = len(qu)
            lvl = []
            for i in range(n):
                nod = qu.popleft()
                lvl.append(nod.val)
                
                if nod.left:    qu.append(nod.left)
                if nod.right:   qu.append(nod.right)
                    
            if reverse: lvl.reverse()
            zigzag.append(lvl)
            reverse = not reverse
        
        return zigzag