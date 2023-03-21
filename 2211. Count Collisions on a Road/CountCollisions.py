class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: stack, 
    def countCollisions(self, directions: str) -> int:
        stack = []

        collisions = 0
        for direction in directions:
            if not stack:
                stack.append(direction)
                continue
                
            curr = direction
            while stack:
                prev = stack[-1]
                if prev == "R" and curr == "L":
                    collisions += 2
                    curr = "S"
                    stack.pop()
                elif prev == "R" and curr == "S":
                    collisions += 1
                    stack.pop()
                elif prev == "S" and curr == "L":
                    collisions += 1
                    curr = "S"
                    stack.pop()
                else:
                    break
                    
            stack.append(curr)
                    
            
        return collisions