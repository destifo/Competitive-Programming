from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # O(n) time, n --> nodes,
    # O(h) space, h --> height
    # Approach: dfs, backtracking
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        
        def dfs(root: Optional[TreeNode], nums: List[str]) -> None:
            left = root.left
            right = root.right
            
            if left is None and right is None:
                num = ''.join(nums)
                num = int(num)
                ans[0] += num
                return
            
            if left is not None:
                nums.append(str(left.val))
                dfs(left, nums)
                nums.pop()
            
            if right is not None:
                nums.append(str(right.val))
                dfs(right, nums)
                nums.pop()
                
        dfs(root, [str(root.val)])
        return ans[0]
    
    
    # O(n) time, n -> no of nodes,
    # O(n) space,
    # Approach: dfs, 
    def sumNumbers2(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        
        def is_leaf(node: Optional[TreeNode]) -> bool:
            return not node.left and not node.right
        
        
        def search_numbers(root: Optional[TreeNode], digits: List[int]) -> None:
            nonlocal ans
            if is_leaf(root):
                digits.append(str(root.val))
                num = int("".join(digits))
                ans += num
                digits.pop()
                return
            
            digits.append(str(root.val))
            if root.left:
                search_numbers(root.left, digits)
            if root.right:
                search_numbers(root.right, digits)
            digits.pop()
        
        if root:
            search_numbers(root, [])
        return ans