'''
https://leetcode.com/problems/symmetric-tree/
'''


from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time,
    # O(2^depth + 2^(depth-1)) space,
    # Approach: BFS, 
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        qu1 = deque()
        qu1.append(root)
        qu2 = deque()
        qu2.append(root)
        
        while qu1 and qu2:
            n = len(qu1)
            m = len(qu2)
            
            if n != m:
                return False
            
            for i in range(n):
                nod1 = qu1.popleft()
                nod2 = qu2.pop()
                
                if not nod1 and not nod2:
                    continue
                
                if not nod1 or not nod2:    return False
                    
                if nod1.val != nod2.val:    return False
                
                qu1.append(nod1.left)
                qu1.append(nod1.right)
                
                qu2.appendleft(nod2.right)
                qu2.appendleft(nod2.left)
                    
        return True