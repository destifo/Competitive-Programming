from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: graph, tree, hashtable, 
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        incomings = defaultdict(int)
        
        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
                
            if child not in nodes:
                nodes[child] = TreeNode(child)
                
            incomings[child] += 1
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
        
        root = None
        for node in nodes.keys():
            if incomings[node] == 0:
                root = nodes[node]
                break
        
        return root