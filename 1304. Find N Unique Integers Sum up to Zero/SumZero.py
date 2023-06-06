from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: math, 
    def sumZero(self, n: int) -> List[int]:
        elts = n//2
        curr_num = 1
        
        ans = []
        while elts:
            ans.append(curr_num)
            ans.append(-curr_num)
            elts -= 1
            curr_num += 1
            
        if n % 2 == 1:
            ans.append(0)
            
        return ans