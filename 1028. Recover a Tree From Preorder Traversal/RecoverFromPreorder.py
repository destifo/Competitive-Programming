from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # O(n) time, n --> len(traversal)
    # O(h) space, h --> height of the tree
    # Approach: hash table, tree
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        level = defaultdict(TreeNode)
        root = None
        
        dashes = 0
        digits = []
        for i, ch in enumerate(traversal):
            if ch == "-":
                dashes += 1
            else:
                digits.append(ch)
                if i+1 < len(traversal) and traversal[i+1] != "-":
                    continue
                
                val = int("".join(digits))
                node = TreeNode(val)
                parent_level = dashes-1
                if parent_level >= 0:
                    parent = level[parent_level]
                    if not parent.left:
                        parent.left = node
                    else:
                        parent.right = node
                else:
                    root = node
                level[dashes] = node
                dashes = 0
                digits = []
                
        return root