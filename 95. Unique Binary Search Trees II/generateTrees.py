'''
https://leetcode.com/problems/unique-binary-search-trees-ii/
'''


from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 0(n^3) time,
    # O(n^3) space,
    # Approach: dp, memoization
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nums = [i+1 for i in range(n)]
        memo = {}
        
        def generateTree(lst: List[int]) -> List[TreeNode]:
            if len(lst) == 0:
                return [None]
            
            if len(lst) == 1:
                return [TreeNode(lst[0])]
              
            if len(lst) == 2:
                tree1 = TreeNode(val=lst[0], right=TreeNode(lst[1]))
                tree2 = TreeNode(val=lst[1], left=TreeNode(lst[0]))
                return [tree1, tree2]
            
            if (lst[0], lst[-1]) in memo:
                return memo[(lst[0], lst[-1])]
            
            trees = []
            for i in range(len(lst)):
                possible_lefts = generateTree(lst[:i])
                possible_rights = generateTree(lst[i+1:])
                for left in possible_lefts:
                    for right in possible_rights:
                        tree = TreeNode(val=lst[i])
                        tree.left = left
                        tree.right = right
                        trees.append(tree)
                
            memo[(lst[0], lst[-1])] = trees
            return trees
        
        return generateTree(nums) 
    
    
    def generate(self, i: int, j: int, memo: Dict[Tuple[int], List[TreeNode]]) -> List[TreeNode]:
        
        if i > j:   return [None]
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        trees = []
        for k in range(i, j+1):
            left = self.generate(i, k-1, memo)
            right = self.generate(k+1, j, memo)
            
            for l in left:
                for r in right:
                    node = TreeNode(k)
                    node.left = l
                    node.right = r
                    trees.append(node)
                    
        memo[(i, j)] = trees
        return trees
    
    
    # O(n!) time,
    # O(n!) space,
    # Approach: dp, bst, 
    def generateTrees2(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        return self.generate(1, n, memo)