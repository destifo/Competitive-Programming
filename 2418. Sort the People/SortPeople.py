from typing import List


class Solution:
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: sorting, 
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # bundle people with their height in a list
        height_to_name = [ (heights[i], names[i]) for i in range(len(names)) ]
        # sort the array in descending order
        height_to_name.sort(reverse=True)
        # return only the names
        return [name for height, name in height_to_name]