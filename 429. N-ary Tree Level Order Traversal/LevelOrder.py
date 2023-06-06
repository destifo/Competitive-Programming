'''
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
'''


from collections import deque
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # O(V + E) time,
    # O(V) space,
    # Approach: BFS, 
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:    return []        
        qu = deque()
        qu.append(root)
        traversal = []
        
        while qu:
            n = len(qu)
            level = []
            for i in range(n):
                nod = qu.popleft()
                for child in nod.children:
                    qu.append(child)
                level.append(nod.val)
            traversal.append(level)
            
        return traversal