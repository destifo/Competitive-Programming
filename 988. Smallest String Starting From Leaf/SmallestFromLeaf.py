from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # O(n*logn) time, n --> nodes, height = log(n)
    # O(n + log(n)) space,
    # Approach: dfs, backtracking
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(root: Optional[TreeNode], letters: List[str]) -> str:
            
            left = root.left
            right = root.right
            
            if left is None and right is None:
                word = "".join(letters[::-1])
                return word
            
            left_ans = None
            if left:
                letters.append(chr(left.val+97))
                left_ans = dfs(left, letters)
                letters.pop()
            
            right_ans = None
            if right:
                letters.append(chr(right.val+97))
                right_ans = dfs(right, letters)
                letters.pop()
                
            if left is None:
                return right_ans
            
            if right is None:
                return left_ans
            
            small_word = left_ans if left_ans < right_ans else right_ans
            return small_word
        
        return dfs(root, [chr(root.val+97)])