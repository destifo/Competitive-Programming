class Solution:
    
    # O(n) time,
    # O(1) space
    # Approach: stack, string
    def removeStars(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if ch == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
                
        return "".join(stack)