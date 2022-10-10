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
    # Approach: BFS, deque
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_tot = float('-inf')
        ans = 1
        
        qu = deque()
        qu.append(root)
        depth = 0
        
        while qu:
            n = len(qu)
            depth +=1
            curr_tot = 0
            for i in range(n):
                nod = qu.popleft()
                curr_tot += nod.val
                left = nod.left
                right = nod.right
                
                if left:
                    qu.append(left)
                if right:
                    qu.append(right)
            
            if max_tot < curr_tot:
                ans = depth
                max_tot = curr_tot
        
        return ans