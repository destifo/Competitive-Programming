from typing import List


class Solution:
    
    def overlap(self, interval1: List[int], interval2: List[int]) -> bool:
        return interval1[1] > interval2[0]
    
    
    def chooseClosestEnding(self, interval1: List[int], interval2: List[int]) -> List[int]:
        
        return interval1 if interval1[1] < interval2[1] else interval2
    
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: stack, greedy, sorting 
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        stack = []

        for interval in intervals:
            added = interval
            if stack and self.overlap(stack[-1], interval):
                # greedy choice here, choose the interval with the smallest end value,
                added = self.chooseClosestEnding(interval, stack.pop())
            stack.append(added)
            
        return len(intervals)-len(stack)