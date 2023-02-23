from typing import List


class Solution:
    
    def isInBetween(self, target, a, b):
        
        return target > a and target < b
    
    
    # O(1) time,
    # O(1) space,
    # Approach: math, 
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, x2 = rec1[0], rec1[2]
        y1, y2 = rec1[1], rec1[3]
        x3, x4 = rec2[0], rec2[2]
        y3, y4 = rec2[1], rec2[3]
        
        x_bounds, x_test = ([x1, x2], [x3, x4]) if abs(x1-x2) > abs(x3-x4) else ([x3, x4], [x1, x2])
        y_bounds, y_test = ([y1, y2], [y3, y4]) if abs(y1-y2) > abs(y3-y4) else ([y3, y4], [y1, y2])
        
        return (self.isInBetween(x_test[0], x_bounds[0], x_bounds[1]) or self.isInBetween(x_test[1], x_bounds[0], x_bounds[1])) and (self.isInBetween(y_test[0], y_bounds[0], y_bounds[1]) or self.isInBetween(y_test[1], y_bounds[0], y_bounds[1]))