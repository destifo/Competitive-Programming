from typing import List


class Solution:
    # O(nlogn) time, n --> len(boxTypes) 
    # O(1) space,
    # Approach: greedy, sorting
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse=True, key=lambda x:x[1])
        tot_unit = 0
        
        for box_num, box_unit in boxTypes:
            if truckSize < 1:   break
            
            possible_boxes = min(truckSize, box_num)
            tot_unit += (box_unit*possible_boxes)
            truckSize -= possible_boxes
            
        return tot_unit