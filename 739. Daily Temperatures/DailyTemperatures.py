'''
https://leetcode.com/problems/daily-temperatures/
'''


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = []
        answer = [0] * n
        
        for i in range(n):
            temp = temperatures[i]
            while stack and temp > temperatures[stack[-1]]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
            
        return answer