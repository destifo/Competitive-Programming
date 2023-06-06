from typing import List


class Solution:
    
    # O(len(logs)) time,
    # O(1) space,
    # Approach: array, 
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        
        for log in logs:
            if depth and log == "../":
                depth -= 1
            elif log != "./" and log != "../":
                depth += 1
                
        return depth