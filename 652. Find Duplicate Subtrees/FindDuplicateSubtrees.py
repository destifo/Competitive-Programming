from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def serialize(self, node, answer, count):
        
        if not node:
            return ""
        
        serialized_form = ("(" + str(self.serialize(node.left, answer, count)) + ")" + str(node.val) + "(" + str(self.serialize(node.right, answer, count)) + ")")
        count[serialized_form] += 1
        
        if count[serialized_form] == 2:
            answer.append(node)
            
        return serialized_form
    
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        answer = []
        self.serialize(root, answer, defaultdict(int))
        return answer