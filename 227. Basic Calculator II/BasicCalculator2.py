'''
https://leetcode.com/problems/basic-calculator-ii/submissions/
'''

class Solution:
    def calculate(self, s: str):
        stack = []
        n = len(s)
        index = 0
        op_dict = {
            '*': '*',
            '/': '//',
            '+': '//',
            '-': '-'
        }
        while index < len(s):
            if s[index] == ' ':
                index +=1
                continue
            if s[index] == "*":
                index +=1
                oprnd1 = stack.pop()
                oprnd2 = ''
                while index < n and s[index] not in op_dict.keys():
                    oprnd2 +=s[index]
                    index +=1
                oprnd2 = int(oprnd2)
                result = oprnd1*oprnd2
                stack.append(result)
                continue
            if s[index] == "/":
                index +=1
                oprnd1 = stack.pop()
                oprnd2 = ''
                while index < n and s[index] not in op_dict.keys():
                    oprnd2 +=s[index]
                    index +=1
                oprnd2 = int(oprnd2)
                result = oprnd1//oprnd2
                stack.append(result)
                continue

            if s[index] in op_dict.keys():
                stack.append(s[index])
                index +=1
                continue       

            num_str = ''
            while index < n and s[index] not in op_dict.keys():
                num_str +=s[index]
                index +=1
            
            stack.append(int(num_str))

        
        #while len(stack) > 1:
        #    oprnd2 = stack.pop()
        #    op = stack.pop()
        #    oprnd1 = stack.pop()
#
        #    if op == '+':
        #        stack.append(oprnd1 + oprnd2)
        #    else:
        #        stack.append(oprnd1 - oprnd2)

        if len(stack) == 1:
            return stack.pop()

        for i in range(0, len(stack), 2):
            oprnd1 = stack[i]
            op = stack[i + 1]
            oprnd2 = stack[i + 2]

            if op == '+':
                stack[i + 2] = (oprnd1 + oprnd2)
            else:
                stack[i + 2] = (oprnd1 - oprnd2)
            
            if (i + 2) == len(stack) - 1:   break
        
        return stack.pop()

sol = Solution()
print(sol.calculate("0-2147483647"))