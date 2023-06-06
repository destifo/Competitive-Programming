from typing import List


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: direct pass, 
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []
        pivot_count = 0
        
        for num in nums:
            if num > pivot:
                greater.append(num)
            elif num < pivot:
                less.append(num)
            else:
                pivot_count +=1
                
        less.extend([pivot for i in range(pivot_count)])
        less.extend(greater)
        
        return less