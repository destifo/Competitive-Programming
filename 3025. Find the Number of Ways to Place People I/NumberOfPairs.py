from typing import List


class Solution:

    def between_horizontal(self, static_y: int, x1: int, x2: int, points: List[List[int]]) -> bool:
        for x, y in points:
            if y == static_y and x1 < x < x2:
                return False
        
        return True

    def between_vertical(self, static_x: int, y1: int, y2: int, points: List[List[int]]) -> bool:
        for x, y in points:
            if x == static_x and y1 < y < y2:
                return False
        
        return True

    
    def inside_rect(self, point1: List[int], point2: List[int], points: List[List[int]]) -> bool:
        x1, y1 = point1
        x2, y2 = point2

        if not (x1 < x2 and y1 > y2):
            return False

        for x, y in points:
            if (x == x1 and y == y1) or (x == x2 and y == y2):
                continue

            if (x1 < x < x2 and min(y1, y2) < y <= max(y1, y2)) or ((x == x1 or x == x2) and min(y1, y2) <= y <= max(y1, y2)) or ((y == y1 or y == y2) and x1 <= x <= x2):
                return False

        return True

    def valid_pair(self, point1: List[int], point2: List[int], points: List[List[int]]) -> bool:
        x1, y1 = point1
        x2, y2 = point2

        if x1 == x2:
            return self.between_vertical(x1, y1, y2, points)

        if y1 == y2:
            return self.between_horizontal(y1, x1, x2, points)

        return self.inside_rect(point1, point2, points)

    # O(n^3) time,
    # O(1) space,
    # Approach: sorting, math
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort()

        pairs = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if self.valid_pair(points[i], points[j], points):
                    pairs += 1

        return pairs
