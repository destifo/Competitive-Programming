'''
https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/
'''


from collections import deque


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        
        mutables = []
        open = deque()
        balanced = 0
        
        for i in range(n):
            bracket = s[i]
            lckd = int(locked[i])
            if not lckd:
                mutables.append(i)
            
            if bracket == '(':
                open.append(i)
                balanced +=1
            
            if bracket == ')':
                if balanced > 0:
                    balanced -=1
                elif mutables:
                    mutables.pop()
                    if balanced < 1:
                        balanced +=1
                else:
                    return False
                
        if balanced > 0:
            for i in range(len(mutables)-1, -1, -1):
                if balanced == 0:
                    return True
                if s[mutables[i]] == ')': continue
                if mutables[i] >= open[0]:
                    open.popleft()
                    mutables.pop(0)
                    balanced -=2
             
        # print(balanced)
        return True if balanced == 0 else False


    
sol = Solution()
print(sol.canBeValid(")("
,"00"))
# "(((())"
# "110101"