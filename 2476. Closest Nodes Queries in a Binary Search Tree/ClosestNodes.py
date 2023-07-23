from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def flattenBst(self, node: Optional[TreeNode], nums: List[int]) -> None:
        
        if not node:
            return 
        
        self.flattenBst(node.left, nums)
        nums.append(node.val)
        self.flattenBst(node.right, nums)
    
    
    
    def findPredecessor(self, nums: List[int], target: int) -> int:
        
        lo, hi = 0, len(nums)-1
        ans = -1
        
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return target
            elif nums[mid] < target:
                ans = nums[mid]
                lo = mid+1
            else:
                hi = mid-1
                
        return ans
    
    
    def findSuccessor(self, nums: List[int], target: int) -> int:
        
        lo, hi = 0, len(nums)-1
        ans = -1
        
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return target
            elif nums[mid] > target:
                ans = nums[mid]
                hi = mid-1
            else:
                lo = mid+1
                
        return ans
    
    
    # O(queries*logn) time,
    # O(queries) space,
    # Approach: binar search, bst, tree
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        ans = []
        nums = []
        self.flattenBst(root, nums)
        for num in queries:
            predecessor, successor = self.findPredecessor(nums, num), self.findSuccessor(nums, num)
            ans.append([predecessor, successor])
            
        return ans