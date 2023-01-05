from collections import defaultdict
from typing import List, Set


class Solution:
    
    
    def pair(self, row: int, cost: List[List[int]], chosen_cols: Set[int], memo) -> int:
        if row >= len(cost):
            curr_cost = 0
            for col in range(len(cost[0])):
                if chosen_cols[col] < 1:
                    curr_cost += self.min_cost[col]
                    
            return curr_cost
        
        serialized_cols = ""
        for col, val in chosen_cols.items():
            if val > 0:
                serialized_cols += str(col)
                serialized_cols += "#"
        
        state = (row, serialized_cols)        
        if state in memo:
            return memo[state]
        
        min_cost = float('inf')
        
        for col in range(len(cost[row])):
            chosen_cols[col] += 1
            curr_cost = cost[row][col] + self.pair(row+1, cost, chosen_cols, memo)
            min_cost = min(min_cost, curr_cost)
            chosen_cols[col] -= 1
        
        memo[state] = min_cost
        return min_cost
    
    
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        
        # calculate min choice for each row
        self.min_cost = [float('inf') for _ in range(len(cost[0]))]
        for col in range(len(cost[0])):
            col_min = float('inf')
            for row in range(len(cost)):
                val = cost[row][col]
                col_min = min(col_min, val)
            self.min_cost[col] = col_min
            
        # do pairing, from rows to cols
        return self.pair(0, cost, defaultdict(int), {})