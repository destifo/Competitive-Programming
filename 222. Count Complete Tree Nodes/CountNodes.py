from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def findMaxHeight(self, node: Optional[TreeNode]):
        
        if not node:
            return 0
        
        return 1 + self.findMaxHeight(node.left)
    
    
    def count(self, node: Optional[TreeNode], nodes: List[int], height: int, max_height: int) -> bool:
        
        if not node:
            if height-1 == max_height:
                # print(height)
                nodes[0] += 1
            return max_height != height-1
        
        
        if self.count(node.left, nodes, height+1, max_height):
            return True
        if self.count(node.right, nodes, height+1, max_height):
            return True
        
        return False
    
    # O(L*h) time, L --> number of leaf nodes, h --> the height of the tree, less than O(n)
    # O(h) space,
    # Approach: dfs, math
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = [0]
        max_height = self.findMaxHeight(root)
        max_height -=1
        
        self.count(root, count, 0, max_height)
        
        total_nodes = count[0]//2
        if max_height > 0:
            total_nodes += int((2**max_height) - 1)
        
        return total_nodes