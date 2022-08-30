'''
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
'''


from typing import List


class Solution:
    # O(nlogn) time,
    # O(1) space,
    # Approach: sorting, greedy
    def findMinArrowShots(self, points:List[List[int]]) -> int:
        n = len(points)
        points.sort()
        arrows = 0
        
        i = 0
        while i < n:
            arrows +=1
            curr = points[i]
            nxt = i+1
            hi = curr[1]
            while nxt < n and points[nxt][0] <= hi:
                hi = min(hi, points[nxt][1])
                nxt +=1
            i = nxt
            
        return arrows


sol = Solution()
print(sol.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))   