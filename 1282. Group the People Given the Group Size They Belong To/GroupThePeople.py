from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: hash map, 
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = []
        size_to_group = {}
        
        for p, size in enumerate(groupSizes):
            if size not in size_to_group:
                new_group = []
                size_to_group[size] = new_group
                groups.append(new_group)
                
            size_to_group[size].append(p)
            if len(size_to_group[size]) == size:
                size_to_group.pop(size)
                
        return groups