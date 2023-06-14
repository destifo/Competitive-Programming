from typing import List


class Solution:
    
    # O(nlogn + mlogm) time,
    # O(1) space,
    # Approach: sorting, greedy, math
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9 + 7
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_height = 1
        for i in range(1, len(horizontalCuts)):
            height = horizontalCuts[i]-horizontalCuts[i-1]
            max_height = max(max_height, height)
            
        max_width = 1
        for i in range(1, len(verticalCuts)):
            width = verticalCuts[i]-verticalCuts[i-1]
            max_width = max(max_width, width)
            
        max_area = (max_height*max_width)%MOD
        return max_area