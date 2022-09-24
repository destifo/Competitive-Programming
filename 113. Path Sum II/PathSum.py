from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    # O(n) time,
    # O(h*l) space, h --> height, l --> number of leaf nodes
    # Approach: dfs, backtracking
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        curr_nums = []
        
        def dfs(root: Optional[TreeNode], tot) -> None:
            
            left = root.left
            right = root.right
            
            if not left and not right:
                if tot == targetSum:
                    ans.append(curr_nums[::])
                return
            
            if left:
                curr_nums.append(left.val)
                dfs(left, tot+left.val)
                curr_nums.pop()
                
            if right:
                curr_nums.append(right.val)
                dfs(right, tot+right.val)
                curr_nums.pop()
                
        if not root:
            return []
        
        curr_nums.append(root.val)
        dfs(root, root.val)
        return ans