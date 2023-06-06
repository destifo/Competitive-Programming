'''
https://leetcode.com/problems/delete-nodes-and-return-forest/
'''


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time, n --> no of nodes
    # O(n) space, where all the nodes are to be deleted(worst case)
    # Approach: DFS, hashset
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        rem_roots = []
        to_del = set(to_delete)
        if root.val not in to_del:
            rem_roots.append(root)
        
        
        def dfs(root: Optional[TreeNode]) -> None:
            if root == None:
                return
            
            left = root.left
            right = root.right
            
            if root.val in to_del:
                if left and left.val not in to_del:
                    rem_roots.append(left)
                if right and right.val not in to_del:
                    rem_roots.append(right)
            else:
                if left and left.val in to_del:
                    root.left = None
                if right and right.val in to_del:
                    root.right = None
            
            dfs(left)
            dfs(right)
            
        dfs(root)
        # for root in rem_roots:
        #     print(root.val)
        
        return rem_roots