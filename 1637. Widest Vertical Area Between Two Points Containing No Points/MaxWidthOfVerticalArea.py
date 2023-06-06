'''
https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
'''


class Solution:
    def maxWidthOfVerticalArea(self, points):
        points.sort(key=lambda x:x[0])
        n = len(points)
        max_width = 0
        for i in range(n-1):
            curr_point = points[i]
            next_point = points[i+1]
            x1 = curr_point[0]
            x2 = next_point[0]

            max_width = max(max_width, x2-x1)

        return max_width
