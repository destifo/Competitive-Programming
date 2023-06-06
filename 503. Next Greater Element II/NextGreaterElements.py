'''
https://leetcode.com/problems/next-greater-element-ii/
'''


from typing import List


class Solution:
    # O(n) time, it's 2n to be precise
    # O(n) space, can grow max to 2n
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [-1] * n
        stack = []
        
        for i in range(2*n):
            i %= n
            num = nums[i]
            while stack and num > nums[stack[-1]]:
                answer[stack[-1]] = num
                stack.pop()
            
            if answer[i] == -1:
                stack.append(i)
                
        return answer

    
    # O(n) time, 2*n to be precise
    # O(n) space, 2*n as well
    # Approach: monotonic stack, hashtable
    def nextGreaterElements2(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        stack = []
        ans = [-1 for _ in range(nums_len)]
        i = 0
        
        while i < 2*nums_len:
            index = i % nums_len
            num = nums[index]
            
            while stack and num > nums[stack[-1]]:
                popped_index = stack.pop()
                if ans[popped_index] is -1:
                    ans[popped_index] = num
            stack.append(index)
            
            i +=1
                
        return ans