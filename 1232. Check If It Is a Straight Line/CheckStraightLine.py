import math
from typing import List


class Solution:
    
    def isOnLine(self, x: int, y: int, slope: int, b: int) -> int:
        
        if slope == math.inf:
            return x == b
        elif slope == 0:
            return y == b
        else:
            return y == slope*x + b
    
    # O(n) time,
    # O(1) space,
    # Approach: math, 
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        x_diff, y_diff = x2-x1, y2-y1
        slope = None
        b = None
        
        if x_diff == 0:
            slope = math.inf if y_diff > 0 else -math.inf
            b = x1
        elif y_diff == 0:
            slope = 0
            b = y1
        else:
            slope = y_diff/x_diff
            b = y1-slope*x1
            
        for x, y in coordinates:
            if not self.isOnLine(x, y, slope, b):
                return False
            
        return True