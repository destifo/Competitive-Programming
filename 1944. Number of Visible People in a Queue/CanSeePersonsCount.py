from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: monotonic stack, 
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = [] # mono dec stack
        ans = [0 for _ in range(len(heights))]
        
        for i, h in enumerate(heights):
			
			# the ppl getting popped can see the person who is popping them from the stack
            while stack and heights[stack[-1]] < h:
                ans[stack.pop()] += 1
            
			# the person who is on top of the stack can see person beinng pushed to the stack
            if stack:
                ans[stack[-1]] += 1
            stack.append(i)
            
                
        return ans