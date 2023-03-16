from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def _buildTree(self, start: int, end: int, postorder: List[int], nodes_index: int) -> Optional[TreeNode]:
        
        if start > end:
            return None
        
        val = postorder[self.postorder_index]
        self.postorder_index -= 1
        node = TreeNode(val)
        index = nodes_index[val]
        node.right = self._buildTree(index+1, end, postorder, nodes_index)
        node.left = self._buildTree(start, index-1, postorder, nodes_index)
        
        return node
    
    
    # O(n) time,
    # O(n) space,
    # Approach: divide and conquer, recursion, tree
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.postorder_index = len(postorder)-1
        nodes_index = {}
        for index, node_val in enumerate(inorder):
            nodes_index[node_val] = index
            
        return self._buildTree(0, len(postorder)-1, postorder, nodes_index)