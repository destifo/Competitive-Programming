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
    # Approach: DFS, two pointers
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []
        
        def inOrderTraverse(root: Optional[TreeNode]) -> None:
            left = root.left
            if left:
                inOrderTraverse(left)
            
            nums.append(root.val)
            
            right = root.right
            if right:
                inOrderTraverse(right)
                
        inOrderTraverse(root)
        
        l, r = 0, len(nums)-1
        tot = nums[l] + nums[r]
        
        while l < r:
            if tot == k:
                return True
            elif tot < k:
                tot -=nums[l]
                l +=1
                tot +=nums[l]
            else:
                tot -=nums[r]
                r -=1
                tot +=nums[r]
                
        return False

    
    # O(n) time,
    # O(n) space,
    # Approach: DFS, hashset, 
    def findTarget2(self, root: Optional[TreeNode], k: int) -> bool:
        values = set()
        def dfs(root: Optional[TreeNode]) -> bool:
            
            value = k - root.val
            if value in values:
                return True
            values.add(root.val)
            
            left = dfs(root.left) if root.left else False
            right = dfs(root.right) if root.right else False
            
            return left or right
        
        return dfs(root)