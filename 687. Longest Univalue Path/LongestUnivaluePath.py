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
    # Approach: DFS, recursion
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest_path = 0
        if not root:    return 0
        
        def findLongest(root: Optional[TreeNode]) -> int:
            
            left = root.left
            right = root.right
            curr_val = 1
            
            left_ans = 0
            if left:
                left_ans = findLongest(left)
                if root.val == left.val:
                    curr_val +=left_ans
                else:
                    left_ans = 0
            
            right_ans = 0
            if right:
                right_ans = findLongest(right)
                if root.val == right.val:
                    curr_val +=right_ans
                else:
                    right_ans = 0
            
            self.longest_path = max(self.longest_path, curr_val)
            return max(left_ans, right_ans) + 1
        
        findLongest(root)
        return self.longest_path-1