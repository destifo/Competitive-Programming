from typing import List, Tuple


class Solution:
    
    
    def findShortestPath(self, start: Tuple[int], end: Tuple[int]) -> int:
        seconds = 0
        start_x, start_y = start
        end_x, end_y = end
        dx = 1 if start_x < end_x else -1
        dy = 1 if start_y < end_y else -1
        
        x, y = start
        while x != end_x or y != end_y:
            if x == end_x or y == end_y:
                seconds += abs(x-end_x) + abs(y-end_y)
                return seconds
            x += dx
            y += dy
            seconds += 1
            
        return seconds
    
    
    # O(n*max(points)) time,
    # O(n*max(points)) space,
    # Approach: greedy, math
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0
        
        for i in range(len(points)-1):
            seconds += self.findShortestPath(tuple(points[i]), tuple(points[i+1]))
            
        return seconds