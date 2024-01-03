from typing import List


class Solution:
    
    # O(n*m) time, n -> rows, m -> cols
    # O(1) space,
    # Approach: simulation, couting
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev, curr = 0, 0
        
        for floor in bank:
            for cell in floor:
                if cell == '1':
                    curr += 1
            
            ans += prev*curr
            if curr > 0:
                prev = curr
            curr = 0
                
        return ans