# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getSum(self, node: Optional[TreeNode]) -> float:
        
        if not node:
            return 0
        
        left_path_sum = self.getSum(node.left) + node.val
        right_path_sum = self.getSum(node.right) + node.val
        
        merged_path_sum = left_path_sum + right_path_sum - node.val
        
        self.max_path_sum = max(self.max_path_sum, left_path_sum, right_path_sum, merged_path_sum, node.val)
        
        return max(left_path_sum, right_path_sum, node.val)
        
    
    # O(n) time,
    # O(n) space, for the recursive call stack
    # Approach: dfs, recursion, 
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = -math.inf
        self.getSum(root)
        
        return self.max_path_sum