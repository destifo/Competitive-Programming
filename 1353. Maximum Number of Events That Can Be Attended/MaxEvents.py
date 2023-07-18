import heapq
from typing import List


class Solution:
    
    def addToChoices(self, choices: List[int], events: List[List[int]], day: int) -> None:
        
        while events and events[-1][0] <= day:
            heapq.heappush(choices, events.pop()[1])
            
        
    # O(nlogn) time,
    # O(n) space,
    # Approach: heap, sorting, greedy, 
    def maxEvents(self, events: List[List[int]]) -> int:
        choices = []
        attended = 0
        
        events.sort(reverse=True)
        last_day = max(max(event) for event in events)
        for day in range(1, last_day+1):
            self.addToChoices(choices, events, day)
            while choices and day > choices[0]:
                heapq.heappop(choices)
            if choices and day <= choices[0]:
                heapq.heappop(choices)
                attended += 1
                
        return attended