'''
https://leetcode.com/problems/insert-into-a-binary-search-tree/
'''


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # O(n) time, 
    # O(1) space,
    # Approach: DFS, 
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if root == None:
            root = node
            return root
        curr = root
        
        while True:
            if val < curr.val:
                if not curr.left:
                    curr.left = node
                    return root
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = node
                    return root
                curr = curr.right
        

    # O(n) time, 
    # O(1) space,
    # Approach: bst, greedy
    def insertIntoBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        prev = None
        curr = root
        new_nod = TreeNode(val)
        if root is None:    return new_nod
        
        while curr:
            prev = curr
            if val >= curr.val:
                curr = curr.right
            else:
                curr = curr.left
                
        if val > prev.val:
            prev.right = new_nod
        else:
            prev.left = new_nod
            
        return root