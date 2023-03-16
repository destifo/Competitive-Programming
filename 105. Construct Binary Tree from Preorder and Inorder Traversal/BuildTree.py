from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def _buildTree(self, start, end, preorder, nodes_index) -> Optional[TreeNode]:
        
        if start > end:
            return None

        val = preorder[0]
        node = TreeNode(val)
        index = nodes_index[val]
        node.left = self._buildTree(start, index-1, preorder[1:], nodes_index)
        node.right = self._buildTree(index+1, end, preorder[1+(index-start):], nodes_index)
        
        return node
    
    
    # O(n*n) time,
    # O(n*n) space,
    # Approach: divide and conquer, 
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        nodes_index = {}
        for index, node in enumerate(inorder):
            nodes_index[node] = index

        return self._buildTree(0, len(inorder)-1, preorder, nodes_index)