import heapq
from typing import List


class Solution:
    # non optimal/ naive solution
    # Approach: DFS, 
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        min_refl = [float('inf')]
        
        def refill(index, refl, fuel, dist):
            if dist == target or fuel+dist >= target:
                min_refl[0] = min(min_refl[0], refl)
                return
            if index == len(stations):
                return
            
            for i in range(index, len(stations)):
                if stations[i][0] - dist > fuel:
                    break
                dist_diff = stations[i][0] - dist
                refill(i+1, refl+1, stations[i][1] + (fuel-dist_diff), stations[i][0])
                
        refill(0, 0, startFuel, 0)
        
        return min_refl[0] if min_refl[0] != float('inf') else -1


    # O(n) time, n --> len(stations)
    # O(n) space, 
    # Approach: heap(Priority queue), greedy
    def minRefuelStops2(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        max_heap = []
        
        refills = 0
        curr_fuel = startFuel
        
        for i in range(n):
            if curr_fuel == target: return refills
            dist = stations[i][0]
            while dist > curr_fuel:
                if not max_heap:
                    return -1
                fuel = -heapq.heappop(max_heap)
                curr_fuel += fuel
                refills +=1
            
            heapq.heappush(max_heap, -stations[i][1])
            
        while max_heap and curr_fuel < target:
            fuel = -heapq.heappop(max_heap)
            curr_fuel += fuel
            refills +=1
            
        if curr_fuel < target:
            return -1
            
        return refills