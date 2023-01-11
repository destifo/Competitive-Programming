from collections import defaultdict, deque
from typing import List


class Solution:
    
    # O(buses + stations) time, not sure about the complexities
    # O(buses + stations) space,
    # Approach: bfs, 
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        buses_at_station = defaultdict(list)
        stations_in_bus = defaultdict(set)
        
        if source == target:
            return 0
        
        for bus, route in enumerate(routes):
            for stop in route:
                buses_at_station[stop].append(bus)
                stations_in_bus[bus].add(stop)
                
        visited_buses = set()
        visited_stations = set()
        queue = deque()
        ans = 1
        
        for bus in buses_at_station[source]:
            queue.append(bus)
            
        while queue:
            n = len(queue)
            for _ in range(n):
                curr_bus = queue.popleft()
                if target in stations_in_bus[curr_bus]:
                    return ans
                
                visited_buses.add(curr_bus)
                
                for station in stations_in_bus[curr_bus]:
                    if station in visited_stations:
                        continue
                    visited_stations.add(station)
                    for bus in buses_at_station[station]:
                        if bus in visited_buses:
                            continue
                        queue.append(bus)
                        visited_buses.add(bus)
            ans += 1
        
        return -1