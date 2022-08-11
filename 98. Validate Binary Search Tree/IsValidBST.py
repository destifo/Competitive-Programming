'''
https://leetcode.com/problems/validate-binary-search-tree/
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
    # O(n) space,
    # Approach: DFS, array
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nums = []
        
        def preOrderTraverse(root):
            
            val = root.val
            left = float('-inf')
            right = float('inf')
            
            if not root.left and not root.right:
                nums.append(val)
                return
            
            if root.left:
                preOrderTraverse(root.left)
            nums.append(val)
            if root.right:
                preOrderTraverse(root.right)
            
            
        preOrderTraverse(root)
        
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                return False
            
        return True

    
    # O(n) time,
    # O(1) space,
    # Approach: DFS,
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        
        def checkRange(root, lower_bound, upper_bound):
            
            if root == None:
                return True
            
            val = root.val
            if val > lower_bound and val < upper_bound:
                return checkRange(root.left, lower_bound, val) and checkRange(root.right, val, upper_bound)
            return False
        
        return checkRange(root, float('-inf'), float('inf'))