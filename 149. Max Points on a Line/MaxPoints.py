from collections import defaultdict
from typing import List, Tuple


class Solution:
    
    def getLineProps(self, point1, point2) -> Tuple[int]:
        y_diff = point2[1]-point1[1]
        x_diff = point2[0]-point1[0]
        
        slope = float('inf') if x_diff == 0 else y_diff/x_diff
        if slope == 0:
            return slope, point1[1]
        
        if slope == float('inf'):
            return slope, point1[0]
        
        b = point1[1] - slope*point1[0]
        return slope, b
    
    
    # O(n^2) time,
    # O(n^2) space,
    # Approach: math, hashmap, 
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = defaultdict(set)
        max_points = 1
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                slope, b = self.getLineProps(points[i], points[j])
                lines[(slope, b)].add(tuple(points[i]))
                lines[(slope, b)].add(tuple(points[j]))
                max_points = max(max_points, len(lines[(slope, b)]))
        
        return max_points