'''
https://leetcode.com/problems/construct-string-from-binary-tree/
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
    # Approach: DFS, recursion
    def tree2str(self, root: Optional[TreeNode]) -> str:
        str_lst = []
        
        def preOrderTraverse(root: Optional[TreeNode]) -> None:
            str_lst.append(str(root.val))
            
            if not root.left and not root.right:
                return
            
            if root.left:
                str_lst.append('(')
                preOrderTraverse(root.left)
                str_lst.append(')')
                
            if root.right:
                if not root.left:
                    str_lst.append('(')
                    str_lst.append(')')
                str_lst.append('(')
                preOrderTraverse(root.right)
                str_lst.append(')')
            
        preOrderTraverse(root)
        return ''.join(str_lst)


t  = TreeNode()
t.val = 1
t2 = TreeNode()
t2.val = 2
t3 = TreeNode()
t3.val = 3
t4 = TreeNode()
t4.val = 4
t.left = t2
t.right = t3
t2.right = t4
sol = Solution()
print(sol.tree2str(t))