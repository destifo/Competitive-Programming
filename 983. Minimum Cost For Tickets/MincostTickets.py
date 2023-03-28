from typing import List


class Solution:
    
    def minCost(self, curr_day, days, days_set, costs, memo):
        
        if curr_day > days[-1]:
            return 0
        
        if curr_day in memo:
            return memo[curr_day]
        
        if curr_day not in days_set:
            memo[curr_day] = self.minCost(curr_day+1, days, days_set, costs, memo)
            return memo[curr_day]
        
        day_pass = [1, 7, 30]
        min_cost = float('inf')
        for i in range(len(costs)):
            next_pay_day = curr_day + day_pass[i]
            min_cost = min(min_cost, costs[i] + self.minCost(next_pay_day, days, days_set, costs, memo))
        
        memo[curr_day] = min_cost
        return min_cost
        
    
    # O(len(days)) time,
    # O(len(days)) space,
    # Approach: top down dp, memoization,
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days.sort()
        
        return self.minCost(days[0], days, set(days), costs, {})