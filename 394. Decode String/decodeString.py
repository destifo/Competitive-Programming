'''
https://leetcode.com/problems/decode-string/submissions/
'''

class Solution:
    # had great help with the algorithm from neetcode, tnks
    def decodeString(self, s: str):
        stack = []

        for ch in s:
            if ch == ']':
                encoded_string = ""
                while stack and stack[-1] != '[':
                    encoded_string = stack.pop() + encoded_string
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                num = int(num[::-1])
                stack.append(encoded_string * num)
            else:
                stack.append(ch)
                
        
        return "".join(stack)


sol = Solution()
print(sol.decodeString("3[a2[c]]"))