from typing import List


class Solution:
    
    # O(n^2) time,
    # O(1) space,
    # Approach: simulation, 
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target_ticket = tickets[k]
        time = 0
        
        for i in range(target_ticket-1):
            for j in range(len(tickets)):
                if tickets[j] > 0:
                    time += 1
                    tickets[j] -= 1
        
        for i in range(k+1):
            if tickets[i] > 0:
                time += 1
                tickets[i] -= 1
                
        return time
    

    # O(n) time,
    # O(1) space,
    # Approach: math, 
    def timeRequiredToBuy2(self, tickets: List[int], k: int) -> int:
        time = 0
        
        for i, curr_ticket in enumerate(tickets):
            time += min(tickets[k], curr_ticket) if i <= k else min(tickets[k]-1, curr_ticket) 
                
        return time