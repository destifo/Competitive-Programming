'''
https://leetcode.com/problems/average-of-levels-in-binary-tree/
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
    # O(n) time, 
    # O(depth) space,
    # Approach: BFS, 
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        lvl_avgs = []
        
        qu = deque()
        qu.append(root)
        
        while qu:
            n = len(qu)
            tot = 0
            for i in range(n):
                nod = qu.popleft()
                tot += nod.val
                
                if nod.left:    qu.append(nod.left)
                if nod.right:   qu.append(nod.right)
                    
            lvl_avgs.append(tot/n)
            
        return lvl_avgs