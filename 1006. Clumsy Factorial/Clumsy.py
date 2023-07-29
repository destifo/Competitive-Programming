class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: stack, 
    def clumsy(self, n: int) -> int:
        stack = [n]
        
        turn = 0
        # multiplicaiton and division
        for num in range(n-1, 0, -1):
            if turn % 4 == 0:
                num1 = stack.pop()
                stack.append(num1*num)
            elif turn % 4 == 1:
                num1 = stack.pop()
                stack.append(num1//num)
            else:
                stack.append(num)
            turn += 1
            
        # addition and substraction
        turn = 0
        for i in range(1, len(stack)):
            if turn % 2 == 0:
                stack[i] += stack[i-1]
            else:
                stack[i] = stack[i-1]-stack[i]
            turn += 1
                
        return stack[-1]
    
    
    # O(1) time,
    # O(1) space,
    # Approach: math, simulation, 
    def clumsy(self, n: int) -> int:
        ans = {1: 1, 2: 2, 3: 6, 4: 7}
        additive = {0: 1, 1: 2, 2: 2, 3: -1}
        
        return ans[n] if n in ans else n + additive[n%4]