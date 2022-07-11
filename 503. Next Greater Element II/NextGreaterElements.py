'''
https://leetcode.com/problems/next-greater-element-ii/
'''


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