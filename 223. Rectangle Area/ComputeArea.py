class Solution:
    # O(1) time,
    # O(1) space,
    # Appraoch: math, geometry
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        rect1_area = abs(ax1-ax2)*abs(ay1-ay2)
        rect2_area = abs(bx1-bx2)*abs(by1-by2)
        total_area = rect1_area + rect2_area
        
        min_right = min(ax2, bx2)
        max_left = max(ax1, bx1)
        min_top = min(ay2, by2)
        max_bottom = max(ay1, by1)
        
        intersection_width, intersection_height = 0, 0
        if min_right > max_left:
            intersection_width = abs(min_right - max_left)
        if min_top > max_bottom:
            intersection_height = min_top - max_bottom
        
        intersection_area = (intersection_width*intersection_height)

        total_area -= intersection_area
        
        return total_area