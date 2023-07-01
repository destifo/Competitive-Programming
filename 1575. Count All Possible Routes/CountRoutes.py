from typing import Dict, List, Tuple


class Solution:
    
    def findRoutes(self, curr_city: int, finish: int, remaining_fuel: int, locations: List[int], memo: Dict[Tuple[int], int]) -> int:
        
        state = (curr_city, remaining_fuel)
        if state in memo:
            return memo[state]
        
        routes = 1 if curr_city == finish else 0
        for city in range(len(locations)):
            needed_fuel = abs(locations[city]-locations[curr_city])
            if city == curr_city or needed_fuel > remaining_fuel:
                continue
                
            routes += self.findRoutes(city, finish, remaining_fuel-needed_fuel, locations, memo)
        
        MOD = 10**9 + 7
        routes %= MOD
        memo[state] = routes
        return routes
    
    
    # O(fuel*len(locations)) time,
    # O(fuel*len(locations)) space,
    # Approach: top down dp, 
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        return self.findRoutes(start, finish, fuel, locations, {})