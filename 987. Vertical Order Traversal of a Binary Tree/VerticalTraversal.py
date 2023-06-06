'''
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
'''


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time, n --> number of nodes
    # O(n) space,
    # Approach: DFS, hashtable, 
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        cols = {}
        depth = [0]
        col_min_max = [0, 0]
        
        def dfs(nod: Optional[TreeNode], coord: List[int]) -> None:
            if nod == None: return
            
            row, col = coord
            col_min_max[0], col_min_max[1] = [min(col_min_max[0], col), max(col_min_max[1], col)]
            depth[0] = max(depth[0], row)
            if (col, row) not in cols.keys():
                cols[(col, row)] = []
            
            cols[(col, row)].append(nod.val)
            
            dfs(nod.left, [row+1, col-1])
            dfs(nod.right, [row+1, col+1])
            
        
        dfs(root, [0, 0])
        for i in range(col_min_max[0], col_min_max[1]+1):
            col_nums = []
            for j in range(depth[0]+1):
                if (i, j) not in cols.keys():   continue
                nums = cols[(i, j)]
                nums.sort()
                col_nums.extend(nums)
                
            ans.append(col_nums)
            
        return ans