'''
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
'''


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: DFS,
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        max_depth = 1
        
        while stack:
            nod, depth = stack.pop()
            max_depth = max(max_depth, depth)
        
            for child in nod.children:
                stack.append((child, depth+1))
        
        return max_depth