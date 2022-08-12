'''
https://leetcode.com/problems/recover-binary-search-tree/
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
    # Approach: Inorder DFS, recursion
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        swapped = []
        prev = [None]
        
        def findSwapped(root):
            if root == None:
                return
            
            findSwapped(root.left)
            
            if prev[0] != None and prev[0].val > root.val:
                if len(swapped) == 0:
                    swapped.append((prev[0], root))
                elif len(swapped) == 1:
                    swapped.append(root)
            
            prev[0] = root
            
            findSwapped(root.right)
        
        
        findSwapped(root)
        # print(swapped)
        if len(swapped) == 1:
            nod1 = swapped[0][0]
            nod2 = swapped[0][1]
            # print(nod1, nod2)
            temp = nod1.val
            nod1.val = nod2.val
            nod2.val = temp
        elif len(swapped) == 2:
            nod2 = swapped[0][0]
            nod1 = swapped[1]
            # print(nod1.val, nod2.val)
            temp = nod1.val
            nod1.val = nod2.val
            nod2.val = temp