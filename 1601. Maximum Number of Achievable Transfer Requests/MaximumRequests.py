from typing import List


class Solution:
    
    def isValidChange(self, change: List[int]) -> bool:
        return change.count(0) == len(change)
    
    
    def findMaxRequests(self, index: int, transfers: int, net_change: List[int], requests: List[List[int]]) -> int:
        if index == len(requests):
            return transfers if self.isValidChange(net_change) else 0
        
        to, From = requests[index]
        net_change[to] += 1
        net_change[From] -= 1
        take = self.findMaxRequests(index+1, transfers+1, net_change, requests)
        net_change[to] -= 1
        net_change[From] += 1
        
        skip = self.findMaxRequests(index+1, transfers, net_change, requests)
        
        return max(take, skip)
    
    
    # O(n*2^requests) time,
    # O(requests) space,
    # Apporach: backtracking, 
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        net_change = [0 for _ in range(n)]
        return self.findMaxRequests(0, 0, net_change, requests)