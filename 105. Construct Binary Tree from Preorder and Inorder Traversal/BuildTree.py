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

        val = preorder[self.preorder_index]
        node = TreeNode(val)
        index = nodes_index[val]
        self.preorder_index += 1
        node.left = self._buildTree(start, index-1, preorder, nodes_index)
        node.right = self._buildTree(index+1, end, preorder, nodes_index)
        
        return node
    
    
    # O(n) time,
    # O(n) space,
    # Approach: divide and conquer, 
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        nodes_index = {}
        self.preorder_index = 0
        for index, node in enumerate(inorder):
            nodes_index[node] = index

        return self._buildTree(0, len(inorder)-1, preorder, nodes_index)