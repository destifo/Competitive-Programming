from typing import List


class Solution:
    
    def distribute(self, index, cookies, distribution):
        
        if index == len(cookies):
            return max(distribution)
        
        min_unfairness = float('inf')
        for i in range(len(distribution)):
            
            distribution[i] += cookies[index]
            if min_unfairness > distribution[i]:
                min_unfairness = min(min_unfairness, self.distribute(index+1, cookies, distribution))
                
            distribution[i] -= cookies[index]
            
        return min_unfairness
    
    
    # O(n^k) time,
    # O(max(n, k)) space,
    # Approach: backtracking, recursion
    def distributeCookies(self, cookies: List[int], k: int) -> int:
    
        return self.distribute(0, cookies, [0 for _ in range(k)])