from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def isLeaf(self, node, sequence: List[int]) -> None:
        if not node:
            return
        
        is_leaf = not node.left and not node.right
        
        if is_leaf:
            sequence.append(node.val)
        else:
            self.isLeaf(node.left, sequence)
            self.isLeaf(node.right, sequence)
        
    
    # O(n + m) time,
    # O(n + m) space,
    # Approach: dfs, recursion
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        sequence1 = []
        sequence2 = []
        self.isLeaf(root1, sequence1)
        self.isLeaf(root2, sequence2)
        
        return sequence1 == sequence2