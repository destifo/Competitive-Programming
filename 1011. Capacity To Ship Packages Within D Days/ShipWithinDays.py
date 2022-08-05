'''
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
'''


from typing import List


class Solution:
    # O(nlogn) time,
    # O(1) space,
    # Approach: Binary Search,
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isWeightValid(w:int) -> bool:
            tot = 0
            rem_days = days-1
            
            for weight in weights:
                if weight > w:  return False
                
                if tot + weight > w:
                    if rem_days < 1:    return False
                    rem_days -=1
                    tot = 0
                tot += weight
                
            return True
        
        def binarySearchCapacity(start:int, end:int) -> int:
            mid = (start + end)//2
            weightIsValid = isWeightValid(mid)
            
            if weightIsValid and (mid == 1 or not isWeightValid(mid-1)):
                return mid
            elif start >= end-1:
                return end
            elif not weightIsValid:
                return binarySearchCapacity(mid, end)
            else:
                return binarySearchCapacity(start, mid)
            
        return binarySearchCapacity(1, sum(weights))