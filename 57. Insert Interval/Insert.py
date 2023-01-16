from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: math, array, 
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        new_start = newInterval[0]
        new_end = newInterval[1]
        inserted = False
        
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                new_intervals.append(interval)
            if newInterval[0] >= interval[0] and newInterval[0] <= interval[1]:
                new_start = min(newInterval[0], interval[0])
            if interval[0] > newInterval[1]:
                if not inserted:
                    new_intervals.append([new_start, new_end])
                    inserted = True
                new_intervals.append(interval)
                
            if interval[0] <= newInterval[1]:
                new_end = max(newInterval[1], interval[1])
        
        if not inserted:
            new_intervals.append([new_start, new_end])
        
        return new_intervals