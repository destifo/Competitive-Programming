from typing import Dict, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def findFullBinaryTrees(self, n: int, memo: Dict[int, TreeNode]) -> None:
        
        if n in memo:
            return memo[n]
        
        memo[n] = []
        for i in range(1, n, 2):
            left_possible = self.findFullBinaryTrees(i, memo)
            right_possible = self.findFullBinaryTrees(n-i-1, memo)
            for left in left_possible:
                for right in right_possible:
                    new_node = TreeNode(0)
                    new_node.left, new_node.right = left, right
                    memo[n].append(new_node)
                    
        return memo[n]
        
    
    # O(2^n*n/2) time,
    # O(2^n*n/2*n) space,
    # Approach: top-down dp, tree
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        node = TreeNode(0)
        node.left, node.right = TreeNode(0), TreeNode(0)
        memo = {1: [TreeNode(0)], 3: [node]}
        return self.findFullBinaryTrees(n, memo) if n%2 == 1 else []