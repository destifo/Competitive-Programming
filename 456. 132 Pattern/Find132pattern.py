from typing import List


class Solution:
    
    # O(n) time, 2 passes
    # O(n) space,
    # Approach: stack, hash map
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        prev_small = [float('-inf') for _ in range(n)]
        curr_small = nums[0]
        
        for i in range(1, n):
            num = nums[i]
            if curr_small < num:
                prev_small[i] = curr_small
            else:
                curr_small = num
                
        stack = []
        for i in range(n-1, 0, -1):
            num = nums[i]
            while stack and prev_small[i] >= stack[-1]:
                stack.pop()
                
            if stack and prev_small[i] != float('-inf') and stack[-1] < num:
                return True
            
            stack.append(num)
            
        return False
    
    
    # O(n) time,
    # O(n) space,
    # Approach: stack, more intuitive solution
    def find132pattern2(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []  # mono dec stack, store pair of (num, prev_min)
        minn = float('inf')
        
        for num in nums:
            while stack and num >= stack[-1][0]:
                stack.pop()
                
            if stack and stack[-1][1] < num:
                return True
            
            stack.append((num, minn))
            minn = min(minn, num)
            
        return False