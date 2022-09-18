'''
https://leetcode.com/problems/trapping-rain-water/
'''


from typing import List


class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: monotonic stack, array
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        
        result = 0
        
        for i in range(n):
            h = height[i]
            
            if not stack and h == 0:
                continue
            
            curr_lo = None
            while stack and stack[-1][0] <= h:
                if curr_lo != None and stack[-1][0] > curr_lo:
                    width = i - stack[-1][1] - 1
                    elvation = min(stack[-1][0], h) - curr_lo
                    result += width * elvation
                if stack[-1][0] == h:
                    break
                curr_lo = stack.pop()[0]
                
            if stack and stack[-1][0] > h and curr_lo != None:
                width = i - stack[-1][1] - 1
                elvation = h - curr_lo
                result += width * elvation
                
            stack.append((h, i))
                
        return result


sol = Solution()
print(sol.trap([4,2,0,3,2,5]))              