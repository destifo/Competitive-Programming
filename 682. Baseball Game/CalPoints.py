from typing import List


class Solution:
    
    # O(n) time, one pass
    # O(n) space,
    # Approach: stack
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        tot = 0
        
        for op in operations:
            if op == "+":
                scores.append(scores[-1]+scores[-2])
                tot += scores[-1]
            elif op == "D":
                scores.append(scores[-1]*2)
                tot += scores[-1]
            elif op == "C":
                tot -= scores.pop()
            else:
                scores.append(int(op))
                tot += scores[-1]
                
        return tot