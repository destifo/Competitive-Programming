
# Definition for a QuadTree node.
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    
    def constructNode(self, start, end, grid) -> 'Node':
        quad_node = Node()
        grid_val = -1
        is_leaf = True
        
        for col in range(start[0], end[0]):
            for row in range(start[1], end[1]):
                if grid_val == -1:
                    grid_val = grid[row][col]
                
                if grid[row][col] != grid_val:
                    is_leaf = False
                    break
                    
        quad_node.val = grid_val
        quad_node.isLeaf = is_leaf
        if is_leaf:
            return quad_node
        
        curr_size = (end[0]-start[0])//2
        mid_x = start[0] + curr_size
        mid_y = start[1] + curr_size
        quad_node.topLeft = self.constructNode(start, (mid_x, mid_y), grid)
        quad_node.topRight = self.constructNode((mid_x, start[1]), (end[0], mid_y), grid)
        quad_node.bottomLeft = self.constructNode((start[0], mid_y), (mid_x, end[1]), grid)
        quad_node.bottomRight = self.constructNode((mid_x, mid_y), end, grid)
        
        return quad_node
    
    # O(n^2) time,
    # O(n) space,
    # Approach: recursion, design
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.constructNode((0, 0), (len(grid), len(grid)), grid)