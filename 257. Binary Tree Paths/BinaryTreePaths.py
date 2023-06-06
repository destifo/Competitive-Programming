from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # O(nlogn) time,
    # O(nlogn) space,
    # Approach: dfs, binary tree, backtracking
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        
        def dfs(root: Optional[TreeNode], nodes: List[str]) -> None:
            
            left = root.left
            right = root.right
            
            if left is None and right is None:
                path = "".join(nodes)
                paths.append(path)
                return 
            
            if left:
                nodes.append(f'->{left.val}')
                dfs(left, nodes)
                nodes.pop()
                
            if right:
                nodes.append(f'->{right.val}')
                dfs(right, nodes)
                nodes.pop()
          
        dfs(root, [str(root.val)])
        return paths