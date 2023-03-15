from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def doesExist(self, list_node, tree_node):
        
        if list_node is None:
            return True
        
        if not tree_node or tree_node.val != list_node.val:
            return False
        
        list_node = list_node.next
        return self.doesExist(list_node, tree_node.left) or self.doesExist(list_node, tree_node.right)
    
    
    # O(n*m) time,
    # O(n*m) space,
    # Approach: dfs, 
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        stack = []
        stack.append(root)
        
        while stack:
            tree_node = stack.pop()
            if not tree_node:
                continue
            if self.doesExist(head, tree_node):
                return True
            
            stack.append(tree_node.left)
            stack.append(tree_node.right)
            
        return False