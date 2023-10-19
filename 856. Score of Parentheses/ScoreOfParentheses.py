from typing import List, Any


class Solution:
    
    def cascadeAdd(self, stack: List[Any]) -> None:
        while len(stack) > 2 and stack[-1] != "(" and stack[-2] != "(":
            last1 = stack.pop()
            last2 = stack.pop()
            stack.append(last1 + last2)
    
    
    # O(n) time,
    # O(n) space,
    # Approach: stack, 
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        stack = []
        
        for br in s:
            if br == "(":
                stack.append(br)
            else:
                last = stack.pop()
                if last == "(":
                    stack.append(1)
                    self.cascadeAdd(stack)
                elif stack and stack[-1] == "(":
                    stack.pop()
                    stack.append(last*2)
                    self.cascadeAdd(stack)

        return sum(stack)