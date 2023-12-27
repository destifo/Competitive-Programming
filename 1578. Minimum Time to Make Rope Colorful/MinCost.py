import heapq
from typing import List


class Solution:
    # O(nlogn) time,
    # O(n) space,
    # Approach: heap, priority queue
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        min_heap = []
        min_cost = 0
        
        i = 0
        while i < n:
            nxt = i + 1
            heapq.heappush(min_heap, neededTime[i])
            while nxt < n and colors[i] == colors[nxt]:
                heapq.heappush(min_heap, neededTime[nxt])
                i = nxt
                nxt +=1
                
            while len(min_heap) > 1:
                min_cost +=heapq.heappop(min_heap)
            heapq.heappop(min_heap)
            i +=1
        
        return min_cost


    # O(n) time,
    # O(1) space,
    # Approach: simulation, 
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        min_cost = 0
        
        i = 0
        while i < n:
            nxt = i + 1
            max_time = neededTime[i]
            min_cost += neededTime[i]
            while nxt < n and colors[i] == colors[nxt]:
                min_cost += neededTime[nxt]
                max_time = max(max_time, neededTime[nxt])
                i = nxt
                nxt +=1
                
            min_cost -= max_time
            i +=1
        
        return min_cost
    
    
    # O(n) time,
    # O(1) space,
    # Approach: sliding window, two pointers, greedy
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        ans = 0
        
        left, right = 0, 0
        maxx, tot = 0, 0
        while right < n:
            if colors[left] != colors[right]:
                if right-left > 1:
                    ans += tot-maxx
                left = right
                tot = 0
                maxx = 0
                
            maxx = max(maxx, neededTime[right])
            tot += neededTime[right]
            right += 1
            
        if right-left > 1:
            ans += tot-maxx
                
        return ans